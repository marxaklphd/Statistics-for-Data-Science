import scipy.stats as stats

def confidence_interval(sample_mean, population_std_dev, sample_size, confidence_level=0.95):
    """
    Calculate the confidence interval for the mean.

    Parameters:
    - sample_mean: The mean of the sample
    - population_std_dev: The population standard deviation
    - sample_size: The size of the sample
    - confidence_level: The desired confidence level (default is 0.95)

    Returns:
    - Tuple containing the lower and upper bounds of the confidence interval
    """
    # Calculate the critical value (z-score)
    critical_value = stats.norm.ppf((1 + confidence_level) / 2)

    # Calculate the margin of error
    margin_of_error = critical_value * (population_std_dev / (sample_size ** 0.5))

    # Calculate the confidence interval
    confidence_interval_lower = sample_mean - margin_of_error
    confidence_interval_upper = sample_mean + margin_of_error

    return confidence_interval_lower, confidence_interval_upper

# Example usage:
sample_mean = 38
population_std_dev = 6.5
sample_size = 25

lower, upper = confidence_interval(sample_mean, population_std_dev, sample_size)
print(f"95% Confidence Interval: ({lower}, {upper})")
