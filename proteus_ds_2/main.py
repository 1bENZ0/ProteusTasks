import argparse

import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error

from linear_regression_model import SimpleLinearRegression
from plotting import plot_results


def main():
    """
    Основная функция для запуска модели линейной регрессии.
    """
    parser = argparse.ArgumentParser(
        description='Simple Linear Regression Model')
    parser.add_argument('data_file', help='Path to the data file')
    args = parser.parse_args()

    try:
        df = pd.read_csv(args.data_file, names=['Time', 'Value'],
                         index_col='Time')
        df['Time'] = np.arange(len(df.index))
        x = df.loc[:, ['Time']]
        y = df.loc[:, 'Value']

        simple_model = SimpleLinearRegression()
        simple_model.fit(x, y)

        y_predicted = simple_model.predict(x)

        mse = mean_squared_error(y, y_predicted)
        print(f'Mean Squared Error: {mse}')

        plot_params = dict(
            color="0.75",
            style=".-",
            markeredgecolor="0.25",
            markerfacecolor="0.25",
            legend=True,
        )

        plot_results(df, y_predicted, plot_params)

    except FileNotFoundError:
        print(f"Ошибка: Файл '{args.data_file}' не найден.")
    except pd.errors.EmptyDataError:
        print(f"Ошибка: Файл '{args.data_file}' не содержит данных.")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {str(e)}")


if __name__ == '__main__':
    main()
