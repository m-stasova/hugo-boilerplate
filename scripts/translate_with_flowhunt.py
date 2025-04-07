#!/usr/bin/env python3
"""
translate_with_flowhunt.py

This script translates files from /content/en/* to all language variations defined in /content/[lang]/
that don't already exist in the target language directories using FlowHunt API.

Usage:
    python translate_with_flowhunt.py [--path /path/to/content] [--check-interval 60] [--max-concurrent 10]

Prerequisites:
    - Python 3.6 or higher
    - FlowHunt API key (set in .env file or as environment variable API_KEY)
    - Required packages: flowhunt, tqdm, python-dotenv

Examples:
    # Basic usage (will use ../content/ relative to the script location)
    python translate_with_flowhunt.py
    
    # With explicit path
    python translate_with_flowhunt.py --path /Users/username/work/hugo-boilerplate/content
    
    # With API key as environment variable
    export FLOWHUNT_API_KEY="your-api-key"
    python translate_with_flowhunt.py
"""

import os
import sys
import argparse
import time
import json
from pathlib import Path
from tqdm import tqdm
from dotenv import load_dotenv
import flowhunt
from pprint import pprint

# Load environment variables from .env file
script_dir = os.path.dirname(os.path.abspath(__file__))
hugo_root = os.path.dirname(os.path.dirname(os.path.dirname(script_dir)))  # Adjusted to point to the correct root
env_path = os.path.join(script_dir, '.env')
if os.path.exists(env_path):
    print(f"Loading environment variables from {env_path}")
    load_dotenv(env_path)
else:
    print("No .env file found, using environment variables if available")

# Get API key from environment variable
api_key = os.getenv("FLOWHUNT_API_KEY")
if not api_key:
    print("Error: FLOWHUNT_API_KEY not found in environment variables or .env file")
    print("Please set the FLOWHUNT_API_KEY environment variable or add it to the .env file")
    sys.exit(1)

# FlowHunt flow ID for translation service
FLOW_ID = '023d4dee-b451-467f-a5cd-693e9f2aeac4'
WORKSPACE_ID = '93b15202-726d-4556-a3bf-c157338e6ff4'

# Map of folder names to full language names
LANGUAGE_MAP = {
    # ISO 639-1 language codes
    'af': 'Afrikaans',
    'ar': 'Arabic',
    'bg': 'Bulgarian',
    'bn': 'Bengali',
    'ca': 'Catalan',
    'cs': 'Czech',
    'da': 'Danish',
    'de': 'German',
    'el': 'Greek',
    'en': 'English',
    'es': 'Spanish',
    'et': 'Estonian',
    'fa': 'Persian',
    'fi': 'Finnish',
    'fr': 'French',
    'he': 'Hebrew',
    'hi': 'Hindi',
    'hr': 'Croatian',
    'hu': 'Hungarian',
    'id': 'Indonesian',
    'is': 'Icelandic',
    'it': 'Italian',
    'ja': 'Japanese',
    'ko': 'Korean',
    'lt': 'Lithuanian',
    'lv': 'Latvian',
    'ms': 'Malay',
    'nl': 'Dutch',
    'no': 'Norwegian',
    'pl': 'Polish',
    'pt': 'Portuguese',
    'ro': 'Romanian',
    'ru': 'Russian',
    'sk': 'Slovak',
    'sl': 'Slovenian',
    'sq': 'Albanian',
    'sr': 'Serbian',
    'sv': 'Swedish',
    'sw': 'Swahili',
    'ta': 'Tamil',
    'th': 'Thai',
    'tr': 'Turkish',
    'uk': 'Ukrainian',
    'ur': 'Urdu',
    'vi': 'Vietnamese',
    'zh': 'Chinese',
    'us': 'American English',
    
    # Country-specific language codes
    'pt-br': 'Brazilian Portuguese',
    'zh-cn': 'Simplified Chinese',
    'zh-tw': 'Traditional Chinese',
    'en-gb': 'British English',
    'en-us': 'American English',
    'es-mx': 'Mexican Spanish',
    
    # Special cases that might be confused
    'ch': 'Swiss German',  # Not Chinese, but Swiss domain/German dialect
    'cy': 'Welsh',  # Not Cypriot
    'gl': 'Galician',  # Not Greenlandic
    'mt': 'Maltese',  # Not Montenegrin
    'eu': 'Basque',  # Not European Union
}

def is_translatable_file(file_path):
    """Check if a file should be translated based on extension"""
    return file_path.suffix.lower() in ['.md', '.markdown', '.yaml', '.yml', '.html', '.txt']

