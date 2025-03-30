---
title: "Test Page for Partials"
---

This is a test page to demonstrate all available shortcodes in the Hugo boilerplate theme. Each section below shows how to use a specific shortcode and how it appears to users.

## Lazy Loading Components

### Lazy-loaded YouTube Video

Below is a lazy-loaded YouTube video to test the video lazy loading functionality:

{{< lazyvideo "8kGxHHhYRmE" "Beautiful Nature Video - Relaxing Music with Nature Sounds" >}}

The video above should only load when it comes into view, improving page performance.

### Lazy-loaded Image

{{< lazyimg "https://images.unsplash.com/photo-1682687982501-1e58ab814714" "Example of a lazy-loaded image" >}}

### Lazy-loaded SVG

{{< lazysvg "/images/example.svg" "Example of a lazy-loaded SVG" >}}

### Picture Element

{{< picture "/images/example.jpg" "Example of a responsive picture element" >}}

## Banner Components

### Banner with Button

{{< banner-with-button 
    title="New Feature Available" 
    message="Try our new dashboard experience with improved analytics." 
    buttonText="Try it now" 
    buttonUrl="#" 
    dismissable=true 
>}}

### Banner on Dark Background

{{< banner-on-dark 
    message="Black Friday Sale: Get 50% off all plans until November 30th" 
    url="#" 
    dismissable=true 
>}}

### Banner on Brand Color

{{< banner-on-brand 
    message="Join our webinar on product updates this Friday" 
    url="#" 
    dismissable=true 
>}}

### Banner with Background Glow

{{< banner-with-background-glow 
    message="Our new mobile app is now available for download" 
    url="#" 
    dismissable=true 
>}}

### Bottom Aligned Banner

{{< banner-bottom-aligned 
    message="This site uses cookies to improve your experience" 
    url="#" 
    dismissable=true 
>}}

### Floating Banner at Bottom

{{< banner-floating-at-bottom 
    message="Limited time offer: Free shipping on all orders" 
    url="#" 
    dismissable=true 
>}}

### Centered Floating Banner

{{< banner-floating-at-bottom-centered 
    message="New blog post: 10 tips for better productivity" 
    url="#" 
    dismissable=true 
>}}

### Privacy Notice (Left Aligned)

{{< banner-privacy-notice-left-aligned 
    message="We use cookies to enhance your browsing experience, serve personalized ads or content, and analyze our traffic." 
    policyUrl="#" 
    acceptText="Accept all" 
    rejectText="Reject all" 
>}}

### Privacy Notice (Centered)

{{< banner-privacy-notice-centered 
    message="We use cookies to enhance your browsing experience, serve personalized ads or content, and analyze our traffic." 
    policyUrl="#" 
    acceptText="Accept all" 
    rejectText="Reject all" 
>}}

### Privacy Notice (Full Width)

{{< banner-privacy-notice-full-width 
    message="We use cookies to enhance your browsing experience, serve personalized ads or content, and analyze our traffic." 
    policyUrl="#" 
    acceptText="Accept all" 
    rejectText="Reject all" 
>}}

## Category Components

### Preview Three Column with Description

{{< categories-preview-three-column-with-description 
    heading="Shop by Collection" 
    description="Each season, we collaborate with world-class designers to create a collection inspired by the natural world." 
    backgroundColor="bg-white" 
>}}

### Preview Three Column

{{< categories-preview-three-column 
    heading="Shop by Category" 
    backgroundColor="bg-gray-100" 
>}}

### Preview with Image Backgrounds

{{< categories-preview-with-image-backgrounds 
    heading="Shop by Style" 
    browseAllText="Browse all styles" 
    browseAllUrl="#" 
    backgroundColor="bg-white" 
>}}

### Preview with Scrolling Cards

{{< categories-preview-with-scrolling-cards 
    heading="Browse Categories" 
    browseAllText="View all categories" 
    browseAllUrl="#" 
    backgroundColor="bg-gray-100" 
>}}

### Product List Card with Full Details

{{< categories-product-list-card-with-full-details 
    heading="Featured Products" 
    backgroundColor="bg-white" 
>}}

### Product List with Image Overlay and Add Button

{{< categories-product-list-with-image-overlay-and-add-button 
    heading="New Arrivals" 
    buttonText="Add to bag" 
    backgroundColor="bg-gray-100" 
>}}

### Product List with Inline Price and CTA Link

{{< categories-product-list-with-inline-price-and-cta-link 
    heading="Recommended Products" 
    viewAllText="View all products" 
    viewAllUrl="#" 
    ctaText="View details" 
    backgroundColor="bg-white" 
>}}

### Product List with Tall Images

{{< categories-product-list-with-tall-images 
    heading="Trending Now" 
    backgroundColor="bg-gray-100" 
>}}

## Content Components

### Centered Content

{{< content-centered 
    heading="About Our Company" 
    backgroundColor="bg-white" 
>}}

### Split Content with Image

