import numpy as np
from sklearn.preprocessing import StandardScaler


class PolynomialRegression:
    """
    Realization of polynomial regression using ridge regularization
    """

    def __init__(self, degree, alpha=0.1):
        """
        Initialization of the polynomial regression model.

        Parameters
        ----------
        degree : int
            The degree of the polynomial.
        alpha : float
            Regularization parameter.
        """
        self.degree = degree
        self.alpha = alpha
        self.weights = None
        # Standardizer for data scaling
        self.scaler = StandardScaler()

    def fit(self, x, y):
        """
        Training a polynomial model on the data.

        Parameters
        ----------
        x : numpy.ndarray[int]
            Features.
        y : numpy.ndarray[float]
            Targets.

        Returns
        -------
        None
        """
        try:
            # Input data scaling
            x_scaled = self.scaler.fit_transform(x)
            # Conversion to polynomial features
            x_poly = self._polynomial_features(x_scaled)
            # Calculation of model coefficients using regularization
            self.weights = np.linalg.inv(
                x_poly.T @ x_poly + self.alpha * np.identity(
                    x_poly.shape[1])) @ x_poly.T @ y
        except Exception as e:
            raise Exception(f"Error during model training: {e}")

    def predict(self, x):
        """
        Computing the prediction using the trained model.

        Parameters
        ----------
        x : numpy.ndarray[int]
            Targets.

        Returns
        -------
        numpy.ndarray[float]
            Prediction.
        """
        try:
            # Input data scaling
            x_scaled = self.scaler.transform(x)
            # Conversion to polynomial features
            x_poly = self._polynomial_features(x_scaled)
            # Calculating forecast with using the calculated coefficients
            return x_poly @ self.weights
        except Exception as e:
            raise Exception(f"Error during forecast calculation: {e}")

    def _polynomial_features(self, x):
        """
        Polynomial feature generation.

        Parameters
        ----------
        x : numpy.ndarray[int]
            Features.

        Returns
        -------
        numpy.ndarray[float]
        """
        try:
            # Initialization of polynomial features
            x_poly = np.ones((len(x), 1))
            # Addition of polynomial features depending on degree
            for d in range(1, self.degree + 1):
                x_poly = np.column_stack((x_poly, x ** d))
            return x_poly
        except Exception as e:
            raise Exception(
                f"Error during the calculation of polynomial features: {e}")
