# Anomalies detector

This is a simple Python application for detect anomalies in provided data.

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.11
- Required Python packages (install using `pip install -r requirements.txt`)

### Installing

1. Clone the repository:

    ```bash
    git clone https://github.com/1bENZ0/ProteusTasks -b task_2.2
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
Run the main script `main.py` with the path to your data file and optionally specify two parameters:

```bash
python main.py path/to/your/data_file.csv --window_size <Window size for rolling average (default: 500, type: int)> --threshold_factor <Multiplier for threshold(default: 0.01, type: float)> 
```

Example:

```bash
python main.py data/sample_data.csv --window_size 1000 --threshold 0.1 
```
