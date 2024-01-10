def plot_graphs(ax, canvas, figure, df_cleaned, y_pred_poly, degree_value,
                plot_params):
    ax.clear()
    ax.plot(df_cleaned['Time'], df_cleaned['Value'],
            label='After Outlier Removal', **plot_params)
    ax.set_title('Distribution of values over time (After Outlier Removal)')
    ax.set_xlabel('Time')
    ax.set_ylabel('Value')
    ax.legend()

    # Plot Polynomial Regression
    ax.plot(df_cleaned['Time'], y_pred_poly,
            label=f'Polynomial Regression (Degree {degree_value})',
            linestyle='solid', color='#1F77B4', linewidth=3)

    ax.set_ylim(min(df_cleaned['Value']), 200)
    figure.tight_layout()
    canvas.draw()
