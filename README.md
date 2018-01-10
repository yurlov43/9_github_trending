# Github Trends

The program looks for twenty repositories with the largest number of stars created in the last week.

# How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.

# Quickstart

Example of script launch on Linux and Windows, Python 3.5:

```bash
$ python github_trending.py
```

The program displays a list of repositories in the console:

```bash
1.      Name: meltdown-exploit
        Url: https://github.com/paboldin/meltdown-exploit
        Amount issues: 9


2.      Name: spectre-meltdown-checker
        Url: https://github.com/speed47/spectre-meltdown-checker
        Amount issues: 6
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
