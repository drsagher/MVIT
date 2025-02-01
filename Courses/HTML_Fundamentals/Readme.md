# HTML Fundamentals

## Lesson 1 Introduction to HTML
HTML (HyperText Markup Language) is the foundational language used to create and structure content on the web. Here's a simple breakdown:

### 1. What Does HTML Do?
- Defines Structure: HTML organizes content like text, images, links, and forms into headings, paragraphs, lists, tables, and more.
- Creates Web Pages: Every webpage you visit is built with HTML even if other languages like CSS or JavaScript enhance it.
- Works with Browsers: Browsers (Chrome, Firefox, etc.) read HTML files and render them into the visual/functional pages you see.

### 2. Key Components of HTML
- Elements: Building blocks of HTML, defined by tags e.g. ```<h1>, <p>, <img>```
- Tags: Enclose content to give it meaning. Most have an opening <tag> and closing </tag> tag.
- Attributes: Provide extra info about elements (e.g., src for images, href for links)

```
<h1>This is a Heading</h1>
<p>This is a paragraph.</p>

<img src="image.jpg" alt="A description">
<a href="https://example.com">Visit Example</a>
```

### 3. HTML is NOT a Programming Language
- Markup, Not Logic: It defines what content is (e.g., a heading, button, or form), not how to perform calculations or logic.
- Static by Default: To add interactivity or dynamic behavior, you need languages like JavaScript.

### 4. How HTML Works with Other Technologies
- CSS: Styles HTML elements (colors, layouts, fonts).
- JavaScript: Adds interactivity (animations, form validation, etc.).
- HTML Alone: Creates static pages (content doesn’t change unless edited manually).

### 5. HTML5: The Modern Standard
HTML5 is the latest version, adding features like:
- Semantic tags ```<header>, <nav>, <article>```
- Multimedia support ```<video>, <audio>```
- Form enhancements (date pickers, input validation).

### 6. Why Learn HTML?
- Essential for Web Development: All websites use HTML.
- Easy to Start: Simple syntax, no complex tools needed.
- Foundation for Other Tools: Frameworks (React, Angular) and CMS platforms (WordPress) rely on HTML.

### Example of a Basic HTML Page
```
<!DOCTYPE html>
<html>
<head>
    <title>My First Page</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>Welcome to my website.</p>
    <img src="welcome.jpg" alt="Welcome image">
</body>
</html>
```

### Key Takeaways
- HTML is the skeleton of every webpage.
- It uses tags and attributes to define content structure.
- Combine it with CSS and JavaScript to create modern, interactive websites.

## History of HTML and its role in web development

HTML (HyperText Markup Language) was created in 1991 by Tim Berners-Lee, a British computer scientist, as part of his vision for the World Wide Web at CERN. Initially designed to share scientific documents, HTML provided a simple way to link text and resources across computers using hyperlinks, revolutionizing how information was accessed globally. The first version, HTML 1.0, laid the groundwork with basic tags for headings, paragraphs, and links. By 1995, HTML 2.0 standardized the language, but the late 1990s saw rapid evolution during the "browser wars" (Netscape vs. Internet Explorer), leading to fragmented features like proprietary tags. To restore order, the World Wide Web Consortium (W3C) took charge, releasing HTML 4.01 in 1999, which emphasized structure and accessibility. The early 2000s introduced XHTML, a stricter XML-based version, but developers craved flexibility, paving the way for HTML5 in 2014. HTML5 modernized the language with semantic tags ```<header>, <nav>```, native multimedia support ```<video>, <audio>``` and APIs for offline storage and geolocation, aligning it with the demands of dynamic, interactive web apps.


In web development, HTML serves as the structural backbone of every website, defining content hierarchy, embedding media, and enabling navigation. It works seamlessly with CSS (for styling) and JavaScript (for interactivity) to create rich user experiences. HTML’s role expanded with responsive design, ensuring sites adapt to mobile devices, and its semantic elements improved accessibility for screen readers and SEO. Today, HTML remains indispensable—even modern frameworks like React or Angular rely on it to render interfaces. By democratizing content creation and fostering global connectivity, HTML’s evolution mirrors the web’s growth from static pages to immersive platforms, cementing its place as the cornerstone of the digital age.

## How HTML works with CSS and JavaScript
HTML, CSS, and JavaScript work together to create functional, visually appealing, and interactive websites. HTML forms the structural foundation, defining elements like headings, paragraphs, images, and forms. It organizes content but lacks styling or dynamic behavior. CSS (Cascading Style Sheets) enhances HTML by adding visual design—controlling layouts, colors, fonts, and responsiveness. By targeting HTML elements via selectors, CSS transforms raw content into polished interfaces. JavaScript introduces interactivity, manipulating HTML and CSS in real-time. It responds to user actions (clicks, scrolls, form inputs), fetches data dynamically, and updates the DOM (Document Object Model), allowing pages to react without reloading. For example, HTML creates a button, CSS styles it, and JavaScript triggers an action when clicked. Together, they form a layered approach: HTML for content, CSS for presentation, and JavaScript for behavior, enabling modern, dynamic web experiences.

## Understanding browsers and rendering engines
Understanding browsers and rendering engines is key to grasping how web content becomes visible. Browsers like Chrome, Firefox, Safari, and Edge rely on rendering engines (e.g., Blink, Gecko, WebKit) to interpret HTML, CSS, and JavaScript, converting code into visual and interactive pages. The engine parses HTML to build the DOM (Document Object Model), processes CSS to create the CSSOM (CSS Object Model), and combines them into a render tree that calculates layout and paints pixels on the screen. Each engine handles rendering differently, which can lead to subtle cross-browser inconsistencies in how designs or features appear. Developers use browser developer tools (like Chrome DevTools) to inspect and debug this process, optimizing performance and ensuring compatibility. By understanding how engines prioritize tasks (like layout calculations or repaints), developers can write efficient code that speeds up page loads and enhances user experience. This knowledge bridges the gap between code and what users see, ensuring websites work seamlessly across devices and platforms.

