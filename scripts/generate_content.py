#!/usr/bin/env python3
"""
generate_content.py

This script generates content for each topic provided in an input file using FlowHunt API.

Usage:
    python generate_content.py --input_file topics.txt --flow_id FLOW_ID --output_dir generated_content

Prerequisites:
    - Python 3.6 or higher
    - FlowHunt API key (set in .env file or as environment variable FLOWHUNT_API_KEY)
    - Required packages: flowhunt, tqdm, python-dotenv

Examples:
    # Basic usage
    python generate_content.py --input_file topics.txt --flow_id "flow-id" --output_dir output
    python generate_content.py --input_file glossaries.txt --flow_id 8eeb2771-10c0-4165-a16b-37fe81707659 --output_dir ../../../content/en/glossary
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

# Load environment variables from .env file
script_dir = os.path.dirname(os.path.abspath(__file__))
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

def get_workspace_id():
    """Get the workspace ID from FlowHunt API"""
    api_client = initialize_api_client()
    api_instance = flowhunt.AuthApi(api_client)

    try:
        api_response = api_instance.get_user()
        return api_response.api_key_workspace_id
    except flowhunt.ApiException as e:
        print(f"Exception when calling AuthApi->get_user: {e}")
        return None

def initialize_api_client():
    """Initialize and return a FlowHunt API client"""
    configuration = flowhunt.Configuration(
        host="https://api.flowhunt.io"
    )
    configuration.api_key['APIKeyHeader'] = api_key
    return flowhunt.ApiClient(configuration)

def invoke_flow_for_content(api_instance, topic, flow_id, workspace_id):
    """
    Invoke a FlowHunt flow to generate content for a topic
    
    Args:
        api_instance: FlowHunt API instance
        topic (str): Topic to generate content for
        flow_id (str): FlowHunt flow ID
        workspace_id (str): FlowHunt workspace ID
        
    Returns:
        str: Process ID or None if failed
    """
    try:
        # Prepare the request payload
        flow_invoke_request = flowhunt.FlowInvokeRequest(
            variables={
                "today": time.strftime("%Y-%m-%d"),
            }, 
            human_input=topic
        )
        
        # Invoke the flow
        response = api_instance.invoke_flow_singleton(
            flow_id=flow_id,
            workspace_id=workspace_id,
            flow_invoke_request=flow_invoke_request
        )
        
        return response.id
        
    except Exception as e:
        print(f"Error invoking flow for topic '{topic}': {str(e)}")
        return None

def check_flow_results(api_instance, process_id, flow_id, workspace_id):
    """
    Check if a flow has completed and get the results
    
    Args:
        api_instance: FlowHunt API instance
        process_id (str): Process ID to check
        flow_id (str): FlowHunt flow ID
        workspace_id (str): FlowHunt workspace ID
        
    Returns:
        tuple: (is_ready, result_text)
    """
    try:
        response = api_instance.get_invoked_flow_results(
            flow_id=flow_id, task_id=process_id, workspace_id=workspace_id
        )
        
        if response.status == "SUCCESS":
            generated_content = json.loads(response.result)
            content = ""
            for output in generated_content['outputs'][0]['outputs']:
                part = output['results']['message']['result'].strip()
                if part.startswith("```"):
                    part = "\n".join(part.splitlines()[1:]).strip()
                if part.endswith("```"):
                    part = part[:-3].strip()
                content += part + "\n"
            content = content.strip()

            if not content:
                content = "NOCONTENT"

            return True, content.strip()
        else:
            return False, None
            
    except Exception as e:
        print(f"Error checking flow results for process {process_id}: {str(e)}")
        return False, None

def read_topics(input_file):
    """Read topics from input file"""
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"Error reading input file: {str(e)}")
        sys.exit(1)

def save_content(content, topic, output_dir):
    """Save generated content to a file"""
    try:
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Create a safe filename from the topic
        safe_filename = "".join(x for x in topic if x.isalnum() or x in (' ', '-', '_')).strip()[:50]
        safe_filename = safe_filename.replace(' ', '_') + '.md'
        
        output_path = os.path.join(output_dir, safe_filename)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        return output_path
    except Exception as e:
        print(f"Error saving content for topic '{topic}': {str(e)}")
        return None

def process_topics(topics, flow_id, workspace_id, output_dir):
    """Process topics using FlowHunt API"""
    if not topics:
        print("No topics to process")
        return
    
    print(f"Processing {len(topics)} topics")
    check_interval = 10
    
    with initialize_api_client() as api_client:
        api_instance = flowhunt.FlowsApi(api_client)
        
        # Dictionary to track tasks: {process_id: topic}
        pending_tasks = {}
        completed_tasks = []
        failed_tasks = []
        
        # Schedule all tasks
        progress_bar = tqdm(total=len(topics), desc="Scheduling content generation")
        
        for topic in topics:
            topic = topic.strip()
            if not topic:
                continue
            process_id = invoke_flow_for_content(api_instance, topic, flow_id, workspace_id)
            
            if process_id:
                pending_tasks[process_id] = topic
            else:
                failed_tasks.append(topic)
                progress_bar.update(1)
        
        progress_bar.close()
        print(f"Scheduled {len(pending_tasks)} tasks, now waiting for results...")
        
        # Process results
        progress_bar = tqdm(total=len(pending_tasks), desc="Processing content generation")
        
        while pending_tasks:
            time.sleep(check_interval)
            process_ids = list(pending_tasks.keys())
            completed_in_batch = 0
            
            for process_id in process_ids:
                topic = pending_tasks[process_id]
                is_ready, content = check_flow_results(api_instance, process_id, flow_id, workspace_id)
                
                if is_ready:
                    del pending_tasks[process_id]
                    completed_in_batch += 1
                    
                    if content:
                        output_path = save_content(content, topic, output_dir)
                        if output_path:
                            completed_tasks.append(topic)
                            print(f"\nGenerated content for '{topic}' saved to: {output_path}")
                        else:
                            failed_tasks.append(topic)
                    else:
                        failed_tasks.append(topic)
                        print(f"\nFailed to generate content for '{topic}'")
            
            progress_bar.update(completed_in_batch)
            
            if pending_tasks:
                print(f"\nStill waiting for {len(pending_tasks)} tasks to complete...")
        
        progress_bar.close()
    
    # Print summary
    print("\nContent Generation Summary:")
    print(f"Topics completed successfully: {len(completed_tasks)}")
    print(f"Topics failed: {len(failed_tasks)}")
    print(f"Total topics processed: {len(completed_tasks) + len(failed_tasks)}")

def main():
    """Main function to parse arguments and process topics"""
    parser = argparse.ArgumentParser(
        description="Generate content for topics using FlowHunt API",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        "--input_file",
        required=True,
        help="Path to input file containing topics (one per line)"
    )
    parser.add_argument(
        "--flow_id",
        required=True,
        help="FlowHunt flow ID for content generation"
    )
    parser.add_argument(
        "--output_dir",
        required=True,  
        help="Directory where generated content will be saved"
    )
    
    args = parser.parse_args()
    
    # Get workspace ID
    workspace_id = get_workspace_id()
    if not workspace_id:
        print("Error: Unable to retrieve workspace ID. Please check your API key.")
        sys.exit(1)
    
    print(f"Using workspace ID: {workspace_id}")
    
    # Read topics
    topics = read_topics(args.input_file)
    print(f"Found {len(topics)} topics in {args.input_file}")
    
    # Process topics
    process_topics(topics, args.flow_id, workspace_id, args.output_dir)
    
    print("\nContent generation completed!")

if __name__ == "__main__":
    main()