from scipy.stats import norm

def calculate_critical_value(confidence_level):
    """
    Calculate the critical z-value for a given confidence level.

    Parameters:
    confidence_level (float): The desired confidence level (between 0 and 1).

    Returns:
    float: The critical z-value.
    """
    critical_value = norm.ppf((1 + confidence_level) / 2)
    return critical_value

# Example usage for a 90% confidence interval
confidence_level_90 = 0.95
critical_value_90 = calculate_critical_value(confidence_level_90)
print(f"The critical z-value for a {confidence_level_90 * 100}% confidence interval: {critical_value_90}")
