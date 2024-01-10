def detect_anomalies(df, window_size, threshold_factor):
    """
    Determine above which threshold the anomalies are located.
    Parameters
    ----------
    df : pandas.Dataframe[float, int]
        Initial data.
    window_size : int
    threshold_factor : int

    Returns
    -------
    anomalies_threshold : int
        Threshold for anomaly detection.
    """
    try:
        rolling_mean = df['Value'].rolling(window=window_size).mean()
        rolling_std = df['Value'].rolling(window=window_size).std()

        anomalies_threshold = rolling_mean + threshold_factor * rolling_std

        return anomalies_threshold
    except Exception as e:
        raise Exception(f"Error detected: {e}")