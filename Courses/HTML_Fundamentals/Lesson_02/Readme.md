# Lesson 2 Basic HTML Document Structure
An HTML document follows a standardized hierarchy of tags to ensure browsers render content correctly. Here’s what it looks like:

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document Title</title>
</head>
<body>
    <!-- Visible content goes here -->
    <h1>Hello, World!</h1>
    <p>This is a paragraph.</p>
</body>
</html>
```

##  ``` <!DOCTYPE html> ```
- Declares the document type and HTML version (HTML5 in this case).
- Ensures the browser renders the page in standards mode.

##  ``` <html> ```
- The root element wrapping all content.
- The ``` lang ``` attribute specifies the document’s language (e.g., ``` en ``` for English).

## ``` <head> ```
- Contains metadata (data about the page) not visible to users.
- Includes:
  - ``` <meta charset="UTF-8"> ``` : Sets character encoding (supports all symbols/emojis).
  - ``` <meta name="viewport"> ``` : Ensures responsive design on mobile devices.
  - ``` <title> ```: Defines the page title shown in browser tabs/bookmarks.
  - Links to CSS files, scripts, or icons.

## ``` <body> ```
- Holds visible content displayed to users: text, images, links, forms, etc.
- Common elements: headings ``` <h1> to <h6> ```, paragraphs ``` <p> ```, lists, images ``` <img> ```, and semantic tags like ``` <header>, <main>, <footer> ```.

## Key Notes
- Indentation: Proper indentation improves readability (not required but recommended).
- Semantic Tags: Modern HTML uses tags like ``` <header>, <nav> ```, and ``` <article> ``` for better accessibility and SEO.
- External Files: CSS and JavaScript are often linked in the <head> or at the end of ``` <body> ```.

## Why This Structure Matters
- Browsers use this structure to parse and render content accurately.
- Missing tags e.g., ``` <head> or <body> ``` can cause rendering issues.
- A well-structured document is essential for SEO, accessibility, and future code maintenance.

## HTML Comments
In HTML, comments are notes added to the code that are ignored by browsers and not displayed on the webpage. They help developers explain code, leave reminders, or temporarily disable parts of the HTML without deleting them.
