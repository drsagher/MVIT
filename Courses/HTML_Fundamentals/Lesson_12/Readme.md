# Lesson 12 Best Practices

## Common Mistakes to Avoid in HTML
### 1. Missing or mismatched tags
- Make sure to close all tags, and that the closing tag matches the opening tag.
- Example: ```<p>This is a paragraph</p>``` instead of ```<p>```This is a paragraph>

### 2. Incorrect nesting of tags
- Make sure to nest tags correctly, with the innermost tag closing first.
- Example: ```<p><strong>This text is strong</strong></p>``` instead of ```<p><strong>This text is strong</p></strong>```

### 3. Forgetting to include alt text for images
- Make sure to include alt text for all images, to provide a description for screen readers and search engines.
- Example: ```<img src="image.jpg" alt="A description of the image"```>

### 4. Not specifying character encoding
- Make sure to specify the character encoding of your HTML document, to ensure that special characters are displayed correctly.
- Example: ```<meta charset="UTF-8">```

### 5. Not using semantic HTML
- Make sure to use semantic HTML elements, such as ```<header>```, ```<nav>```, ```<main>```, ```<section>```, ```<article>```, ```<aside>```, ```<footer>```, to provide meaning to the structure of your HTML document.
- Example: ```<header><h1>Page Title</h1></header>``` instead of ```<div><h1>Page Title</h1></div>```

### 6. Not testing for accessibility
- Make sure to test your HTML document for accessibility, to ensure that it can be used by people with disabilities.
- Example: Use the WAVE Web Accessibility Evaluation Tool to test your HTML document.

### 7. Not validating HTML
- Make sure to validate your HTML document, to ensure that it is free of errors and conforms to the HTML specification.
- Example: Use the W3C Markup Validation Service to validate your HTML document.

### 8. Not using ARIA attributes
- Make sure to use ARIA attributes, such as role, aria-label, aria-describedby, to provide a way for screen readers to understand the structure and content of your HTML document.
- Example: ```<button role="button" aria-label="Click me">Click me</button>```

### 9. Not providing a fallback for JavaScript
- Make sure to provide a fallback for JavaScript, to ensure that your HTML document can still be used if JavaScript is disabled or not supported.
- Example: ```<noscript><p>This page requires JavaScript to be enabled.</p></noscript>```

### 10. Not keeping HTML up to date
- Make sure to keep your HTML up to date, to ensure that it conforms to the latest HTML specification and takes advantage of new features and improvements.
- Example: Use the latest version of the HTML specification, and take advantage of new features such as HTML5 semantic elements.

