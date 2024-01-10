from anomalies_detector import detect_anomalies
from argument_parse import parse_arguments, load_data
from plotting import plot_anomalies


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

        anomalies_threshold = detect_anomalies(df, args.window_size,
                                               args.threshold_factor)
        plot_anomalies(df, anomalies_threshold)
    except Exception as e:
        raise Exception(f"Error detected: {e}")


if __name__ == "__main__":
    main()
