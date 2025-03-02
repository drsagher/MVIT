# Lesson 03 Box Model
The CSS Box Model is a fundamental concept in web development that describes the structure of an HTML element as a rectangular box. The box model consists of four main parts: content, padding, border, and margin.

## Box Model Components
1. Content Area: The innermost part of the box model, where the element's content is displayed.
2. Padding: The space between the content area and the border. Padding is used to add space around the content.
3. Border: The visible outline of the box. Borders can be styled with different colors, styles, and widths.
4. Margin: The space between the box and other elements. Margins are used to add space around the box.

## Box Model Properties
Here are some common CSS properties used to style the box model:

- ```width``` and ```height```: Set the width and height of the content area.
- ```padding```: Set the padding of the box.
- ```border```: Set the border of the box.
- ```margin```: Set the margin of the box.
- ```box-sizing```: Set the box-sizing property to either content-box or border-box.

## Box-Sizing Property
The box-sizing property is used to define how the width and height of an element are calculated. There are two values:
- ```content-box```: The width and height of the element are calculated based on the content area only.
- ```border-box```: The width and height of the element are calculated based on the content area, padding, and border.

## Example
Here is an example of how to use the box model properties:
```
.box {
  width: 200px;
  height: 100px;
  padding: 20px;
  border: 1px solid #ccc;
  margin: 10px;
  box-sizing: border-box;
}
```

In this example, the .box element has a width of 200px and a height of 100px. The padding is set to 20px, and the border is set to 1px solid #ccc. The margin is set to 10px. The box-sizing property is set to border-box, which means that the width and height of the element are calculated based on the content area, padding, and border.

## Activity: Building a card component using the box model

### ```index.html```

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Card Component</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="card">
        <img src="https://source.unsplash.com/random/400x300" alt="Random image" class="card-image">
        <div class="card-content">
            <h2 class="card-title">Card Title</h2>
            <p class="card-text">This is a sample card component demonstrating the CSS box model with various elements including an image, title, text, and button.</p>
            <a href="#" class="card-button">Learn More</a>
        </div>
    </div>
</body>
</html>
```

### ```styles.css```

```
/* styles.css */
body {
    font-family: Arial, sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    margin: 0;
    background-color: #f0f0f0;
}

.card {
    width: 400px;
    background-color: white;
    border-radius: 10px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    margin: 20px;
    overflow: hidden;
}

.card-image {
    width: 100%;
    height: 300px;
    object-fit: cover;
}

.card-content {
    padding: 25px;
}

.card-title {
    margin: 0 0 15px 0;
    color: #333;
}

.card-text {
    margin: 0 0 20px 0;
    color: #666;
    line-height: 1.6;
}

.card-button {
    display: inline-block;
    padding: 10px 20px;
    background-color: #007bff;
    color: white;
    text-decoration: none;
    border-radius: 5px;
    transition: background-color 0.3s ease;
}

.card-button:hover {
    background-color: #0056b3;
}
```

This implementation demonstrates:

### Box Model Components:
- Content: Text, image, and button
- Padding: Inside spacing of content area
- Border: Rounded corners (border-radius)
- Margin: Space around the card
- Box-shadow: Creates depth effect

### Key Features:
- Responsive width with fixed image height
- Flexbox centering for the card
- Proper content hierarchy and spacing
- Hover effects on the button
- Clean typography and color scheme
- Box-shadow for depth perception
- Overflow hidden for image containment

### File Structure:
- Separate HTML and CSS files
- Proper semantic class naming
- External CSS stylesheet linked in head
- Responsive Considerations:
- Flexible width using percentage values
- Fixed image height with object-fit
- Proper padding and margin usage
- Mobile-friendly dimensions

### To use this component:
- Create both HTML and CSS files
- Link the CSS file properly in the HTML head
- Save the HTML file and open in a browser
- Customize colors, sizes, and content as needed

### You can modify the:
- Colors (background, text, button)
- Padding and margin values
- Border radius
- Box shadow intensity
- Image source and dimensions
- Font sizes and family
- Button styling and transitions


## Assignment: Understanding CSS Selector Specificity

### Objective
Demonstrate understanding of CSS selector specificity by creating a webpage that shows how different selectors override each other based on their specificity weight.

### Tasks:
### HTML Structure ```specificity.html```

#### Create a basic HTML document with
- 1 heading ```<h1>```
- 3 paragraphs ```<p>```
- 1 div containing 1 paragraph
- 1 button

### CSS Rules ```specificity.css```

#### Create conflicting style declarations that demonstrate
- Element selector vs Class selector
- Class selector vs ID selector
- Multiple classes vs single class
- Inline styles vs external styles
- !important declaration
- Specificity Challenges

#### Implement these specific style conflicts
- Make one paragraph red using element selector, blue using class
- Make heading green with ID selector, orange with inline style
- Style button with multiple conflicting selector combinations

### Documentation
- Add CSS comments explaining why particular styles won in each conflict

### Starter Code

#### ```specificity.html```

```
<!-- specificity.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Selector Specificity</title>
    <link rel="stylesheet" href="specificity.css">
</head>
<body>
    <h1 id="main-heading" class="heading">Specificity Challenge</h1>
    
    <p class="text">First paragraph</p>
    <p class="text special">Second paragraph</p>
    <p class="text" id="unique-paragraph">Third paragraph</p>
    
    <div class="container">
        <p>Nested paragraph</p>
    </div>
    
    <button class="btn primary-btn" id="action-btn" style="background-color: blue">
        Click Me
    </button>
</body>
</html>
```

#### ```specificity.css```

```
/* specificity.css */
/* Base Styles */
body {
    font-family: Arial, sans-serif;
    margin: 2rem;
}

/* Add your conflicting selectors below */
```

### Expected Outcome:
Create visual demonstrations of these specificity principles:
ID selectors (#) beat class selectors (.)
Class selectors beat element selectors
Inline styles beat external styles
!important overrides everything
More specific selectors beat less specific ones

### Challenge Questions:
What will be the color of the third paragraph if both ID and !important are used?
How does the order of stylesheets affect specificity?
Why should !important be used sparingly?

### Solution Guidelines:
Use the specificity weight formula: (inline, IDs, classes, elements)
Demonstrate at least 5 specificity conflicts
Use color changes as the primary visual indicator
Include commented explanations in CSS

### Sample Solution Excerpt:

```
/* specificity.css */
/* Task 1: Element vs Class */
p { color: red; }
.text { color: blue; } /* Wins - class > element */

/* Task 2: Class vs ID */
.heading { color: green; }
#main-heading { color: orange; } /* Wins - ID > class */

/* Task 3: Multiple Classes vs Single Class */
.special { font-weight: normal; }
.text.special { font-weight: bold; } /* Wins - more specific */

/* Task 4: Inline vs External */
#action-btn { background-color: green; }
/* Inline style (blue) wins unless !important is used */

/* Task 5: !important Override */
#action-btn { color: white !important; }
button { color: black; } /* !important wins despite lower specificity */
```

### Learning Outcomes:
- Understand specificity hierarchy
- Calculate specificity weights
- Resolve style conflicts effectively
- Apply best practices for selector usage
- Recognize anti-patterns in CSS authoring

### Submission Requirements:
- Working HTML/CSS files
- Clear visual demonstrations of specificity
- Comments explaining each conflict resolution
- Answers to challenge questions in CSS comments

This assignment helps students practically understand one of CSS's most fundamental concepts through hands-on implementation and controlled style conflicts. The complexity can be adjusted based on student level by adding more complex selector combinations or including pseudo-classes.
