import argparse

import numpy as np
import pandas as pd


def parse_arguments():
    """
    Handling arguments from the command line.

    Returns
    -------
    None
    """
    try:
        parser = argparse.ArgumentParser(
            description='Anomalies detector')
        parser.add_argument('data_file', help='Path to the data file')
        parser.add_argument('--window_size', type=int, default=500,
                            help='Window size for rolling average (default: 500)')
        parser.add_argument('--threshold_factor', type=float, default=0.01,
                            help='Multiplier for threshold (default: 0.01)')
        args = parser.parse_args()
        return args
    except argparse.ArgumentTypeError as e:
        raise Exception(f"An invalid data type has been entered: {e}")
    except Exception as e:
        raise Exception(f"There's been an unforeseen error: {str(e)}")


def load_data(data_file):
    """
    Downloading data into pandas dataframe.

    Parameters
    ----------
    data_file : str
        Path to data file.

    Returns
    -------
    pandas.Dataframe
    """
    try:
        df = pd.read_csv(data_file, names=['Time', 'Value'], index_col='Time')
        df['Time'] = np.arange(len(df.index))
        return df
    except FileNotFoundError:
        raise Exception(f"Error: File '{data_file}' was not found.")
    except pd.errors.EmptyDataError:
        raise Exception(
            f"Error: File '{data_file}' does not contain any data.")
    except Exception as e:
        raise Exception(f"There's been an unforeseen error: {str(e)}")
