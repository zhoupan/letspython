# letspython

[![Release](https://img.shields.io/github/v/release/zhoupan/letspython)](https://img.shields.io/github/v/release/zhoupan/letspython)
[![Build status](https://img.shields.io/github/actions/workflow/status/zhoupan/letspython/main.yml?branch=main)](https://github.com/zhoupan/letspython/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/zhoupan/letspython/branch/main/graph/badge.svg)](https://codecov.io/gh/zhoupan/letspython)
[![Commit activity](https://img.shields.io/github/commit-activity/m/zhoupan/letspython)](https://img.shields.io/github/commit-activity/m/zhoupan/letspython)
[![License](https://img.shields.io/github/license/zhoupan/letspython)](https://img.shields.io/github/license/zhoupan/letspython)

Let's Python.

- **Github repository**: <https://github.com/zhoupan/letspython/>
- **Documentation** <https://zhoupan.github.io/letspython/>

## Python

### Here are the steps to install Python on Windows:

1. Download the installation file: Go to the Python website (https://www.python.org/downloads/windows/) and download the latest version of Python that is appropriate for your version of Windows.

2. Run the installation file: Locate the downloaded installation file and double-click on it to run the installer.

3. Select installation options: During the installation process, select the options you want, such as the location of the installation and add Python to your system PATH.

4. Finish installation: Once you have selected your options, click the "Install" button to complete the installation process.

5. Verify installation: After completing the installation process, open the Command Prompt or Anaconda Prompt and type `python --version` to verify that Python is installed correctly and that you have the correct version.

### Here are the steps to install Python on macOS:

1. Download the installation file: Go to the Python website (https://www.python.org/downloads/mac-osx/) and download the latest version of Python that is appropriate for your version of macOS.

2. Run the installation file: Open the downloaded file and double-click on the installation package.

3. Follow the instructions: Follow the installation instructions in the installation package. By default, the installer will install Python into `/usr/local/bin`.

4. Verify installation: After completing the installation process, open the Terminal and type `python --version` to verify that Python is installed correctly and that you have the correct version.

### Here are the steps to install Python on Linux:

1. Check if Python is installed: Open the Terminal and type `python --version` to check if Python is installed. If it returns `command not found`, then you need to install Python.

2. Install Python: Open the Terminal and type one of the following commands, depending on your Linux distribution:

- Debian, Ubuntu, or other Debian-based distributions: `sudo apt install python3`
- Red Hat, CentOS, or other Red Hat-based distributions: `sudo yum install python3`

3. Verify installation: After completing the installation process, open the Terminal and type `python3 --version` to verify that Python is installed correctly and that you have the correct version.

- [Download](https://www.python.org/downloads)
- [pyenv-win](https://github.com/pyenv-win/pyenv-win)
- [pyenv](https://github.com/pyenv/pyenv)

## Poetry

Poetry supports multiple installation methods, including a simple script found at [install.python-poetry.org](https://install.python-poetry.org). For full
installation instructions, including advanced usage of the script, alternate install methods, and CI best practices, see
the full [installation documentation](https://python-poetry.org/docs/#installation).

## Git

Here are the steps to install Git on different operating systems:

**Windows:**

1. Download the Git installer from the official Git website (https://git-scm.com/download/win).
2. Run the installer and follow the setup wizard.
3. Choose the installation directory and select the components to be installed.
4. Choose the default editor and terminal emulator.
5. Choose the default path environment for Git.
6. Choose the HTTPS transport backend and configure your console window options.
7. Choose whether to enable the credential helper.
8. Complete the installation.

**macOS:**

1. Download the Git installer from the official Git website (https://git-scm.com/download/mac).
2. Run the installer and follow the setup wizard.
3. Accept the license agreement and choose the installation location.
4. Choose the components to be installed.
5. Choose whether to install git in Terminal.
6. Choose the default text editor and merge tool.
7. Choose the path environment for the Git installation.
8. Complete the installation.

**Linux:**

For Debian-based Linux distributions like Ubuntu, use the following command in the terminal:

```
sudo apt-get update
sudo apt-get install git
```

For RedHat-based Linux distributions like Fedora, use the following command in the terminal:

```
sudo yum install git
```

For openSUSE-based Linux distributions, use the following command in the terminal:

```
sudo zypper install git
```

For Arch Linux, use the following command in the terminal:

```
sudo pacman -S git
```

After installing Git, open the command prompt, terminal, or Git Bash and type `git --version` to verify that Git has been installed correctly.

## GitHub Desktop

Here are the steps to install GitHub Desktop on Windows or macOS:

**Windows:**

1. Download the latest version of GitHub Desktop from the official GitHub website (https://desktop.github.com/).
2. Double-click the downloaded setup file to start the installation. If prompted, grant administrative access for the installer.
3. Select the installation options such as the installation directory and shortcuts.
4. Click Install to begin the installation process.
5. Once the installation is completed, you can open GitHub Desktop and sign in with your GitHub account.

**macOS:**

1. Download the latest version of GitHub Desktop from the official GitHub website (https://desktop.github.com/).
2. Double-click the downloaded dmg file to mount it.
3. Drag the GitHub Desktop icon to the Applications folder.
4. Open the Applications folder and double-click the GitHub Desktop app to run it.
5. If you see a warning about an unidentified developer, right-click on the app icon and choose Open to confirm that you want to open it.
6. Follow the prompts to complete the installation and sign in with your GitHub account.

After completing the installation and signing in to your GitHub account, you can start using GitHub Desktop. With GitHub Desktop, you can clone repositories, create branches, commit changes, and perform other Git-related tasks using a visual interface.

## Clone a GitHub project with command line

To clone a GitHub project, follow these steps:

1. Open the GitHub website in your web browser and navigate to the repository you want to clone.
2. Click on the "Code" button (green button) located on the right side of the screen. This will reveal a dropdown menu.
3. In the dropdown menu, select "HTTPS" or "SSH", depending on your preferences.
4. Click on the copy icon next to the URL to copy the repository's URL to your clipboard.
5. Open a terminal or command prompt on your local machine.
6. Navigate to the directory where you want to clone the repository.
7. Type `git clone`, paste the URL you copied in step 4, and press Enter.

For example, if you want to clone a repository with the HTTPS URL https://github.com/myusername/myrepository.git into a directory called "myproject" in your home directory on Linux or macOS, you would type the following command:

```
cd ~
git clone https://github.com/myusername/myrepository.git myproject
```

This will create a local copy of the repository in the "myproject" directory on your machine. Once you have cloned the repository, you can make changes to the code, commit them, and push them back to the remote repository.

## Clone a GitHub project with GitHub Desktop

To clone a GitHub project with GitHub Desktop, follow these steps:

1. Open GitHub Desktop.
2. Click on the "File" menu at the top left corner of the screen.
3. Click on "Clone Repository".
4. In the "URL" field, paste the URL of the GitHub repository you want to clone.
5. Choose the local path where the repository should be cloned to.
6. Click on "Clone" to start the cloning process.

Once the cloning process is completed, the repository will be available in your local directory and you can start working on it. If you want to update the local repository from the remote repository, you can use the "Fetch origin" button in the "Changes" view of the repository in GitHub Desktop. If you want to push your local changes to the remote repository, you can use the "Push origin" button.

## Visual Studio Code

Here are the steps to install Visual Studio Code (VS Code) on Windows, macOS, and Linux:

**Windows:**

1. Download the Visual Studio Code installer from the official website: https://code.visualstudio.com/.
2. Run the downloaded executable file.
3. When prompted, choose your preferred language and click "OK".
4. Review the license agreement, select "I Accept the Agreement", and click "Next".
5. Choose the destination folder for the installation and click "Next".
6. Choose the additional tasks you would like the installer to perform, or leave the defaults selected, and click "Next".
7. Choose the start menu folder and whether to create desktop and Quick Launch icons, and click "Next".
8. Click "Install" to start the installation process.
9. Once the installation is completed, click "Finish" to exit the installer.

**macOS:**

1. Download the Visual Studio Code installer for macOS from the official website: https://code.visualstudio.com/.
2. Double-click the downloaded .dmg installer file.
3. Drag the VS Code icon to the Applications folder.
4. Open VS Code from the Applications folder.
5. When prompted, click "Open" to confirm you want to open the app.
6. If you encounter any security warnings during the installation process, follow the instructions on the screen.

**Linux:**

Here are the steps to install Visual Studio Code on Ubuntu:

1. Download the Visual Studio Code package from the official website for Linux (https://code.visualstudio.com/)
2. Open the terminal and navigate to the Downloads directory.
3. Extract the downloaded file by running this command:

```
tar -xzf <file name>
```

4. Move the extracted folder to the opt directory:

```
sudo mv <folder name> /opt
```

5. Create a symbolic link

```
sudo ln -s /opt/<folder name>/Code /usr/bin/code
```

6. Finally, launch VS Code by running "code" command from the terminal.

After installing VS Code, you can launch it and begin using it for your programming tasks.

## Creating virtual environment

```bash
poetry install
```

> Creating virtual environment.
> Reads the pyproject.toml file from the current project, resolves the dependencies, and installs them.
> If there is a poetry.lock file in the current directory, it will use the exact versions from there instead of resolving them. This ensures that everyone using the library will get the same versions of the dependencies.
> If there is no poetry.lock file, Poetry will create one after dependency resolution.

## Activate or deactivate virtual environment

To activate a virtual environment:

- On Linux/macOS, open a terminal and navigate to the project directory where you created the virtual environment. Use the command `source .venv/bin/activate` to activate the virtual environment.
- On Windows, open a command prompt and navigate to the project directory where you created the virtual environment. Use the command `.venv\Scripts\activate` to activate the virtual environment.

You should see the name of the virtual environment in the command prompt or terminal window. This indicates that the virtual environment has been activated successfully.

To deactivate the virtual environment, simply use the command `deactivate` in the terminal or command prompt. This will switch to the global Python environment or another activated virtual environment. Again, you should see a change in the command prompt or terminal window indicating that the virtual environment has been deactivated.

## Resources

- [cookiecutter-poetry](https://github.com/fpgmaas/cookiecutter-poetry): A modern cookiecutter template for Python projects that use Poetry for dependency management.
- [poetry](https://github.com/python-poetry/poetry): Python packaging and dependency management made easy.
- [pypi](https://pypi.org/): Find, install and publish Python packages with the Python Package Index.
- [pytest](https://docs.pytest.org): The pytest framework makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries.
- [mypy](https://www.mypy-lang.org/): Mypy is an optional static type checker for Python that aims to combine the benefits of dynamic (or "duck") typing and static typing. Mypy combines the expressive power and convenience of Python with a powerful type system and compile-time type checking. Mypy type checks standard Python programs; run them using any Python VM with basically no runtime overhead.
- [ruff](https://github.com/astral-sh/ruff): An extremely fast Python linter and code formatter, written in Rust.
- [MkDocs](https://www.mkdocs.org/): Project documentation with Markdown.
- [tox](https://tox.wiki/en/latest/): tox aims to automate and standardize testing in Python. It is part of a larger vision of easing the packaging, testing and release process of Python software.
- [EditorConfig](https://editorconfig.org/): EditorConfig helps maintain consistent coding styles for multiple developers working on the same project across various editors and IDEs. The EditorConfig project consists of a file format for defining coding styles and a collection of text editor plugins that enable editors to read the file format and adhere to defined styles. EditorConfig files are easily readable and they work nicely with version control systems.
- [nodejs](https://nodejs.org/en/download/): Node.js is an open-source and cross-platform JavaScript runtime environment. It is a popular tool for almost any kind of project!
- [pnpm](https://pnpm.io/): Fast, disk space efficient package manager.
- [Prettier](https://prettier.io/): Prettier is an opinionated code formatter.
