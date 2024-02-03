import scipy.stats as stats

def confidence_interval(sample_mean, sample_std_dev, sample_size, confidence_level=0.99):
    """
    Calculate the confidence interval for the mean.

    Parameters:
    - sample_mean: The mean of the sample
    - sample_std_dev: The sample standard deviation
    - sample_size: The size of the sample
    - confidence_level: The desired confidence level (default is 0.99)

    Returns:
    - Tuple containing the lower and upper bounds of the confidence interval
    """
    # Calculate the critical value (t-score)
    critical_value = stats.t.ppf((1 + confidence_level) / 2, df=sample_size - 1)

    # Calculate the margin of error
    margin_of_error = critical_value * (sample_std_dev / (sample_size ** 0.5))

    # Calculate the confidence interval
    confidence_interval_lower = sample_mean - margin_of_error
    confidence_interval_upper = sample_mean + margin_of_error

    return confidence_interval_lower, confidence_interval_upper

# Example usage:
sample_mean = 49
sample_std_dev = 4
sample_size = 9

lower, upper = confidence_interval(sample_mean, sample_std_dev, sample_size)
print(f"99% Confidence Interval: ({lower}, {upper})")
