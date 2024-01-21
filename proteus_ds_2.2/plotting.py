import matplotlib.pyplot as plt


def plot_anomalies(df, anomalies_threshold):
    """
    Anomaly graph plotting.

    Parameters
    ----------
    df : pandas.Dataframe[float, int]
        Initial data.

    anomalies_threshold : int
        Threshold for anomaly detection.

    Returns
    -------
    None
    """
    try:

        plt.figure(figsize=(10, 6))
        plt.fill_between(df['Time'], anomalies_threshold, color='red',
                         alpha=0.4, label='Anomalies', zorder=2)
        plt.plot(df['Time'], df['Value'], label='Data', color='grey',
                 zorder=1)
        plt.title(
            'Anomaly Detection using Rolling Mean and Standard Deviation')
        plt.xlabel('Time')
        plt.ylabel('Value')
        plt.ylim(min(df['Value']), max(df['Value']))
        plt.legend()
        plt.show()
    except Exception as e:
        raise Exception(f"An error was detected during plotting: {e}")
