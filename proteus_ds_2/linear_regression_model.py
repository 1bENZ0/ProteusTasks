import numpy as np


class SimpleLinearRegression:
    """
    Простая реализация линейной регрессии с использованием нормального
    уравнения.
    """

    def __init__(self):
        """
        Инициализация модели линейной регрессии.
        """
        self.weights = None
        self.bias = None

    def fit(self, x, y):
        """
        Обучение линейной регрессионной модели на исходных данных.

        Параметры:\n
        - x (array-like): Входные признаки.
        - y (array-like): Целевые значения.

        Возвращает:\n
        None
        """
        try:
            # Создание матрицы признаков
            feature_matrix = np.column_stack((np.ones(len(x)), x))

            # Расчет коэффициентов с использованием нормального уравнения
            self.weights = (np.linalg.inv(feature_matrix.T @ feature_matrix)
                            @ feature_matrix.T @ y)

            # Извлечение смещения и коэффициентов
            self.bias = self.weights[0]
            self.weights = self.weights[1:]

        except Exception as e:
            raise Exception(f"Ошибка во время обучения модели: {e}")

    def predict(self, x):
        """
        Вычисление прогноза с помощью обученной модели.

        Параметры:\n
        - x (array-like): Входные признаки для предсказания.

        Возвращает:\n
        array-like: Предсказанные значения.
        """
        try:
            # Расчет прогноза с использованием обученных коэффициентов
            predictions = self.bias + x @ self.weights
            return predictions

        except Exception as e:
            raise Exception(f"Ошибка во время расчета прогноза: {e}")
