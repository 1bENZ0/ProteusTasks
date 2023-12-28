import matplotlib.pyplot as plt


def plot_results(df, y_predicted, plot_params):
    """
    Построение графика фактических и предсказанных значений.

    Параметры:\n
    - df (pandas.DataFrame): Датафрейм содержащий колонки 'Time' и 'Value'.
    - y_predicted (numpy.ndarray): Предсказанные значения.
    - plot_params (dict): Параметры для отрисовки графика.
    """
    try:
        ax = df['Value'].plot(**plot_params)
        ax.plot(df.index, y_predicted, label='Predicted value by model',
                linewidth=3)
        ax.set_title('Distribution of values over time')
        ax.legend()
        plt.show()
    except Exception as e:
        raise Exception(f"Ошибка во время построения графика: {e}")
