# Lesson 02 CSS Selectors
CSS (Cascading Style Sheets) selectors are patterns used to select and style HTML elements. They allow developers to target specific elements or groups of elements in a document to apply styles. Below is a detailed breakdown of CSS selector types, their syntax, and usage:

## 1. Basic Selectors
### a. Element Selector
- Targets HTML elements by their tag name.
- Syntax: element
- Example: ``` p { color: blue; } /* Styles all <p> elements */ ```

### b. Class Selector
- Targets elements with a specific class attribute.
- Syntax: .class-name
- Example: ``` .highlight { background: yellow; } /* Styles elements with class="highlight" */ ```

### c. ID Selector
- Targets a single element with a unique id attribute.
- Syntax: #id-name
- Example: ``` #header { font-size: 24px; } /* Styles the element with id="header" */ ```

### d. Universal Selector
- Targets all elements on the page.
- Syntax: *
- Example: ``` * { margin: 0; } /* Resets margin for all elements */ ```

## 2. Combinators
Combinators define relationships between elements.

### a. Descendant Combinator (Space)
- Targets elements nested within another element (any level deep).
- Syntax: ancestor descendant
- Example: ``` div p { color: red; } /* Styles <p> elements inside any <div> */ ```

### b. Child Combinator (>)
- Targets direct children of an element.
- Syntax: parent > child
- Example: ``` ul > li { list-style: none; } /* Styles direct <li> children of <ul> */ ```

### c. Adjacent Sibling Combinator (+)
- Targets the immediately following sibling element.
- Syntax: element + sibling
- Example: ``` h1 + p { margin-top: 0; } /* Styles <p> directly after <h1> */ ```

### d. General Sibling Combinator (~)
- Targets all subsequent sibling elements.
- Syntax: element ~ sibling
- Example: ``` h1 ~ p { color: green; } /* Styles all <p> elements after <h1> */ ```

## 3. Attribute Selectors
Target elements based on attributes or attribute values.

### a. Simple Attribute
- Syntax: [attribute]
- Example: ``` [disabled] { opacity: 0.5; } /* Styles elements with the 'disabled' attribute */ ```

### b. Attribute with Value
- Syntax: [```attribute="value"```]
- Example: ``` [type="text"] { border: 1px solid gray; } /* Styles text inputs */ ```

### c. Substring Matches
- [attribute^="value"]: Starts with "value".
- [attribute$="value"]: Ends with "value".
- [attribute*="value"]: Contains "value" anywhere.
- Example: ``` a[href^="https"] { color: green; } /* Styles links starting with "https" */ ```

### d. Case-Insensitive Match (CSS4)
- Syntax: [attribute="value" i]
- Example: ``` [lang="en" i] { font-style: italic; } /* Matches "en", "EN", etc. */ ```

## 4. Pseudo-Classes
Target elements in a specific state or position.

### a. Common State-Based Pseudo-Classes
- ```:hover```: Styles on mouse hover.
- ```:active```: Styles while being clicked.
- ```:focus```: Styles when focused (e.g., form inputs).
- Example: ``` button:hover { background: #ddd; } ```

### b. Structural Pseudo-Classes
- ```:first-child```: First child of its parent.
- ```:last-child```: Last child of its parent.
- ```:nth-child(n)```: Matches elements based on a formula (e.g., 2n for even elements).
- ```:nth-of-type(n)```: Similar to :nth-child, but only for elements of the same type.
- Example: ``` tr:nth-child(odd) { background: #f5f5f5; } /* Zebra-striping table rows */ ```

### b. Structural Pseudo-Classes
- ```:first-child```: First child of its parent.
- ```:last-child```: Last child of its parent.
- ```:nth-child(n)```: Matches elements based on a formula (e.g., 2n for even elements).
- ```:nth-of-type(n)```: Similar to :nth-child, but only for elements of the same type.
- Example: ``` tr:nth-child(odd) { background: #f5f5f5; } /* Zebra-striping table rows */ ```

### c. Form-Related Pseudo-Classes
- ```:checked```: Checked checkboxes/radio buttons.
- ```:disabled```: Disabled form elements.
- Example: ``` input:checked { accent-color: blue; } ```

### d. Logical Pseudo-Classes (CSS4)
- ```:is()```: Groups selectors (reduces repetition).
- ```:where()```: Similar to :is(), but with zero specificity.
- Example: ``` :is(header, footer) a { color: white; } ```

## 5. Pseudo-Elements
Style specific parts of an element.

### a. ::before and ::after
- Inserts content before/after an element.
- Example: ``` .note::before { content: "⚠️"; } /* Adds an icon before .note elements */ ```





