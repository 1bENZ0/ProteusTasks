import argparse

import numpy as np
import pandas as pd


def parse_arguments():
    """
    Handling arguments from the command line.5

    Returns
    -------
    None
    """
    try:
        parser = argparse.ArgumentParser(
            description='Polynomial regression model')
        parser.add_argument('data_file', help='Path to the data file')
        parser.add_argument('--degree', type=int, default=4,
                            help='Degree of the polynomial regression (default: 4)')
        parser.add_argument('--threshold', type=float, default=1.2,
                            help='Threshold for outlier removal (default: 1.2)')
        parser.add_argument('--alpha', type=float, default=0.1,
                            help='Regularization parameter for polynomial regression (default: 0.1)')
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
