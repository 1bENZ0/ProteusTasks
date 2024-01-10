from sklearn.metrics import mean_squared_error

from argument_parse import parse_arguments, load_data
from plotting import plot_before_after_outlier_removal, \
    plot_polynomial_regression
from polynomial_regression_model import PolynomialRegression
from z_score_outlier_removal import z_score_remove


def main():
    """
    Main function.

    Returns
    -------
    None
    """
    try:
        args = parse_arguments()

        df = load_data(args.data_file)

        plot_params = dict(
            linestyle="-",
            marker=".",
            markeredgecolor="0.25",
            markerfacecolor="0.25"
        )

        df_cleaned = z_score_remove(df, threshold=args.threshold)

        x = df_cleaned.loc[:, ['Time']].values
        y = df_cleaned.loc[:, 'Value'].values

        poly_model = PolynomialRegression(degree=args.degree, alpha=args.alpha)
        poly_model.fit(x, y)
        y_pred_poly = poly_model.predict(x)

        mse_poly = mean_squared_error(y, y_pred_poly)
        print(f'Mean Squared Error: {mse_poly}')

        plot_before_after_outlier_removal(df, df_cleaned, plot_params)
        plot_polynomial_regression(df_cleaned, y_pred_poly, args.degree,
                                   plot_params)
    except Exception as e:
        raise Exception(f"Error occurred: {e}")


if __name__ == '__main__':
    main()
