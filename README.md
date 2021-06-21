![banner](/resources/banner.png)

<p align="center">
	<a href="https://www.python.org/downloads/release/python-360/">
   		<img alt="Python 3.6" src="https://img.shields.io/badge/Python-3.6+-blue.svg" />
	</a>
		<img alt="Bioinformatics" src="https://img.shields.io/badge/-Bioinformatics-%23008080" />
	<a href="https://sonarcloud.io/dashboard?id=olegbrz_ALTEMO">
		<img alt="Quality Gate Status" src="https://sonarcloud.io/api/project_badges/measure?project=olegbrz_ALTEMO&metric=alert_status">
	</a>
	<a href="https://sonarcloud.io/dashboard?id=olegbrz_ALTEMO">
     	<img alt="Code Smells" src="https://sonarcloud.io/api/project_badges/measure?project=olegbrz_ALTEMO&metric=code_smells" />
	</a>
	<a href="https://sonarcloud.io/dashboard?id=olegbrz_ALTEMO">
     	<img alt="Lines of code" src="https://sonarcloud.io/api/project_badges/measure?project=olegbrz_ALTEMO&metric=ncloc" />
	</a>
</p>

ALTEMO is a package of functions written in Python for bioinformatics proposed as a final project in the course of Algorithmic Techniques and Models (325) at the University of Málaga.

ALTEMO stands for **AL**gorithmic **TE**chniques and **MO**dels.

## Guide

### Cloning the repository

In order to run the program you will first need to download it, this can be done from GitHub using git:

```bash
PS D:\Code> git clone https://github.com/olegbrz/ALTEMO.git
```

This will download the project to the "ALTEMO" folder in the working directory.

### Python

The next requirement to use the suite is to have Python 3.6 or higher. This can be downloaded from the [official website](https://www.python.org/downloads/).

### Entorno virtual}

To work with the project, it is recommended to create a virtual environment where the necessary dependencies will be downloaded without interfering with the global installation.

To create a virtual environment, you can use Anaconda or similar, or simply `venv` that comes integrated with Python:

```bash
PS D:\Code\ALTEMO> python -m venv .env
```

This command will create the `.env` folder in which a Python virtual environment will be installed. Note that the name of the virtual environment can be different.

To activate the virtual environment:

```bash
PS D:/Code/ALTEMO> ./.env/Scripts/Activate.ps1
```

This script is to be activated in Microsoft Powershell, if you use another console or operating system, see the other scripts in the folder `./.env/Scripts`.

If everything is correct, the console should look like this (with the name of the environment at the beggining):

```bash
PS D:/Code/ALTEMO> ./.env/Scripts/Activate.ps1
(.env) PS D:/Code/ALTEMO>
```

### Instalando dependencias

With the virtual environment activated, you can proceed to install the dependencies with the integrated Python package manager, `pip`. The exact dependencies are stored in the `requirements.txt` file stored in the root of the project. To install them all automatically:

```bash
(.env) PS D:\Code\ALTEMO> pip install -r requirements.txt
```

With all of the above, the environment is ready to run the programs.