def get_target_languages(content_dir):
    """
    Find all language directories in the content directory except 'en'
    
    Args:
        content_dir (Path): Path to the content directory
        
    Returns:
        list: List of target language directory names
    """
    target_langs = []
    
    for item in content_dir.iterdir():
        if item.is_dir() and item.name != "en":
            target_langs.append(item.name)
            
    return target_langs

def initialize_api_client():
    """Initialize and return a FlowHunt API client"""
    configuration = flowhunt.Configuration(
        host="https://api.flowhunt.io"
    )
    configuration.api_key['APIKeyHeader'] = api_key
    
    return flowhunt.ApiClient(configuration)

def invoke_flow_for_translation(api_instance, content, target_lang):
    """
    Invoke a FlowHunt flow to translate content to the target language
    
    Args:
        api_instance: FlowHunt API instance
        content (str): Content to translate
        target_lang (str): Target language code
        
    Returns:
        str: Process ID or None if failed
    """
    try:
        # Get the full language name from the map, fallback to the code if not found
        language_name = LANGUAGE_MAP.get(target_lang.lower(), target_lang)
        
        # Prepare the request payload
        flow_invoke_request = flowhunt.FlowInvokeRequest(
            variables={
                "target_language": language_name
            }, 
            human_input=content
        )
        
        # Invoke the flow
        response = api_instance.invoke_flow_singleton(
            flow_id=FLOW_ID,
            workspace_id=WORKSPACE_ID,
            flow_invoke_request=flow_invoke_request
        )
        
        # Return the process ID for checking status later
        return response.id
        
    except Exception as e:
        print(f"Error invoking flow for {target_lang}: {str(e)}")
        return None

def check_flow_results(api_instance, process_id):
    """
    Check if a flow has completed and get the results
    
    Args:
        api_instance: FlowHunt API instance
        process_id (str): Process ID to check
        
    Returns:
        tuple: (is_ready, result_text)
    """
    try:
        # Get the results of the invoked flow
        response = api_instance.get_invoked_flow_results(
            flow_id=FLOW_ID, task_id=process_id, workspace_id=WORKSPACE_ID
        )
        
        # Check if the flow has completed
        if response.status == "SUCCESS":
            # Extract the translated text from the response
            translated_text = json.loads(response.result)
            translated_text = translated_text['outputs'][0]['outputs'][0]['results']['message']['result']
            return True, translated_text
        else:
            # Flow is still processing
            return False, None
            
    except Exception as e:
        print(f"Error checking flow results for process {process_id}: {str(e)}")
        return False, None

def find_files_for_translation(content_dir, target_langs):
    """
    Find all files that need translation
    
    Args:
        content_dir (Path): Path to the content directory
        target_langs (list): List of target language codes
        
    Returns:
        list: List of tuples (file_path, content, target_lang, target_file)
    """
    en_dir = content_dir / "en"
    translation_tasks = []
    files_already_exist = 0
    
    # Find all translatable files in the English directory
    translatable_files = []
    for root, _, files in os.walk(en_dir):
        for file in files:
            file_path = Path(root) / file
            if is_translatable_file(file_path):
                translatable_files.append(file_path)
    
    print(f"Found {len(translatable_files)} translatable files in the English directory")
    
    if len(translatable_files) == 0:
        print("No translatable files found in the English directory")
        return [], 0
    
    # Create the list of translation tasks
    for file_path in translatable_files:
        # Read the content of the file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Get the relative path from the English directory
        rel_path = file_path.relative_to(en_dir)
        
        # For each target language, check if translation is needed
        for target_lang in target_langs:
            target_dir = content_dir / target_lang
            target_file = target_dir / rel_path
            
            # Skip if the target file already exists
            if target_file.exists():
                files_already_exist += 1
                continue
            
            # Add to translation tasks
            translation_tasks.append((file_path, content, target_lang, target_file))
    
    return translation_tasks, files_already_exist

