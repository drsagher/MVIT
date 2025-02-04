# Lesson 3 HTML Elements and Tags
HTML Elements and Tags are the building blocks of a web page, used to define the structure and content of a document. HTML Elements represent a component or a section of a web page, such as a heading, paragraph, image, or link, while Tags are the markup symbols used to define the start and end of an element. HTML Tags are surrounded by angle brackets and usually come in pairs, with the opening tag preceding the content and the closing tag following it, allowing web browsers to interpret and render the content correctly.

## Basic HTML Tags
1. ``` <!DOCTYPE> ```  Document type declaration
2. ``` <html> ```  Root element of an HTML document
3. ``` <head> ```  Contains metadata about the document
4. ``` <title> ```  Specifies the title of the document
5. ``` <body> ```  Contains the content of the HTML document

## Heading Tags
1.  ``` <h1> ```  Main heading
2.  ``` <h2> ```  Subheading
3.  ``` <h3> ```  Sub-subheading
4.  ``` <h4> ```  Sub-sub-subheading
5.  ``` <h5> ```  Sub-sub-sub-subheading
6.  ``` <h6> ```  Sub-sub-sub-sub-subheading

## Paragraph and Text Tags
1.  ``` <p> ```  Paragraph
2.  ``` <span> ```  Inline container for text
3.  ``` <br> ```  Line break
4.  ``` <hr> ```  Horizontal rule

## Link and Navigation Tags
1. ``` <a> ``` Anchor (link)
2. ``` <nav> ``` Navigation section
3. ``` <ul> ``` Unordered list
4. ``` <ol> ``` Ordered list
5. ``` <li> ``` List item

## Image and Media Tags
1. ``` <img> ``` Image
2. ``` <video> ``` Video
3. ``` <audio> ``` Audio
4. ``` <source> ``` Media source
5. ``` <track> ``` Media track

## Table Tags
1. ``` <table> ``` Table
2. ``` <tr> ``` Table row
3. ``` <td> ``` Table data cell
4. ``` <th> ``` Table header cell
5. ``` <caption> ``` Table caption
6. ``` <col> ``` Table column
7. ``` <colgroup> ``` Table column group

## Form Tags
1. ``` <form> ``` Form
2. ``` <input> ``` Input field
3. ``` <textarea> ``` Text area
4. ``` <select> ``` Select menu
5. ``` <option> ``` Option in a select menu
6. ``` <button> ``` Button
7. ``` <label> ``` Label for a form control
8. ``` <fieldset> ``` Group of form controls
9. ``` <legend> ``` Caption for a fieldset

## Semantic HTML Tags
1. ``` <header> ``` Header section
2. ``` <footer> ``` Footer section
3. ``` <main> ``` Main content section
4. ``` <section> ``` Section of related content
5. ``` <article> ``` Independent piece of content
6. ``` <aside> ``` Tangential content
7. ``` <figure> ``` Figure with a caption
8. ``` <figcaption> ``` Caption for a figure

## Interactive HTML Tags
1. ``` <canvas> ``` Canvas for dynamic graphics
2. ``` <details> ``` Details with a disclosure widget
3. ``` <dialog> ``` Dialog box
4. ``` <menu> ``` Menu with interactive items
5. ``` <summary> ``` Summary or caption for a details element

## HTML Tags with Example

