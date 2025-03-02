# Lesson 04 Display property: ```block```, ```inline```, ```inline-block```
Mastering the CSS display property is essential for building visually appealing and responsive web pages. The display property determines how an element is displayed and laid out on a web page, with three fundamental values: block, inline, and inline-block. Block elements, such as divs and paragraphs, occupy the full width of their parent container and start on a new line. Inline elements, like spans and anchors, sit alongside other elements on the same line. Inline-block elements, meanwhile, combine the characteristics of both, allowing for precise control over layout and design. Understanding the nuances of these display properties is crucial for creating flexible, responsive, and maintainable CSS layouts.

## Core Concepts

### Block Elements
- Starts on a new line
- Takes full available width
- Respects width/height properties
- Margin/padding push other elements away
- **Default Elements**: ```<div>```, ```<h1>-<h6>```, ```<p>```, ```<section>```
- **CSS**: ```display: block```;

### Inline Elements
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

### Hands-On Activity
**Objective**: Create a webpage demonstrating all three display types.

### ```index.html```

```
<!DOCTYPE html>
<html>
<head>
    <title>Display Property Demo</title>
    <style>
        .block-box { 
            display: block;
            width: 200px;
            height: 100px;
            background: #ff9999;
            margin: 10px;
        }
        
        .inline-text {
            display: inline;
            background: #99ff99;
            padding: 5px;
        }
        
        .inline-block-item {
            display: inline-block;
            width: 150px;
            background: #9999ff;
            margin: 5px;
        }
    </style>
</head>
<body>
    <div class="block-box">Block Element 1</div>
    <div class="block-box">Block Element 2</div>
    
    <p>This is <span class="inline-text">inline text</span> within a paragraph. 
    Another <span class="inline-text">inline element</span> here.</p>
    
    <div class="inline-block-item">Inline-Block 1</div>
    <div class="inline-block-item">Inline-Block 2</div>
    <div class="inline-block-item">Inline-Block 3</div>
</body>
</html>
```

### Tasks:
- Toggle between display values to see layout changes
- Try adding margins to inline elements
- Experiment with vertical-align on inline-block items
- Create a navigation menu using inline-block


