# Painting and Drawing, Windows Management, Input devices, Resources

## 1. Painting and Drawing in Visual C#.NET
Painting and drawing are fundamental aspects of graphical application development in Visual C#.NET. These operations allow developers to create visually appealing interfaces and custom graphics within Windows Forms or WPF (Windows Presentation Foundation) applications.

- Graphics Class : The ```System.Drawing.Graphics``` class is used to render shapes, text, and images on a form or control. It provides methods like ```DrawLine()```, ```DrawRectangle()```, ```FillEllipse()```, and ```DrawString()``` for creating visual elements.
- Paint Event : The ```Paint``` event is triggered whenever a control needs to be redrawn (e.g., when resizing or minimizing/restoring a window). Developers handle this event to define custom drawing logic.
- Example : Drawing a rectangle on a form

```
private void Form1_Paint(object sender, PaintEventArgs e)
{
    Graphics g = e.Graphics;
    Pen pen = new Pen(Color.Blue, 3);
    g.DrawRectangle(pen, 50, 50, 100, 100);
}
```

## 2. Window Management in Visual C#.NET
Window management involves controlling the behavior and appearance of windows (forms) in a C#.NET application. This includes tasks like opening, closing, resizing, and organizing multiple windows.

- Form Class : The Form class represents a window in a Windows Forms application. Developers can customize properties like Text, Size, StartPosition, and WindowState to manage the form's behavior.
- Dialog Boxes : Use modal (ShowDialog()) or modeless (Show()) dialog boxes to interact with users. Modal dialogs block interaction with other windows until closed, while modeless dialogs allow multitasking.
- Multiple Windows : Applications with multiple forms can use techniques like MDI (Multiple Document Interface) to organize child windows within a parent window.
