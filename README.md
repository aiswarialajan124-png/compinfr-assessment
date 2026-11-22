# Assessment Submission for Computer Infrastructure

This repository contains my submission for the module Computer Infrastructure.
The project is written in a single Jupyter notebook, in Python.
Everything needed to run the notebook is included in this repository.

## Quick look 

- You can click on [problems.ipynb](problems.ipynb) in this repository and GitHub will display it in static format.
- You can view the notebook in [Google Collab](https://colab.research.google.com/github/aiswarialajan124-png/compinfr-assessment/blob/main/problems.ipynb).
- You can view the notebook using [nbviewer](https://nbviewer.org/github/aiswarialajan124-png/compinfr-assessment/blob/main/problems.ipynb) also.

## Running the Notebook
 
In order to run `problems.ipynb` you can follow these steps:

1. Clone the repository using [git](https://git-scm.com/):

```
git clone https://github.com/aiswarialajan124-png/compinfr-assessment.git
cd cominfr-assessment
```

2. Ensure you have [Python](https://www.python.org/) installed. An easy way to get Python is to use [uv](https://docs.astral.sh/uv/) or [Anaconda](https://anaconda.org/).

3. Install the dependancies:

```
pip install -r requirements.txt
```

4. Open the notebook:

```
jupyter notebook problems.ipynb
```

## Running the script
`stocks.py` downloads the latest hourly data, saves it in `data/` and saves a plot in `plots.`. After installing the dependencies (steps 1 to 3 above), run it from the root of the repository.

On Linux or macOS:

```
./stocks.py
```

On Windows, which does not use shebang lines:

```
python stocks.py
```

Each run adds one new timestamped CSV file to `data/` and one matching PNG file to `plots/`.

## Automated runs
The workflow in `.github/workflows/stocks.yml` runs `stocks.py` on GitHub every Wednesday at 08:00 UTC. It can also be started by hand from the Actions tab of the repository using "Run workflow". The files it creates exist only on the temporary runner and are not saved back to the repository.

## Repository structure
- `problems.ipynb`: the notebook containing all the problems and explanations.
- `requirements.txt`: the Python packages needed to run the notebook.
- `data/`: downloaded stock market data, saved as CSV files named `YYYYMMDD-HHmmss.csv`using the time of the download.
- `plots/`: plots created from the data, saved as PNG files using the same naming format.
- `stocks.py`: an executable script that downloads the latest data and creates the plot (see "Running the script" below).
- `.github/workflows/stocks.yml`: a GitHub Actions workflow that runs `stocks.py` every Wednesday at 08:00 UTC.

## Dependancies

The packages are listed in `requirements.txt`:

- [yfinance](https://github.com/ranaroussi/yfinance): downloads the stock market data.
- [pandas](https://pandas.pydata.org/): reads the data and calculates percentage change.
- [matplotlib](https://matplotlib.org/):plots the data
- [numpy](https://numpy.org/): numerical arrays.
- [notebook](https://jupyter.org/) and [ipykernel](https://ipython.readthedocs.io/en/stable/): run the Jupyter notebook.

## About the notebook 
This notebook works through four problems based on hourly stock market data for NVIDIA, Broadcom, Arm, AMD and IBM:

1. Downloading the data with `yfinance` and saving it to `data/`.
2. Plotting the percentage change of the closing prices and saving the plot to `plots/`.
3. Creating an executable script, `stocks.py`.
4. Automating the script with GitHub Actions.

## About the Author
I am a student in Higher Diploma in Science in Computing in Data Analytics.