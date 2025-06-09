# Lesson 2 Start Thinking in Python

In this lesson, we'll cover the fundamentals of Python, starting with an exploration of various data types, including integers, real numbers, and strings. As you progress through the lesson, you'll discover how to use expressions in mathematical operations, store values in variables, and explore multiple techniques for manipulating strings.

## Learning Objectives:
- Demonstrate an understanding of types in Python by converting or casting data types such as strings, floats, and integers.
- Interpret variables and solve expressions by applying mathematical operations.
- Describe how to manipulate strings by using a variety of methods and operations.
- Build a program in JupyterLab to demonstrate your knowledge of types, expressions, and variables.
- Work with, manipulate, and perform operations on strings in Python.

## Agenda
1. Getting Started with Jupyter
2. Types
3. Expressions and Variables
4. String Operations

### 1. Getting Started with Jupyter

In this section, you will learn Step-by-Step Installation of Anaconda and Open Jupyter Notebook


#### Step 1: Download the Anaconda Installer

- Open your web browser (e.g., Chrome, Edge, or Firefox).
- Go to the official Anaconda download page: https://www.anaconda.com/products/distribution.
- Scroll to the Anaconda Installers section.
- Under Windows, select the 64-bit Graphical Installer (recommended for beginners) for the latest Python version (e.g., Python 3.9 or higher).
- If you have a 32-bit system (rare), choose the 32-bit installer.
- The installer file (e.g., Anaconda3-2023.09-0-Windows-x86_64.exe) will begin downloading. File size is approximately 400–600 MB, so it may take a few minutes depending on your internet speed.

#### Step 2: Install Anaconda
- Locate the downloaded installer in your Downloads folder (or wherever you saved it).
- Double-click the installer file to launch it.
- If prompted by Windows User Account Control (UAC), click Yes to allow the installer to make changes.

#### In the Anaconda installer:
- Welcome Screen: Click Next.
- License Agreement: Read the agreement, select I Agree, and click Next.
- Installation Type: Choose Just Me (recommended for most users) or All Users (requires admin privileges), then click Next.
- Destination Folder: Keep the default location (e.g., C:\Users\<YourUsername>\Anaconda3) or choose a custom folder with sufficient space, then click Next.

#### Advanced Options:
- Check Add Anaconda3 to my PATH environment variable (optional, but useful for command-line access).
- Check Register Anaconda3 as my default Python 3.x (recommended unless you have another Python installation you prefer).
- Click Next.
- Click Install to begin the installation. This may take 5–15 minutes depending on your system.
- Once installation is complete, click Next.
- (Optional) Select Install Microsoft VSCode if you want to install VSCode alongside Anaconda, then click Next.
- Click Finish to close the installer.

#### Step 3: Verify Anaconda Installation
- Open the Start Menu and search for Anaconda Prompt.
- Click Anaconda Prompt to open it.
- In the prompt, type the following command and press Enter:conda --version
-  You should see output like conda 23.7.4 (version numbers may vary). This confirms Anaconda is installed.
- Update Anaconda to the latest version by running:conda update --all --yes
- This ensures all packages, including Jupyter Notebook, are up to date.

#### Step 4: Install Jupyter Notebook (if not already included)
- Anaconda typically includes Jupyter Notebook by default, but you can verify or install it manually.
- In the Anaconda Prompt, type:conda install jupyter
- If prompted, confirm by typing y and press Enter.
- Wait for the installation to complete (this step is usually unnecessary if using a recent Anaconda installer).

#### Step 5: Open Jupyter Notebook
There are multiple ways to launch Jupyter Notebook. Below are the two most common methods for beginners:
**Method 1**: Using Anaconda Navigator (Graphical Interface)
- Open the Start Menu and search for Anaconda Navigator.
- Click Anaconda Navigator to launch it.
- It may take a moment to load, especially the first time.
- In the Anaconda Navigator window, find the Jupyter Notebook tile.
- Click the Launch button under the Jupyter Notebook tile.
- A browser window (e.g., Chrome, Edge) will open, displaying the Jupyter Notebook dashboard.
- The dashboard shows files in your home directory (e.g., C:\Users\<YourUsername>).
- To create a new notebook, click New > Python 3 in the dashboard.
- A new notebook will open where you can start coding.

**Method 2**: Using Anaconda Prompt (Command Line)
- Open the Start Menu and search for Anaconda Prompt.
- Click Anaconda Prompt to open it.
- Type the following command and press Enter:jupyter notebook
- The Jupyter Notebook server will start, and a browser window will open with the dashboard.
- The terminal will display a URL (e.g., http://localhost:8888) that you can copy into a browser if it doesn’t open automatically.
- To create a new notebook, click New > Python 3 in the dashboard.

#### Step 6: Using Jupyter Notebook
- In the Jupyter dashboard, navigate to your desired folder or create a new one to store your notebooks.
- To create a new notebook, click New > Python 3.
- To open an existing notebook (.ipynb file), navigate to its location and click it.
- Save your work frequently using File > Save and Checkpoint or the save icon.
- To stop the Jupyter server, return to the Anaconda Prompt and press Ctrl+C, then type y and press Enter to confirm.

