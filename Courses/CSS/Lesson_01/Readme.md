# Lesson 01 Introduction to CSS
Cascading Style Sheets (CSS) is a fundamental language used to control the visual styling and layout of web pages. CSS works in tandem with HTML, allowing developers to separate presentation from structure and create visually appealing, user-friendly, and responsive websites. With CSS, you can manipulate elements such as colors, fonts, spacing, and positioning, as well as create complex layouts, animations, and effects. Whether you're building a simple blog or a complex web application, CSS is an essential tool for bringing your vision to life and creating a seamless user experience.

## What is CSS?
CSS (Cascading Style Sheets) is a stylesheet language used to describe the presentation of a document written in HTML (or XML). It controls how web pages look by defining styles for elements like layout, colors, fonts, spacing, animations, and responsiveness. CSS works alongside HTML (which structures content) and JavaScript (which adds interactivity) to create modern, visually appealing websites.

## Role of CSS in Web Development
Separation of Concerns: CSS separates content (HTML) from design (styling), making code cleaner, more maintainable, and easier to update.

### Visual Styling
Defines the appearance of elements:
- Layout: Positioning, grids, Flexbox, and alignment.
- Typography: Fonts, sizes, line heights, and text effects.
- Colors & Backgrounds: Gradients, images, and opacity.
- Responsiveness: Adapts designs to different screen sizes (e.g., mobile, tablet, desktop).

### Enhanced User Experience
- Creates engaging interfaces with animations, transitions, and hover effects.
- Improves accessibility through readable contrast ratios and scalable text.

### Consistency
- Ensures a uniform look across multiple pages using external stylesheets or CSS variables.

### Performance Optimization
- Modern CSS techniques (e.g., flex, grid) reduce reliance on complex JavaScript or image-based layouts.
- Minification and critical CSS improve page load times.

### Cross-Browser Compatibility
Tools like autoprefixer and CSS resets (e.g., Normalize.css) ensure consistent rendering across browsers.

### Integration with Modern Tools
Works with preprocessors (Sass), frameworks (Bootstrap), and JavaScript libraries (React) to streamline development.

```
<!-- HTML --> 
<h1 class="title">Hello, World!</h1> 
```
```
/* CSS */ 
.title { 
  color: #2ecc71; 
  font-family: Arial; 
  text-align: center; 
  text-shadow: 2px 2px 4px rgba(0,0,0,0.3); 
}
```
Without CSS, websites would look like plain text documents (see "browser default styles"). CSS is the design layer of the web, making it indispensable for front-end developers and designers! 

## Inline, internal, and external CSS
