from scipy import stats
import numpy as np

def calculate_rmse_confidence_interval(predictions, actual_values, confidence_level=0.95):
    """
    Calculate a confidence interval for the Root Mean Squared Error (RMSE) of a model's predictions.

    Parameters:
    - predictions: Model predictions
    - actual_values: Actual values
    - confidence_level: Confidence level for the interval (default is 0.95)

    Returns:
    - Confidence interval for RMSE
    """

    # Calculate squared errors
    squared_errors = (predictions - actual_values) ** 2

    # Calculate mean and standard error of squared errors
    mean_squared_errors = squared_errors.mean()
    sem_squared_errors = stats.sem(squared_errors)

    # Calculate degrees of freedom
    degrees_of_freedom = len(squared_errors) - 1

    # Calculate confidence interval for RMSE
    lower_bound, upper_bound = stats.t.interval(confidence_level, degrees_of_freedom,
                                                loc=mean_squared_errors, scale=sem_squared_errors)

    # Return the confidence interval
    return np.sqrt(lower_bound), np.sqrt(upper_bound)

# Example usage:
# rmse_lower, rmse_upper = calculate_rmse_confidence_interval(final_predictions, y_test, confidence_level=0.95)
