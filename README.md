# Python Environments and Best Practises Live Training

This is the code for the *O'Reilly Live Training* - **Python Environments and Best Practises** presented by Arianne Dee

**Note**: If you're looking for the project code for a specific date in the past,
look for the specific class [here](https://github.com/ariannedee/python-environments/releases)

Before the class, please follow these instructions:
1. [Install Python](#1-install-python-38-or-higher)
1. [Check that Python was installed properly](#2-make-sure-that-python-is-properly-installed)
1. [Install PyCharm](#3-download-pycharm-community-edition)
1. [Download the code](#4-download-the-course-files)

## Set up instructions
### 1. Install Python 3.8 or higher
Go to https://www.python.org/downloads/

Click the yellow button at the top to download the latest version of Python.

#### On Mac or Linux
Follow the prompts and install using the default settings.

#### On Windows
The default settings don't add Python to your PATH 
so your computer doesn't know where to look for it when Python runs 
(for some inexplicable reason).

##### If you're just installing Python now
Follow the instructions here: [Windows Python installer instructions](docs/WININSTALL.md)

##### If you've already installed Python with the default settings
Follow the instructions here: [Add Python to PATH variable in Windows](docs/WINSETPATH.md)

### 2. Make sure that Python is properly installed
1. Open the *Command Prompt* application in Windows
or *Terminal* on Mac or Linux

1. Type `python --version` and press enter

1. Type `python3 --version` and press enter

1. One or both of those commands should print 
a Python version of 3.8 or higher 
(whichever version you just downloaded).
 If it doesn't, you have to follow instructions to
 [add Python to your PATH variable](docs/WINSETPATH.md).

**Note:** 
You can now type just the `python` or `python3` command
in *Command Prompt* or *Terminal* 
to run the Python interpreter.
You can also run a *.py* file by running 
`python filename.py`

### 3. Download PyCharm
Download here: https://www.jetbrains.com/pycharm/download/

Install, open, and use the default settings.

### 4. Download the course files

#### If you know git:
Clone the repository.

#### If you don't know git:
1. Click the "Clone or download" (green) button at the top-right of the page
2. Click "Download ZIP"
3. Unzip it and move the **python-environments-main** folder to a convenient location

## FAQs

### Can I use a different code editor besides PyCharm?

You can use VS Code for this class.

Jupyter notebooks are not ideal since we'll be working from multiple folders throughout the class.

### PyCharm can't find Python 3

On a Mac:
- Go to **PyCharm** > **Preferences**

On a PC:
- Go to **File** > **Settings**

Once in Settings:
1. Go to **Project: python-environments** > **Project Interpreter**
1. Look for your Python version in the Project Interpreter dropdown
1. If it's not there, click **gear icon** > **Add...**
1. In the new window, select **System Interpreter** on the left, and then look for the Python version in the dropdown
1. If it's not there, click the **...** button and navigate to your Python location
   - To find where Python is located, [look in these directories](docs/PATH_LOCATIONS.md)
   - You may have to search the internet for where Python gets installed by default on your operating system

### Do you offer private Python help?
Yes, email **arianne.dee.studios at gmail.com** if you have any questions.