def process_translations(translation_tasks):
    """
    Process translation tasks using FlowHunt API
    
    Args:
        translation_tasks (list): List of translation tasks
    """
    if not translation_tasks:
        print("No files need translation (all files already exist in target languages)")
        return
    
    print(f"Translating {len(translation_tasks)} files")
    max_concurrent=10
    check_interval=10
    # Initialize the API client
    with initialize_api_client() as api_client:
        api_instance = flowhunt.FlowsApi(api_client)
        
        # Dictionary to track tasks: {process_id: (file_path, target_lang, target_file)}
        pending_tasks = {}
        completed_tasks = []
        failed_tasks = []
        
        # Track progress
        progress_bar = tqdm(total=len(translation_tasks), desc="Scheduling translations")
        
        # Process tasks in batches respecting max_concurrent
        task_index = 0
        while task_index < len(translation_tasks) or pending_tasks:
            # Schedule new tasks up to max_concurrent
            while task_index < len(translation_tasks) and len(pending_tasks) < max_concurrent:
                file_path, content, target_lang, target_file = translation_tasks[task_index]
                
                # Invoke the translation flow
                process_id = invoke_flow_for_translation(api_instance, content, target_lang)
                
                if process_id:
                    # Add to pending tasks
                    pending_tasks[process_id] = (file_path, target_lang, target_file)
                else:
                    # Failed to invoke flow
                    failed_tasks.append((file_path, target_lang, target_file))
                    progress_bar.update(1)
                
                task_index += 1
            
            # Wait for the check interval before checking results
            if pending_tasks:
                print(f"Waiting for {check_interval} seconds before checking results...")
                time.sleep(check_interval)
            
            # Check for completed tasks
            process_ids = list(pending_tasks.keys())
            for process_id in process_ids:
                file_path, target_lang, target_file = pending_tasks[process_id]
                
                is_ready, translated_text = check_flow_results(api_instance, process_id)
                
                if is_ready:
                    # Remove from pending tasks
                    del pending_tasks[process_id]
                    
                    if translated_text:
                        try:
                            # Ensure the target directory exists
                            os.makedirs(target_file.parent, exist_ok=True)
                            
                            # Write the translated content to the target file
                            with open(target_file, 'w', encoding='utf-8') as f:
                                f.write(translated_text)
                            
                            # Add to completed tasks
                            completed_tasks.append((file_path, target_lang, target_file))
                            print(f"Translated: {target_file}")
                            
                        except Exception as e:
                            print(f"Error saving translation to {target_file}: {str(e)}")
                            failed_tasks.append((file_path, target_lang, target_file))
                    else:
                        # Translation failed
                        failed_tasks.append((file_path, target_lang, target_file))
                        print(f"Failed to translate {file_path} to {target_lang}")
                    
                    # Update progress
                    progress_bar.update(1)
            
            # If no more tasks to schedule and no pending tasks, we're done
            if task_index >= len(translation_tasks) and not pending_tasks:
                break
        
        # Close the progress bar
        progress_bar.close()
    
    # Print summary
    print("\nTranslation Summary:")
    print(f"Files translated successfully: {len(completed_tasks)}")
    print(f"Files failed: {len(failed_tasks)}")
    print(f"Total files processed: {len(completed_tasks) + len(failed_tasks)}")

def main():
    """Main function to parse arguments and process files"""
    parser = argparse.ArgumentParser(
        description="Translate missing files from English to other languages using FlowHunt API",
        epilog="""
Examples:
  python translate_with_flowhunt.py
  python translate_with_flowhunt.py --path /path/to/content
  python translate_with_flowhunt.py --check-interval 30
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    # Default path is ../content/ relative to the script location
    default_path = os.path.join(hugo_root, "content")
    
    parser.add_argument(
        "--path",
        help="Path to the content directory containing language subdirectories (default: %(default)s)",
        default=default_path
    )
    parser.add_argument(
        "--check-interval",
        help="Interval in seconds to check for completed translation tasks (default: %(default)s)",
        type=int,
        default=60
    )
    parser.add_argument(
        "--max-concurrent",
        help="Maximum number of concurrent translation tasks (default: %(default)s)",
        type=int,
        default=10
    )
    
    args = parser.parse_args()
    
    # Convert to Path object
    content_dir = Path(args.path)
    
    # Check if the content directory exists
    if not content_dir.exists() or not content_dir.is_dir():
        print(f"Error: Content directory not found: {content_dir}")
        sys.exit(1)
    
    # Check if the English directory exists
    en_dir = content_dir / "en"
    if not en_dir.exists() or not en_dir.is_dir():
        print(f"Error: English directory not found: {en_dir}")
        sys.exit(1)
    
    # Get target languages
    target_langs = get_target_languages(content_dir)
    
    if not target_langs:
        print("No target language directories found. Please create at least one target language directory.")
        sys.exit(1)
    
    print(f"Content directory: {content_dir}")
    print(f"Source language: en")
    print(f"Target languages: {', '.join(target_langs)}")
    
    # Find files that need translation
    translation_tasks, files_already_exist = find_files_for_translation(content_dir, target_langs)
    
    print(f"Found {len(translation_tasks)} files that need translation")
    print(f"Files skipped (already exist): {files_already_exist}")
    
    # Process translations
    process_translations(translation_tasks)
    
    print("\nTranslation completed!")

if __name__ == "__main__":
    main()