{{< content-split-with-image 
    heading="Our Mission" 
    imageUrl="https://images.unsplash.com/photo-1551434678-e076c223a692" 
    imageAlt="Team working together" 
    backgroundColor="bg-gray-100" 
>}}

## Call to Action Components

### Dark Panel CTA

{{< cta-dark-panel 
    heading="Ready to get started?" 
    description="Get in touch or create an account." 
    primaryButtonText="Contact sales" 
    primaryButtonUrl="#" 
    secondaryButtonText="Create account" 
    secondaryButtonUrl="#" 
>}}

### Simple Centered CTA

{{< cta-simple-centered 
    heading="Boost your productivity" 
    description="Start using our app today." 
    buttonText="Get started" 
    buttonUrl="#" 
    backgroundColor="bg-white" 
>}}

### Simple Justified CTA

{{< cta-simple-justified 
    heading="Ready to dive in?" 
    description="Start your free trial today." 
    buttonText="Sign up for free" 
    buttonUrl="#" 
    backgroundColor="bg-gray-100" 
>}}

## FAQ Components

### Centered Accordion FAQ

{{< faq-centered-accordion 
    heading="Frequently asked questions" 
    backgroundColor="bg-white" 
>}}

## Feature Components

### Three Column Features

{{< features-three-column 
    heading="Features" 
    description="Our application provides a complete solution for managing your business needs." 
    backgroundColor="bg-gray-100" 
>}}

### Features with 4 Images Grid

{{< features-with-4-images-grid 
    heading="Technical Specifications" 
    description="The following specifications make this product stand out from the competition." 
    backgroundColor="bg-white" 
>}}

### Features with Alternating Sections

{{< features-with-alternating-sections 
    heading="Key Features" 
    description="Our product is designed to solve your everyday problems." 
    backgroundColor="bg-gray-100" 
>}}

### Features with Fading Image

{{< features-with-fading-image 
    heading="Product Specifications" 
    description="Everything you need to know about our product." 
    backgroundColor="bg-white" 
>}}

### Features with Header, Images, and Descriptions

{{< features-with-header-images-and-descriptions 
    heading="How It Works" 
    description="Our simple process from start to finish." 
    backgroundColor="bg-gray-100" 
>}}

### Features with Intro and Tabs

{{< features-with-intro-and-tabs 
    heading="Product Features" 
    description="Explore the different aspects of our product." 
    backgroundColor="bg-white" 
>}}

### Features with Split Image

{{< features-with-split-image 
    subheading="Designed for business" 
    heading="The right features for your business" 
    description="Our product is designed to address the specific needs of modern businesses." 
    backgroundColor="bg-gray-100" 
>}}

### Features with Square Images

{{< features-with-square-images 
    subheading="Why choose us" 
    heading="Features that set us apart" 
    description="Our product includes everything you need to get started quickly." 
    backgroundColor="bg-white" 
>}}

### Features with Tiered Images

{{< features-with-tiered-images 
    subheading="Powerful features" 
    heading="Everything you need to succeed" 
    backgroundColor="bg-gray-100" 
>}}

### Features with Wide Images

{{< features-with-wide-images 
    subheading="Intuitive interface" 
    heading="Designed for productivity" 
    description="Our clean interface helps you focus on what matters." 
    backgroundColor="bg-white" 
>}}

## Footer Components

### Four Column Footer

{{< footer-four-column 
    backgroundColor="bg-gray-900" 
>}}

### Simple Centered Footer

{{< footer-simple-centered 
    backgroundColor="bg-gray-900" 
>}}

## Header Components

### Centered Header

{{< header-centered 
    heading="Welcome to our website" 
    description="Discover our products and services." 
    backgroundColor="bg-white" 
>}}

### Simple Header

{{< header-simple 
    heading="About Us" 
    description="Learn more about our company and mission." 
    backgroundColor="bg-gray-100" 
>}}

## Hero Components

### Simple Centered Hero

{{< hero-simple-centered 
    heading="Next generation platform" 
    description="Anim aute id magna aliqua ad ad non deserunt sunt. Qui irure qui lorem cupidatat commodo." 
    primaryButtonText="Get started" 
    primaryButtonUrl="#" 
    secondaryButtonText="Learn more" 
    secondaryButtonUrl="#" 
    backgroundColor="bg-white" 
>}}

### Split Hero with Code

{{< hero-split-with-code 
    heading="Develop with confidence" 
    description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua." 
    buttonText="Get started" 
    buttonUrl="#" 
    codeLanguage="javascript" 
    codeContent="// Example code\nfunction example() {\n  console.log('Hello world!');\n}" 
    backgroundColor="bg-gray-100" 
>}}

### Split Hero with Image Tiles

{{< hero-split-with-image-tiles 
    heading="Design your next project" 
    description="Create beautiful designs with our easy-to-use platform." 
    buttonText="Start designing" 
    buttonUrl="#" 
    backgroundColor="bg-white" 
>}}

