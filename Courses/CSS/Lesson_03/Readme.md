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
