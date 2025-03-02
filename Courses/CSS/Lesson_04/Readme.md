# Lesson 04 Display property: ```block```, ```inline```, ```inline-block```
Mastering the CSS display property is essential for building visually appealing and responsive web pages. The display property determines how an element is displayed and laid out on a web page, with three fundamental values: block, inline, and inline-block. Block elements, such as divs and paragraphs, occupy the full width of their parent container and start on a new line. Inline elements, like spans and anchors, sit alongside other elements on the same line. Inline-block elements, meanwhile, combine the characteristics of both, allowing for precise control over layout and design. Understanding the nuances of these display properties is crucial for creating flexible, responsive, and maintainable CSS layouts.

## 1. Core Concepts

### Block Elements
#### Characteristics:

- Starts on a new line
- Takes full available width
- Respects width/height properties
- Margin/padding push other elements away
- **Default Elements**: ```<div>```, ```<h1>-<h6>```, ```<p>```, ```<section>```
- **CSS**: ```display: block```;

### Inline Elements

#### Characteristics:

- Flows within text/content
- Only takes needed space
- Ignores width/height
- Vertical margins/padding don't affect layout
- **Default Elements**: ```<span>```, ```<a>```, ```<strong>```, ```<em>```
- **CSS**: ```display: inline```;

### Inline-Block Elements
#### Hybrid Behavior:
- Flows like inline element
- Allows width/height like block
- Respects vertical margins/padding
- **Common Uses**: Navigation menus, grid items
- **CSS**: ```display: inline-block```;
