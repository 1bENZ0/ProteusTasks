import numpy as np
from scipy import stats


def z_score_remove(df, threshold):
    """
    Analysis and removal of outliers through standardized assessment.

    Parameters
    ----------
    df : pandas.Dataframe[float, int]
        Initial data.
    threshold : float
        The threshold for determining outliers.


    Returns
    -------
        pandas.Dataframe[float, int]
    """
    try:
        # Calculation of z-score
        z_scores = np.abs(stats.zscore(df['Value']))
        # Determination of outliers indices based on z-score and threshold
        outliers = np.where(z_scores > threshold)[0]
        # Drop outliers
        df_cleaned = df.drop(index=df.index[outliers])
        return df_cleaned
    except Exception as e:
        raise Exception(f"Error during outliers removal: {e}")
