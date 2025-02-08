# Lesson 10 Accessibility

## What is Accessibility?
Accessibility refers to the design and development of products, services, and environments that are usable by people with disabilities, including visual, auditory, motor, or cognitive disabilities.

## Why is Accessibility Important?
Accessibility is essential for ensuring that people with disabilities have equal access to information, education, employment, and social opportunities. It also benefits older adults, people with temporary disabilities, and users with varying levels of digital literacy.

## Key Principles of Accessibility
1. Perceivable: Information and user interface components must be presentable to users in ways they can perceive.
2. Operable: User interface components and navigation must be operable by users.
3. Understandable: Information and user interface components must be understandable by users.
4. Robust: Content must be robust enough to be interpreted by a wide variety of user agents, including assistive technologies.

## Accessibility Guidelines
1. WCAG 2.1: The Web Content Accessibility Guidelines (WCAG) 2.1 provide a comprehensive set of guidelines for making web content more accessible.
2. Section 508: Section 508 of the Rehabilitation Act requires federal agencies to make their electronic and information technology accessible to people with disabilities.

## Accessibility Features
1. Alt Text: Providing alternative text for images to enable screen readers to describe the content.
2. Closed Captions: Providing closed captions for audio and video content to enable users to read the dialogue.
3. Keyboard Navigation: Enabling users to navigate and interact with content using only their keyboard.
4. High Contrast Mode: Providing a high contrast mode to enable users with visual impairments to read the content more easily.

## Testing for Accessibility
1. Manual Testing: Testing web content manually using assistive technologies like screen readers and keyboard-only navigation.
2. Automated Testing: Using automated testing tools to identify accessibility issues.
3. User Testing: Conducting user testing with participants with disabilities to identify accessibility issues.

## Writing accessible HTML: ARIA roles, alt text, semantic tags.

### ARIA Roles

ARIA (Accessible Rich Internet Applications) roles provide a way to make dynamic content and interactive elements accessible to screen readers and other assistive technologies. ARIA roles are used to define the role of an element, such as a button, menu, or tab.

- Examples of ARIA roles:
    - ```role="button"```: Defines an element as a button.
    - ```role="menu"```: Defines an element as a menu.
    - ```role="tab"```: Defines an element as a tab.

### Alt Text
Alt text (alternative text) is used to provide a text description of an image for screen readers and other assistive technologies. Alt text should be concise and descriptive, and should provide the same information as the image.
- Examples of alt text:
    - ```<img src="image.jpg" alt="A photo of a sunset">```
    - ```<img src="logo.png" alt="Company logo">```

### Semantic Tags
Semantic tags are HTML elements that provide meaning to the structure of a web page. Semantic tags help screen readers and other assistive technologies understand the structure and content of a web page.

- Examples of semantic tags:
    - ```<header>```: Defines the header section of a web page.
    - ```<nav>```: Defines the navigation section of a web page.
    - ```<main>```: Defines the main content section of a web page.
    - ```<section>```: Defines a section of a web page.
    - ```<article>```: Defines an article or blog post.
    - ```<aside>```: Defines a section of a web page that is related to the main content.

### Best Practices
1. Use ARIA roles to define the role of dynamic content and interactive elements.
2. Use alt text to provide a text description of images.
3. Use semantic tags to provide meaning to the structure of a web page.
4. Use clear and concise language in alt text and semantic tags.
5. Test web pages with screen readers and other assistive technologies to ensure accessibility.

## Keyboard navigation and screen reader compatibility
### Keyboard Navigation
Keyboard navigation refers to the ability to navigate and interact with a website or application using only a keyboard. This is essential for users who cannot use a mouse or other pointing device.

### Best Practices for Keyboard Navigation
1. Provide a logical tab order: Ensure that the tab order follows a logical sequence, such as from top to bottom and left to right.
2. Use ARIA attributes: Use ARIA attributes, such as role and aria-label, to provide a clear and consistent navigation experience.
3. Make interactive elements keyboard-accessible: Ensure that all interactive elements, such as buttons and links, can be accessed and activated using the keyboard.
4. Provide a way to skip navigation: Provide a way for users to skip navigation, such as a "Skip to main content" link.

### Screen Reader Compatibility
Screen readers are software programs that read aloud the text on a website or application. This is essential for users who are blind or have low vision.

### Best Practices for Screen Reader Compatibility
1. Use semantic HTML: Use semantic HTML elements, such as header, nav, and main, to provide a clear and consistent structure.
2. Provide alternative text for images: Provide alternative text for images, using the alt attribute.
3. Use ARIA attributes: Use ARIA attributes, such as role and aria-label, to provide a clear and consistent navigation experience.
4. Test with screen readers: Test your website or application with popular screen readers, such as JAWS and VoiceOver.

### Testing Tools
1. Keyboard-only navigation: Test your website or application using only a keyboard.
2. Screen readers: Test your website or application with popular screen readers, such as JAWS and VoiceOver.
3. Accessibility audit tools: Use accessibility audit tools, such as WAVE and Lighthouse, to identify accessibility issues.

## Accessibility

| Accessibility Feature | Description | Tags | Code Example |
| --- | --- | --- | --- |
| Alt Text | Provides alternative text for images | ```alt``` | ```<img src="image.jpg" alt="A photo of a sunset">``` |
| Semantic HTML | Uses HTML elements to define structure | ```header```, ```nav```, ```main``` | ```<header>Header content</header>``` |
| ARIA Roles | Defines roles for dynamic content and interactive elements | ```role``` | ```<button role="button">Click me</button>``` |
| Keyboard Navigation | Enables navigation using only a keyboard | ```tabindex``` | ```<a href="#" tabindex="1">Link</a>``` |
| Screen Reader Compatibility | Enables screen readers to read content | ```aria-label``` | ```<button aria-label="Submit form">Submit</button>``` |
| High Contrast Mode | Enables high contrast mode for visually impaired users | ```highcontrast``` | ```<button class="highcontrast">High contrast mode</button>``` |
| Closed Captions | Provides closed captions for audio and video content | ```track``` | ```<video><track src="captions.vtt" kind="captions" srclang="en" label="English"></video>``` |


## Resources
1. W3C Web Accessibility Initiative: The W3C Web Accessibility Initiative provides a comprehensive set of resources and guidelines for making web content more accessible.
2. Accessibility Guidelines: The Accessibility Guidelines provide a comprehensive set of guidelines for making web content more accessible.
3. A11y Project: The A11y Project provides a comprehensive set of resources and guidelines for making web content more accessible.
