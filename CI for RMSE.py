#If the data set is large enough the z-score can be used instead of the t-score 
from scipy import stats
import numpy as np

def calculate_confidence_interval(y_true, y_predicted, confidence_level, use_z_score=True):
    """
    Calculate the confidence interval for the squared errors of predicted values.

    Parameters:
    - y_true (array-like): True values.
    - y_predicted (array-like): Predicted values.
    - confidence_level (float): The desired confidence level (e.g., 0.95 for 95% confidence).
    - use_z_score (bool): If True, calculate the confidence interval using Z-score; otherwise, use t-score.

    Returns:
    - tuple: A tuple representing the lower and upper bounds of the confidence interval.
    """
    squared_errors = (y_predicted - y_true) ** 2
    degrees_of_freedom = len(squared_errors) - 1

    if use_z_score:
        interval = stats.norm.interval(confidence_level,
                                       loc=squared_errors.mean(),
                                       scale=stats.sem(squared_errors))
    else:
        interval = stats.t.interval(confidence_level, degrees_of_freedom,
                                    loc=squared_errors.mean(),
                                    scale=stats.sem(squared_errors))

    return np.sqrt(interval)

# Example usage:
confidence_level = 0.95
y_true =  # your true values
y_predicted =  # your predicted values

# User chooses to use Z-score
confidence_interval_z = calculate_confidence_interval(y_true, y_predicted, confidence_level, use_z_score=True)
print("Confidence Interval (Z-score):", confidence_interval_z)

# User chooses to use t-score
confidence_interval_t = calculate_confidence_interval(y_true, y_predicted, confidence_level, use_z_score=False)
print("Confidence Interval (t-score):", confidence_interval_t)
