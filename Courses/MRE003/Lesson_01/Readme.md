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
- Once your virtual environment is activated, install Scikit-Learn using pip:
  ```
  pip install scikit-learn
  ```
  
- To verify the installation, run:
  ```
  python -c "import sklearn; print(sklearn.__version__)"
  ```
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



## Linear Regression with Scikit-Learn

This example demonstrates how to use **Linear Regression** in **Scikit-Learn** to train a model and make predictions.

### Code Explanation

#### 1. Importing Required Library
```python
from sklearn.linear_model import LinearRegression
```
- Imports the `LinearRegression` class from **Scikit-Learn**.
- Used for predicting continuous values based on input data.

#### 2. Defining the Dataset
```python
X = [[1], [2], [3], [4], [5]]  # Input (Independent Variable)
y = [2, 4, 6, 8, 10]  # Output (Dependent Variable)
```
- `X`: A list of lists, where each inner list contains a **single feature**.
- `y`: A list of corresponding output values.
- The dataset follows a simple **linear relationship**:
  
  \[ y = 2x \]

#### 3. Creating and Training the Model
```python
model = LinearRegression()
model.fit(X, y)
```
- `LinearRegression()` initializes the model.
- `.fit(X, y)` trains the model by finding the **best-fit line**.
- Internally, the model learns the equation:
  
  \[ y = mx + b \]
  
  where **m (slope) ≈ 2** and **b (intercept) ≈ 0**.

#### 4. Making a Prediction
```python
print("Prediction for 6:", model.predict([[6]])[0])
```
- `.predict([[6]])` predicts the output when `X = 6`.
- Expected output:
  
  \[ y = 2(6) = 12 \]

#### 5. Output
```
Prediction for 6: 12.0
```
The model correctly predicts `12.0` based on the learned relationship.

### Summary
- **Trains a Linear Regression model** on a simple dataset.  
- **Learns the relationship `y = 2x`**.  
- **Predicts `y = 12` when `X = 6`**.  
- Demonstrates **basic supervised learning** using Scikit-Learn.

## You're All Set! 🚀
You have successfully set up Scikit-Learn in VS Code and tested a simple machine-learning model. You can now explore data science and AI projects efficiently! 🔥



