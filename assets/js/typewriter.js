/**
 * Typewriter Effect Component
 * Creates a typewriter animation effect for the last N words in a heading
 */
class TypewriterEffect {
  constructor(element, options = {}) {
    this.element = element;
    this.options = {
      words: options.words || 1,
      typingSpeed: options.typingSpeed || 100,
      deletingSpeed: options.deletingSpeed || 50,
      pauseDuration: options.pauseDuration || 2000,
      color: options.color || 'text-indigo-600',
      ...options
    };
    
    this.originalText = this.element.textContent.trim();
    this.textToAnimate = '';
    this.staticText = '';
    this.currentCharIndex = 0;
    this.isDeleting = false;
    this.typewriterContainer = null;
    this.typewriterText = null;
    this.cursor = null;
    
    this.init();
  }
  
  init() {
    this.parseText();
    this.createTypewriterElements();
    this.startAnimation();
  }
  
  parseText() {
    const words = this.originalText.split(' ');
    const wordsToAnimateCount = Math.min(this.options.words, words.length);
    
    // Join the words to animate as a single text string
    const wordsToAnimateArray = words.slice(-wordsToAnimateCount);
    this.textToAnimate = wordsToAnimateArray.join(' ');
    this.staticText = words.slice(0, -wordsToAnimateCount).join(' ');
    
    // Add space after static text if it exists
    if (this.staticText && this.textToAnimate.length > 0) {
      this.staticText += ' ';
    }
  }
  
  createTypewriterElements() {
    // Create container for typewriter effect
    this.typewriterContainer = document.createElement('span');
    this.typewriterContainer.className = 'typewriter-container';
    
    // Create text element
    this.typewriterText = document.createElement('span');
    this.typewriterText.className = `typewriter-text ${this.options.color}`;
    
    // Create cursor element
    this.cursor = document.createElement('span');
    this.cursor.className = `typewriter-cursor ${this.options.color}`;
    this.cursor.textContent = '_';
    
    // Append elements
    this.typewriterContainer.appendChild(this.typewriterText);
    this.typewriterContainer.appendChild(this.cursor);
    
    // Replace original element content
    this.element.innerHTML = '';
    if (this.staticText) {
      this.element.appendChild(document.createTextNode(this.staticText));
    }
    this.element.appendChild(this.typewriterContainer);
    
    // Pre-render all possible words to calculate max width
    this.calculateMaxWidth();
  }
  
  calculateMaxWidth() {
    // Test the full text to animate to find its width
    this.typewriterText.textContent = this.textToAnimate;
    const rect = this.typewriterText.getBoundingClientRect();
    const maxWidth = rect.width;
    
    // Set minimum width to prevent jumping
    this.typewriterContainer.style.minWidth = Math.ceil(maxWidth + 20) + 'px';
    
    // Clear text content for animation
    this.typewriterText.textContent = '';
  }
  
  startAnimation() {
    if (this.textToAnimate.length === 0) return;
    
    this.animateText();
  }
  
  animateText() {
    if (this.isDeleting) {
      // Deleting animation
      this.typewriterText.textContent = this.textToAnimate.substring(0, this.currentCharIndex);
      this.currentCharIndex--;
      
      if (this.currentCharIndex < 0) {
        this.isDeleting = false;
        this.currentCharIndex = 0;
        
        // Pause before typing again
        setTimeout(() => this.animateText(), this.options.pauseDuration / 2);
        return;
      }
      
      setTimeout(() => this.animateText(), this.options.deletingSpeed);
    } else {
      // Typing animation
      this.cursor.classList.add('typing');
      this.typewriterText.textContent = this.textToAnimate.substring(0, this.currentCharIndex + 1);
      this.currentCharIndex++;
      
      if (this.currentCharIndex >= this.textToAnimate.length) {
        this.cursor.classList.remove('typing');
        this.isDeleting = true;
        
        // Pause before deleting
        setTimeout(() => this.animateText(), this.options.pauseDuration);
        return;
      }
      
      setTimeout(() => this.animateText(), this.options.typingSpeed);
    }
  }
  
  destroy() {
    // Restore original text
    this.element.textContent = this.originalText;
  }
}

// Auto-initialize typewriter effects
document.addEventListener('DOMContentLoaded', function() {
  const typewriterElements = document.querySelectorAll('[data-typewriter]');
  
  typewriterElements.forEach(element => {
    const options = {
      words: parseInt(element.dataset.typewriterWords) || 1,
      typingSpeed: parseInt(element.dataset.typewriterSpeed) || 100,
      deletingSpeed: parseInt(element.dataset.typewriterDeleteSpeed) || 50,
      pauseDuration: parseInt(element.dataset.typewriterPause) || 2000,
      color: element.dataset.typewriterColor || 'text-indigo-600'
    };
    
    new TypewriterEffect(element, options);
  });
});

export { TypewriterEffect };
