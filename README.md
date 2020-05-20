# Assignment 1

Welcome to your first Python programming assignment.

## The goal

The goal of this assignment is to introduce you to the work environment you will use to complete assignments in this course.

## Where we are

### Cloned repository

If you are viewing this file, then you have most likely downloaded a **repository** of code from a code-sharing web site owned by Microsoft called GitHub.com.

If so, you now have a **clone** of this repository on your own _local_ computer. The original copy of the code still resides on GitHub.com as well.

You will make changes to your local copy of the code using a code editor. And, when you are done modifying the code, you will upload it back to GitHub.com in order to share it with the course instructor and graders. This is how you will submit your work.

### Git

Whether you did so intentionally or not, you most likely used a software program called **git** in order to download this code to your local machine. You will also use git to upload your modified code back to GitHub.com when you are done with the assignment.

Git is open source software for **version control**. It helps programmers keep an archive of all the changes they make to their code, and it helps them share those changes they make with other developers.

In our case, you will be using git to share your modified code with the course instructor and graders. You will likely never directly use git - rather, the editor software you to modify the code will trigger git to upload or download code on your behalf.

### Code editor

To make changes to this code, you will need a **code editor**, also known as an **integrated development environment** (IDE). An IDE or code editor is a software application that helps developers edit and debug code.

Our code editor of choice is [Visual Studio Code](https://code.visualstudio.com), by Microsoft. This is a good free code editor with useful features to help edit and debug code written in most popular programming languages, including Python.

### Files

You will notice that this code repository already contains several files and directories.

- **assignment1.py** - you will write Python code in this file in order to complete the given assignment.
- **README.md** - this file contains instructions written in a relatively easy-to-read formatting notation called Markdown.
- **.gitignore** - a 'hidden' file that instructs the git software not to include certain files when sharing your code with others. This helps you only share the important files. Do not touch this file!
- **requirements.txt** - contains a list of dependencies for this project. Dependencies are any code files written by other people that your code will depend upon in order to run properly. It is common for even simple projects to have many dependencies so developers don't waste time "reinventing the wheel". Do not touch this file!
- **tests/** - a directory containing code that will help you determine whether you have completed the assignment correctly or not... more on this later. Do not touch this directory!

## What to do now

Before you can work on the assignment, you will need to perform a few setup tasks.

1. Open this repository directory up in your code editor, Visual Studio Code using the `File` -> `Open...` menu.
2. Click the `View` -> `Terminal` menu. This will pop open a Terminal panel in the editor.
3. In the Terminal panel, type the three commands below suitable for your operating system.

For Mac/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

For Windows:

```bash
py -m venv env
.\.venv\Scripts\activate
pip install -r requirements.txt
```

These commands create and initalize a Python "virtual environment" - an isolated area of computer memory and hard drive space where you can install and run programs without affecting other code running in other virtual environments. You'll see a directory named `.venv` has been automatically created for this environment. All the dependencies listed in `requirements.txt` are installed into this environment in this directory. Don't touch it!

Now you are ready to modify the code!
