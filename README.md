# Jira Plotter

The purpose of this script is to plot exported data from Jira. For now, the file read must be named "jira-export.csv" and the output image will be named "jira-plot.png". 


## Installation

You need [Python](https://www.python.org/downloads/). This script should run with both Python 2 and 3. 

Option 1 (Recommended):

```bash
pip install pipenv # If you don't already have it
pipenv install 
```

Option 2 (Will install packages globally):

```bash
pip install pandas matplotlib
```

## Usage

```bash
# If you used option 1 do this commented line first:
# pipenv shell 
python jira-plotter.py
```


## Issues that may arise

One issue that may arise is an error with Tkinter or not installing Python as a framework. For that you can add the following line in the script:

```python
matplotlib.use("Agg")
```

Between these two lines:

```python
import matplotlib
import matplotlib.pyplot as plt
```