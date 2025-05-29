# TDD / BDD Practice Code

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.9](https://img.shields.io/badge/Python-3.9-green.svg)](https://shields.io/)

This repository contains the practice code for the labs in **IBM-CD0241EN-SkillsNetwork Introduction to Test Driven Development**

## Contents

### TDD Labs

- Lab 01: Running Test with Nose
- Lab 02: Writing Test Assertions
- Lab 03: Creating an Initial State Using Text Fixtures
- Lab 04: Running Test Cases with Coverage
- Lab 05: Using Factories and Fakes
- Lab 06: Mocking Objects
- Lab 07: Practicing TDD

### BDD Labs

- Lab 08: Environment setup
- Lab 09: Writing feature file
- Lab 10: Loading test data
- Lab 11: Generating steps
- Lab 12: Implementing steps
- Lab 13: Variable substitution

## Development Environment

These labs are designed to be executed in the IBM Developer Skills Network Cloud IDE environment, however you can work on them locally using Docker and Visual Studio Code with the Remote Containers extension to provide a consistent repeatable disposable development environment for all of the labs in this course.

You will need the following software installed:

- [Docker Desktop](https://www.docker.com/products/docker-desktop)
- [Visual Studio Code](https://code.visualstudio.com)
- [Remote Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension from the Visual Studio Marketplace

All of these can be installed manually by clicking on the links above or you can use a package manager like **Homebrew** on Mac of **Chocolatey** on Windows.

### Using Remote Containers

To bring up the development environment you should clone this repo, change into the repo directory, and then open Visual Studio Code using the `code .` command. VS Code will prompt you to reopen in a container and you should say **yes**. This will take a while as it builds the Docker image and creates a container from it to develop in.

```bash
git clone https://github.com/ibm-developer-skills-network/duwjx-tdd_bdd_PracticeCode.git
cd duwjx-tdd_bdd_PracticeCode
code .
```

Note that there is a period `.` after the `code` command. This tells Visual Studio Code to open the editor and load the current folder of files. When prompted to **Reopen in Container** select that option and it will build a development for you inside a Docker container.

Once the environment is loaded you should be placed at a `bash` prompt in the `/app` folder inside of the development container. This folder is mounted to the current working directory of your repository on your computer. This means that any file you edit while inside of the `/app` folder in the container is actually being edited on your computer. You can then commit your changes to `git` from either inside or outside of the container.

For the **BDD Labs** you will need to run the following commands to create the proper development environment:

```bash
bash bin/setup.sh
```

Then exit that terminal and open a new one to activate the virtual environment.

## Author

[John Rofrano](https://www.linkedin.com/in/JohnRofrano/), Senior Technical Staff Member, DevOps Champion, @ IBM Research

## <h3 align="center"> © IBM Corporation 2022, 2023. All rights reserved. <h3/>
