# DevOps-project
Project for course DevOps at FMI 2024-2025
The documentation goes over:
- Overview;
- Plan and structure;
	- Git branching strategy;
	- Continuous integration;
	- Continuous deployment;
	- Project folder structure;
- Implementation details;
- Installation;
	- Start the app;

## Overview
The Random generator is a Flask-based web application that generates and displays a random number between 1 and 1000 whenever the root URL ("/") is accessed.

## Plan and structure

### Git branching strategy
To always have a working latest version of the app I decided to use a *Feature branch* strategy.

- a feature branch is created (for each issue)
- after the feature is completed in the branch, it is merged into the `dev` branch
- after that, the `dev` branch is merged into the `main` branch

The **main** branch (formerly "master") is the primary branch that always contains the latest stable and production-ready version of the application.The **dev** branch serves as the active development branch where new features are integrated and tested before they are considered stable.Developers work on **feature** branches, which are temporary branches created specifically for implementing new features or fixing specific issues. These branches are based on the dev branch.
Once the code in the *dev* branch is completed it is merged with the **main** branch thus becoming the next stable version. 

Feature branches don't require special naming (though they can't be called `dev` or `main`).  
Code can be added to `dev` only via pull requests from feature branches.  	
Code can be added to `main` only via pull requests from `dev`.  

### Continuous integration
Whenever pushing to any branch, the *CI* workflow is executed. This workflow consists of:
 - Flake8			- used to check if the new python code is consistent with the agreed upon styles;
 - EditorConfig     - used to check if the codebase adheres to the formatting and coding style guidelines defined in an .editorconfig file
 - Snyk				- used to identify and warn about existing vulnerabilities in the new code and dependencies, and if such are found, provide a working solution;
 - Bandit           - used to perform static code analysis on Python projects to identify and address security vulnerabilities
 - Unit tests       - used to test the base functionality of the application and if its behavious is as it's expected
 - Trivy			- after all the other actions finish successfully, then Trivy is used to scan the result server docker image for any vulnerabilities and other issues.

### Continuous deployment
Whenever pushing to the **dev** branch, if the *CI* workflow passes successfully, then the *CD* workflow is run.

This workflow is responsible for pushing the docker containers to Dockerhub and testing a deployment of the application, if the push was successful.

The docker image that is pushed is always with the *latest* tag.
Testing the deployment of the app is done by rolling out and then checking if the app was deployed.

### Project folder structure
The hole project is composed of:
 - *src* folder - holding the python code responsible for running the app, as well as the requirements for executing the app;
 - *k8s* folder  - holding the information for the Kubernetes deployment;
 - *.editorconfig* - holding consistent coding styles;
 - *Dockerfile* - holding the docker image file;
 - *README.md* file - the documentation that you are reading *right now*.

## Implementation details
The application is made in Python3, using libraries that come with the language and some that need to be downloaded additionally.
The libraries that come with the language are **unittest**. The libraries that need to be installed from the `requirements.txt` file are **flask** - used for creating the web app.
When accessing the website through the url, the app generates a random nnumber between 1 and 1000 and displays it on the screen. By refreshing, it generates a new number each time. 
In a containerized environment (e.g., Kubernetes, Docker), the app needs to be exposed to the network interfaces managed by the orchestrator.
By setting the *host='0.0.0.0'*, the Flask app listens on all available IPs, enabling the app to be accessible from other containers, nodes, or external systems. 

Additionaly in the `requirements.txt` we have a few dependencies added, conserning the security checks. For convenience, instead of installing them manualy, they were added to the `requirements.txt` so that they can be installed with one command and easily added/removed later on.

## Installation
To start using the app you only need to install the required libraries from the `requirements.txt` file and have `python3`.
If you don't have `python3` installed follow a tutorial to install it on your OS.
To make everything much cleaner, we will start the app in a virtual environment.
First set up the venv:
		
		
		python -m venv myenv

Then start the venv:


		source myenv/bin/activate

After `python3` is installed it's as easy as running:


	pip install -r requirements.txt

If you are using an Arch based Linux distribution installing things with pip gives an error. To fix this issue run this:

	pip install -r requirements.txt --break-system-packages

### Start app:
To startthe app simply run:

	python3 app.py

Afterwards the program should print:
	* Running on all addresses (0.0.0.0)
 	* Running on http://127.0.0.1:5000
 	* Running on http://10.108.7.55:5000
By accessing one of theese two link, u will produce a GET request to the app and on the screen will be displayed your randomly generated number.


