import tkinter as tk
from tkinter import ttk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn.metrics import mean_squared_error

from argument_parse import parse_arguments, load_data
from plotting_gui import plot_graphs
from polynomial_regression_model import PolynomialRegression
from z_score_outlier_removal import z_score_remove


class PolynomialRegressionGUI:
    """
    Class implementing GUI.
    """

    def __init__(self, root):
        """
        Initializes the PolynomialRegressionGUI object.

        Parameters
        ----------
        root : tkinter.Tk
            The main Tkinter window
        """
        try:
            self.root = root
            self.root.title("Outliers removal and polynomial regression GUI")

            # Initialize parameters
            self.degree = tk.IntVar(value=4)
            self.threshold = tk.DoubleVar(value=1.2)
            self.alpha = tk.DoubleVar(value=0.1)

            # Initialize data statistics
            self.initial_data_count = len(df.index)
            self.updated_data_count = self.initial_data_count
            self.mse_value = tk.DoubleVar(value=0.0)

            # Create GUI elements
            self.create_widgets()
        except Exception as e:
            raise Exception(F"Error detected:{e}")

    def update_labels(self, *args):
        """
        Update the labels displaying the current values of threshold and degree.

        Parameters
        ----------
        args : tuple
            Variable number of arguments.

        Returns
        -------
        None
        """
        try:
            # Update Threshold Label
            threshold_value = self.threshold.get()
            formatted_threshold = f"{threshold_value:.2f}"
            self.threshold_value_var.set(float(formatted_threshold))

            # Update Degree Label
            self.degree_value_var.set(self.degree.get())
        except Exception as e:
            raise Exception(F"Error detected:{e}")

    def create_widgets(self):
        """
        Create and layout GUI elements.

        Returns
        -------
        None
        """
        try:
            # Threshold Slider
            threshold_label = ttk.Label(self.root, text="Threshold:")
            threshold_slider = ttk.Scale(self.root, from_=0.1, to=6,
                                         orient="horizontal",
                                         variable=self.threshold, length=100)
            threshold_slider.set(self.threshold.get())
            threshold_slider.bind("<Motion>", self.update_plots)

            # Degree Slider
            degree_label = ttk.Label(self.root, text="Degree:")
            degree_slider = ttk.Scale(self.root, from_=1, to=10,
                                      orient="horizontal",
                                      variable=self.degree,
                                      length=100)
            degree_slider.set(self.degree.get())
            degree_slider.bind("<Motion>", self.update_plots)

            # Matplotlib Figure
            self.figure, self.ax = plt.subplots(figsize=(8, 5))
            self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
            self.canvas_widget = self.canvas.get_tk_widget()

            # Data Statistics Labels
            stats_label = ttk.Label(self.root, text="Data Statistics:")
            initial_data_label = ttk.Label(self.root,
                                           text="Data before outliers remove:")
            updated_data_label = ttk.Label(self.root,
                                           text="Data after outliers remove:")
            mse_label = ttk.Label(self.root, text="Mean Squared Error:")

            self.initial_data_var = tk.StringVar(value=self.initial_data_count)
            self.updated_data_var = tk.StringVar(value=self.updated_data_count)
            self.mse_var = tk.DoubleVar(value=0.0)
            self.threshold_value_var = tk.DoubleVar(value=self.threshold.get())
            self.degree_value_var = tk.IntVar(value=self.degree.get())

            initial_data_count_label = ttk.Label(self.root,
                                                 textvariable=self.initial_data_var)
            updated_data_count_label = ttk.Label(self.root,
                                                 textvariable=self.updated_data_var)
            mse_value_label = ttk.Label(self.root, textvariable=self.mse_var)
            threshold_value_label = ttk.Label(self.root,
                                              textvariable=self.threshold_value_var)
            degree_value_label = ttk.Label(self.root,
                                           textvariable=self.degree_value_var)

            # Layout
            threshold_label.grid(row=0, column=0, padx=(10, 5), pady=5,
                                 sticky="w")
            threshold_slider.grid(row=0, column=0, padx=(5, 5), pady=5)
            threshold_value_label.grid(row=0, column=0, padx=(70, 10), pady=5,
                                       sticky="w")

            degree_label.grid(row=1, column=0, padx=(10, 5), pady=5,
                              sticky="w")
            degree_slider.grid(row=1, column=0, padx=(5, 5), pady=5)
            degree_value_label.grid(row=1, column=0, padx=(70, 10), pady=5,
                                    sticky="w")

            self.canvas_widget.grid(row=2, column=0, columnspan=3, pady=10)

            stats_label.grid(row=3, column=0, columnspan=2, padx=(10, 5),
                             pady=10,
                             sticky="w")

            initial_data_label.grid(row=4, column=0, padx=(10, 5), pady=5,
                                    sticky="w")
            initial_data_count_label.grid(row=4, column=1, padx=(10, 5),
                                          pady=5,
                                          sticky="w")

            updated_data_label.grid(row=5, column=0, padx=(10, 5), pady=5,
                                    sticky="w")
            updated_data_count_label.grid(row=5, column=1, padx=(10, 5),
                                          pady=5,
                                          sticky="w")

            mse_label.grid(row=6, column=0, pady=5, padx=(10, 5), sticky="w")
            mse_value_label.grid(row=6, column=1, pady=5, padx=(10, 5),
                                 sticky="w")

            # Bindings for dynamic updates
            self.threshold.trace_add('write', self.update_labels)
            self.degree.trace_add('write', self.update_labels)

            # Initialize Plots
            self.update_plots()
        except Exception as e:
            raise Exception(F"Error detected:{e}")

    def update_plots(self, event=None):
        """
        Update the plots based on the current parameter values.

        Parameters
        ----------
        event : Event, optional
        Event triggering the update, by default None.

        Returns
        -------
        None
        """
        try:
            # Get current parameter values
            threshold_value = self.threshold.get()
            degree_value = self.degree.get()

            # Remove outliers based on threshold
            df_cleaned = z_score_remove(df, threshold_value)

            # Fit Polynomial Regression
            x = df_cleaned.loc[:, ['Time']].values
            y = df_cleaned.loc[:, 'Value'].values
            poly_model = PolynomialRegression(degree_value)
            poly_model.fit(x, y)
            y_pred_poly = poly_model.predict(x)

            # Plotting
            plot_graphs(self.ax, self.canvas, self.figure, df_cleaned,
                        y_pred_poly,
                        degree_value, plot_params)

            # Update Data Statistics
            self.updated_data_count = len(df_cleaned.index)
            mse_value = mean_squared_error(y, y_pred_poly)
            self.mse_var.set(mse_value)
            self.update_statistics()
        except Exception as e:
            raise Exception(F"Error detected:{e}")

    def update_statistics(self):
        """
        Update cleaned data.

        Returns
        -------
        None
        """
        try:
            self.initial_data_var.set(self.initial_data_count)
            self.updated_data_var.set(self.updated_data_count)
        except Exception as e:
            raise Exception(F"Error detected:{e}")



try:
    args = parse_arguments()
    df = load_data(args.data_file)

    plot_params = dict(
        linestyle="-",
        marker=".",
        markeredgecolor="0.25",
        markerfacecolor="0.25"
    )
    # Create the main window
    root = tk.Tk()
    app = PolynomialRegressionGUI(root)

    def on_closing():
        """
        End compile after closing window.
        Returns
        -------
        None
        """
        try:
            root.quit()
        except Exception as e:
            raise Exception(F"Error detected:{e}")

    root.protocol("WM_DELETE_WINDOW", on_closing)
    # Run the application
    root.mainloop()
except Exception as e:
    raise Exception(F"Error detected:{e}")



