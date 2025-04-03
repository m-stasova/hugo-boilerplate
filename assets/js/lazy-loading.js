// Lazy loading implementation for images, videos, and SVGs
document.addEventListener('DOMContentLoaded', function() {
  // Debug function to log image loading
  function logImageLoading(message, element) {
    console.log(`[Lazy Loading] ${message}`, element);
  }

  // Debug function to show which images are being loaded
  function debugResponsiveImages() {
    const pictures = document.querySelectorAll('picture');
    pictures.forEach(function(picture) {
      const img = picture.querySelector('img');
      const sources = picture.querySelectorAll('source');
      
      if (img) {
        console.log('Image src:', img.currentSrc);
        console.log('Window width:', window.innerWidth);
        console.log('Available sources:');
        sources.forEach(source => {
          console.log('- Type:', source.type);
          console.log('  Srcset:', source.srcset);
          console.log('  Sizes:', source.sizes);
        });
      }
    });
  }

  // Initialize lazy SVGs
  function initLazySVGs() {
    const lazySVGs = document.querySelectorAll('object.lazy-svg');
    
    if ('IntersectionObserver' in window) {
      const svgObserver = new IntersectionObserver(function(entries, observer) {
        entries.forEach(function(entry) {
          if (entry.isIntersecting) {
            const svg = entry.target;
            if (svg.dataset.src) {
              svg.data = svg.dataset.src;
              
              // Add onload event to add the 'loaded' class
              svg.onload = function() {
                svg.classList.add('loaded');
              };
            }
            
            svgObserver.unobserve(svg);
          }
        });
      });
      
      lazySVGs.forEach(function(svg) {
        svgObserver.observe(svg);
      });
    } else {
      // Fallback for browsers that don't support IntersectionObserver
      let lazySVGTimeout;
      
      function lazyLoadSVGs() {
        if (lazySVGTimeout) {
          clearTimeout(lazySVGTimeout);
        }
        
        lazySVGTimeout = setTimeout(function() {
          const scrollTop = window.pageYOffset;
          
          lazySVGs.forEach(function(svg) {
            if (svg.offsetTop < (window.innerHeight + scrollTop)) {
              if (svg.dataset.src) {
                svg.data = svg.dataset.src;
                
                // Add onload event to add the 'loaded' class
                svg.onload = function() {
                  svg.classList.add('loaded');
                };
              }
            }
          });
          
          if (lazySVGs.length === 0) {
            document.removeEventListener('scroll', lazyLoadSVGs);
            window.removeEventListener('resize', lazyLoadSVGs);
            window.removeEventListener('orientationChange', lazyLoadSVGs);
          }
        }, 20);
      }
      
      document.addEventListener('scroll', lazyLoadSVGs);
      window.addEventListener('resize', lazyLoadSVGs);
      window.addEventListener('orientationChange', lazyLoadSVGs);
      
      // Initial load
      lazyLoadSVGs();
    }
  }
  
  // Add loaded class to all images when they finish loading
  function initImageLoadedClass() {
    const lazyImages = document.querySelectorAll('img.lazy-image');
    const lazyPictures = document.querySelectorAll('picture.lazy-picture');
    
    logImageLoading(`Found ${lazyImages.length} lazy images and ${lazyPictures.length} lazy pictures`);
    
    // Add loaded class to images when they finish loading
    lazyImages.forEach(function(image) {
      // If the image is already loaded
      if (image.complete) {
        logImageLoading('Image already loaded', image);
        image.classList.add('loaded');
        
        // Find parent picture element and add loaded class
        const picture = image.closest('picture');
        if (picture) {
          picture.classList.add('loaded');
        }
      } else {
        // Add load event listener
        image.addEventListener('load', function() {
          logImageLoading('Image loaded', image);
          image.classList.add('loaded');
          
          // Find parent picture element and add loaded class
          const picture = image.closest('picture');
          if (picture) {
            picture.classList.add('loaded');
          }
        });
      }
    });
  }
  
  // Initialize lazy loading
  initLazySVGs();
  initImageLoadedClass();
  
  // Run debug function after a short delay to allow images to load
  setTimeout(debugResponsiveImages, 1000);
  
  // Add a window resize event to dynamically update image sizes
  window.addEventListener('resize', function() {
    // The browser will automatically handle responsive images with srcset
    logImageLoading('Window resized, browser will automatically select appropriate image size');
    
    // Run debug function after resize
    setTimeout(debugResponsiveImages, 500);
  });
});