| Tag | Description | Example |
| --- | --- | --- |
| ```<!DOCTYPE>``` | Document type declaration | ```<!DOCTYPE html>``` |
| ```<html>``` | Root element of an HTML document | ```<html>...</html>``` |
| ```<head>``` | Contains metadata about the document | ```<head>...</head>``` |
| ```<title>``` | Specifies the title of the document | ```<title>Page Title</title>``` |
| ```<body>``` | Contains the content of the HTML document | ```<body>...</body>``` |
| ```<h1>``` | Main heading | ```<h1>Heading</h1>``` |
| ```<h2>``` | Subheading | ```<h2>Subheading</h2>``` |
| ```<h3>``` | Sub-subheading | ```<h3>Sub-subheading</h3>``` |
| ```<h4>``` | Sub-sub-subheading | ```<h4>Sub-sub-subheading</h4>``` |
| ```<h5>``` | Sub-sub-sub-subheading | ```<h5>Sub-sub-sub-subheading</h5>``` |
| ```<h6>``` | Sub-sub-sub-sub-subheading | ```<h6>Sub-sub-sub-sub-subheading</h6>``` |
| ```<p>``` | Paragraph | ```<p>Paragraph text</p>``` |
| ```<span>``` | Inline container for text | ```<span>Span text</span>``` |
| ```<br />``` | Line break | ```<br />``` |
| ```<hr />``` | Horizontal rule | ```<hr />``` |
| ```<a>``` | Anchor (link) | ```<a href="https://www.example.com">Link text</a>``` |
| ```<nav>``` | Navigation section | ```<nav>...</nav>``` |
| ```<ul>``` | Unordered list | ```<ul>...</ul>``` |
| ```<ol>``` | Ordered list | ```<ol>...</ol>``` |
| ```<li>``` | List item | ```<li>List item text</li>``` |
| ```<img>``` | Image | ```<img src="image.jpg" alt="Image alt text">``` |
| ```<video>``` | Video | ```<video src="video.mp4" controls></video>``` |
| ```<audio>``` | Audio | ```<audio src="audio.mp3" controls></audio>``` |
| ```<source>``` | Media source | ```<source src="media.mp4" type="video/mp4">``` |
| ```<track>``` | Media track | ```<track src="track.vtt" kind="captions" srclang="en" label="English">``` |
| ```<table>``` | Table | ```<table>...</table>``` |
| ```<tr>``` | Table row | ```<tr>...</tr>``` |
| ```<td>``` | Table data cell | ```<td>Cell text</td>``` |
| ```<th>``` | Table header cell | ```<th>Header text</th>``` |
| ```<caption>``` | Table caption | ```<caption>Caption text</caption>``` |
| ```<col>``` | Table column | ```<col span="2" style="background-color: #f2f2f2;">``` |
| ```<colgroup>``` | Table column group | ```<colgroup span="3" style="background-color: #f2f2f2;"></colgroup>``` |
| ```<form>``` | Form | ```<form>...</form>``` |
| ```<input>``` | Input field | ```<input type="text" name="username" placeholder="Username">``` |
| ```<textarea>``` | Text area | ```<textarea name="message" rows="5" cols="30"></textarea>``` |
| ```<select>``` | Select menu | ```<select name="options">...</select>``` |
| ```<option>``` | Option in a select menu | ```<option value="option1">Option 1</option>``` |
| ```<button>``` | Button | ```<button type="submit">Submit</button>``` |
| ```<label>``` | Label for a form control | ```<label for="username">Username:</label>``` |
| ```<fieldset>``` | Group of form controls | ```<fieldset>...</fieldset>``` |
| ```<legend>``` | Caption for a fieldset | ```<legend>Caption text</legend>``` |
| ```<header>``` | Header section | ```<header>...</header>``` |
| ```<footer>``` | Footer section | ```<footer>...</footer>``` |
| ```<main>``` | Main content section | ```<main>...</main>``` |
| ```<section>``` | Section of related content | ```<section>...</section>``` |
| ```<article>``` | Independent piece of content | ```<article>...</article>``` |
| ```<aside>``` | Tangential content | ```<aside>...</aside>``` |
| ```<figure>``` | Figure with a caption | ```<figure>...</figure>``` |
| ```<figcaption>``` | Caption for a figure | ```<figcaption>Caption text</figcaption>``` |
| ```<canvas>``` | Canvas for dynamic graphics | ```<canvas id="canvas" width="400" height="200"></canvas>``` |

##  HTML Semantic Tags

| Tag | Description | Example |
| --- | --- | --- |
| ```<article>``` | Independent piece of content | ```<article>...</article>``` |
| ```<aside>``` | Tangential content | ```<aside>...</aside>``` |
| ```<details>``` | Details with a disclosure widget | ```<details>...</details>``` |
| ```<figcaption>``` | Caption for a figure | ```<figcaption>Caption text</figcaption>``` |
| ```<figure>``` | Figure with a caption | ```<figure>...</figure>``` |
| ```<footer>``` | Footer section | ```<footer>...</footer>``` |
| ```<header>``` | Header section | ```<header>...</header>``` |
| ```<main>``` | Main content section | ```<main>...</main>``` |
| ```<mark>``` | Highlighted text | ```<mark>Highlighted text</mark>``` |
| ```<nav>``` | Navigation section | ```<nav>...</nav>``` |
| ```<section>``` | Section of related content | ```<section>...</section>``` |
| ```<summary>``` | Summary or caption for a details element | ```<summary>Summary text</summary>``` |
| ```<time>``` | Date or time | ```<time>2022-07-25</time>``` |
