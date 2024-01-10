# Polynomial Regression Model 

This is a simple Python application for fitting and visualizing a polynomial regression model using the provided data.

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.11
- Required Python packages (install using `pip install -r requirements.txt`)

### Installing

1. Clone the repository:

    ```bash
    git clone https://github.com/1bENZ0/ProteusTasks -b task_2.1
    ```

2. Change into the project directory:

    ```bash
    cd your-repository
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage
### Command Line Interface
Run the main script `main.py` with the path to your data file and optionally specify three parameters:

```bash
python main.py path/to/your/data_file.csv --degree <polynomial_degree> --threshold <outlier_threshold> --alpha <regularization_parameter>
```

Optional parameters:
--degree: Polynomial degree (default: 4).
--threshold: Threshold to remove outliers (default: 1.2).
--alpha: Regularization parameter (default: 0.1).

Example:

```bash
python main.py data/sample_data.csv --degree 5 --threshold 1.5 --alpha 0.01
```
### Graphical User Interface
Alternatively, you can run the graphical interface using the main_gui.py script:

```bash
python main_gui.py path/to/your/data_file.csv
```
Note: The GUI might experience lag, but it is considered normal.
