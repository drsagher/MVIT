# Lesson 01 Installing Scikit-Learn

## Python Installation on Windows
- Go to the [official Python website](https://www.python.org/downloads/windows/) and download the latest version.
- During installation, check the box for "Add Python to PATH" and proceed with installation.
- To verify Python installation, Open Command Prompt Windows) and type ```python --version```. It should display the installed Python version.

## Install VS Code
- Download VS Code from the [official website](https://code.visualstudio.com/download).
- Install VS Code by following the installation instructions for your operating system.

## Install Required Extensions
- Open VS Code.
- Go to Extensions or use (```Ctrl + Shift + X```)
- Search for Python and install the extension by Microsoft.

## Create a Virtual Environment (Recommended)
- Create a folde with name ```scikit-learn``` any where in your directory.
- Open this folder in VS Code
- Open VS Code Terminal (```Ctrl + ~```).
- Create a virtual environment by ```python -m venv venv```
- Activate the virtual environment by ``` venv\Scripts\activate```

## Install Scikit-Learn
- Once your virtual environment is activated, install Scikit-Learn using pip: ``` pip install scikit-learn```
- To verify the installation, run: ``` python -c "import sklearn; print(sklearn.__version__)" ```
- It should print the installed Scikit-Learn version.

## Configure VS Code Interpreter
- Open VS Code.
- Press ```Ctrl + Shift + P``` and search for "Python: Select Interpreter".
- Select your virtual environment (```venv```).
- Restart VS Code if necessary.

## Write and Run a Simple Scikit-Learn Program
- Create a new Python file (```example.py```).
- Write a simple script:

```
from sklearn.linear_model import LinearRegression

# Sample data
X = [[1], [2], [3], [4], [5]]
y = [2, 4, 6, 8, 10]

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict

print("Prediction for 6:", model.predict([[6]])[0])
```

- Run the script in the terminal:
```
python example.py
```

## You're All Set! 🚀
You have successfully set up Scikit-Learn in VS Code and tested a simple machine-learning model. You can now explore data science and AI projects efficiently! 🔥



