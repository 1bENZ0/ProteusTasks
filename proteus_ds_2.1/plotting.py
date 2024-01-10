import matplotlib.pyplot as plt


def plot_before_after_outlier_removal(df, df_cleaned, plot_params):
    """
    Plotting the graph before and after outliers removal.

    Parameters
    ----------
    df : pandas.Dataframe[float, int]
        Initial data.
    df_cleaned : pandas.Dataframe[float, int]
        Data without outliers.
    plot_params : dict
        Plot parameters

    Returns
    -------
    None
    """
    try:
        plt.figure(figsize=(10, 6))
        plt.subplot(2, 1, 1)
        plt.plot(df['Time'], df['Value'], label='Before Outliers Removal',
                 **plot_params)
        plt.title('Distribution of values over time (Before Outlier Removal)')
        plt.xlabel('Time')
        plt.ylabel('Value')
        plt.legend()

        plt.subplot(2, 1, 2)
        plt.plot(df_cleaned['Time'], df_cleaned['Value'],
                 label='After Outlier Removal', **plot_params)
        plt.title('Distribution of values over time (After Outlier Removal)')
        plt.xlabel('Time')
        plt.ylabel('Value')
        plt.legend()
        plt.ylim(min(df['Value']), max(df['Value']))
        plt.tight_layout()
        plt.show()
    except Exception as e:
        raise Exception(
            f"An error occurred while plotting the outliers graph: {e}")



def plot_polynomial_regression(df_cleaned, y_pred_poly,
                               degree, plot_params):
    """
    Construct a polynomial regression plot based on outlier-free data.

    Parameters
    ----------
    df_cleaned : pandas.Dataframe[float, int]
        Data without outliers.
    y_pred_poly : numpy.ndarray[float[
        Predicted values.
    degree : int
        The degree of the polynomial.
    plot_params : int
        Parameters to customize the graph.

    Returns
    -------
    None
    """
    try:
        plt.figure(figsize=(10, 6))
        plt.plot(df_cleaned['Time'], df_cleaned['Value'],
                 label='After Outlier Removal', **plot_params)
        plt.plot(df_cleaned['Time'], y_pred_poly,
                 label=f'Polynomial Regression (Degree {degree})',
                 linestyle='solid', color='#1F77B4', linewidth=3)
        plt.title(
            'Distribution of values over time (After Outlier Removal) with Polynomial Regression')
        plt.xlabel('Time')
        plt.ylabel('Value')
        plt.legend()
        plt.ylim(min(df_cleaned['Value']), 200)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        raise Exception(
            f"An error occurred while plotting the polynomial regression graph: {e}")