### Split Hero with Image

{{< hero-split-with-image 
    heading="Data-driven insights" 
    description="Turn your data into actionable insights with our analytics platform." 
    buttonText="Learn more" 
    buttonUrl="#" 
    imageUrl="https://images.unsplash.com/photo-1551434678-e076c223a692" 
    imageAlt="Dashboard analytics" 
    backgroundColor="bg-gray-100" 
>}}

### Split Hero with Screenshot

{{< hero-split-with-screenshot 
    heading="Streamline your workflow" 
    description="Our platform helps you manage your projects more efficiently." 
    buttonText="Get started" 
    buttonUrl="#" 
    imageUrl="https://images.unsplash.com/photo-1551434678-e076c223a692" 
    imageAlt="Application screenshot" 
    backgroundColor="bg-white" 
>}}

## Incentives Components

### 2x2 Grid with Illustrations

{{< incentives-2x2-grid-with-illustrations 
    heading="Why choose us" 
    backgroundColor="bg-gray-100" 
>}}

### 3 Column with Illustrations and Header

{{< incentives-3-column-with-illustrations-and-header 
    heading="Our advantages" 
    description="We provide the best service in the industry with these key benefits." 
    backgroundColor="bg-white" 
>}}

### 3 Column with Illustrations and Heading

{{< incentives-3-column-with-illustrations-and-heading 
    heading="Our guarantees" 
    backgroundColor="bg-gray-100" 
>}}

### 3 Column with Illustrations and Split Header

{{< incentives-3-column-with-illustrations-and-split-header 
    heading="Why customers love us" 
    description="We've helped thousands of companies achieve their goals." 
    backgroundColor="bg-white" 
>}}

### 4 Column with Illustrations

{{< incentives-4-column-with-illustrations 
    backgroundColor="bg-gray-100" 
>}}

## Menu Components

### Flyout Full Width Two Columns

{{< menu-flyout-full-width-two-columns 
    buttonText="Solutions" 
>}}

### Flyout Full Width

{{< menu-flyout-full-width 
    buttonText="Products" 
>}}

### Flyout Simple with Descriptions

{{< menu-flyout-simple-with-descriptions 
    buttonText="Resources" 
>}}

### Flyout Stacked with Footer Actions

{{< menu-flyout-stacked-with-footer-actions 
    buttonText="Features" 
>}}

### Flyout Two Column

{{< menu-flyout-two-column 
    buttonText="Company" 
>}}

### Header Menu

{{< menu-header >}}

## Pricing Components

### Three Tiers Pricing

{{< pricing-three-tiers 
    heading="Pricing plans" 
    description="Choose the plan that's right for you." 
    backgroundColor="bg-white" 
>}}

## Product Components

### Split with Image

{{< products-split-with-image 
    backgroundColor="bg-gray-100" 
>}}

### With Image Gallery and Expandable Details

{{< products-with-image-gallery-and-expandable-details 
    backgroundColor="bg-white" 
>}}

### With Image Grid

{{< products-with-image-grid 
    backgroundColor="bg-gray-100" 
>}}

### With Tabs

{{< products-with-tabs 
    backgroundColor="bg-white" 
>}}

### With Tiered Images

{{< products-with-tiered-images 
    backgroundColor="bg-gray-100" 
>}}

## Reviews Components

### Simple with Avatars

{{< reviews-simple-with-avatars 
    heading="Customer Reviews" 
    backgroundColor="bg-white" 
>}}

### With Summary Chart

{{< reviews-with-summary-chart 
    heading="Customer Feedback" 
    backgroundColor="bg-gray-100" 
>}}

## Stats Components

### Simple Grid Stats

{{< stats-simple-grid 
    heading="Trusted by companies worldwide" 
    description="We've helped thousands of companies achieve their goals." 
    backgroundColor="bg-white" 
>}}

## Team Components

### Grid with Round Images

{{< team-grid-round-images 
    heading="Our Team" 
    description="Meet the people behind our company." 
    backgroundColor="bg-gray-100" 
>}}

## Testimonial Components

### Grid Testimonials

{{< testimonial-grid 
    heading="What our customers are saying" 
    backgroundColor="bg-white" 
>}}

### Simple Centered Testimonial

{{< testimonial-simple-centered 
    backgroundColor="bg-gray-100" 
>}}

## Layout Components

### Bento Grid Three Column

{{< bentogrid-three-column 
    backgroundColor="bg-white" 
>}}

### Bento Grid Two Row

{{< bentogrid-two-row 
    backgroundColor="bg-gray-100" 
>}}

## Logos Components

### Simple Logos

{{< logos-simple 
    heading="Trusted by these companies" 
    backgroundColor="bg-white" 
>}}

### Logos with Heading

{{< logos-with-heading 
    heading="Our Partners" 
    description="We work with the best companies in the industry." 
    backgroundColor="bg-gray-100" 
>}}
