from scipy.stats import t

def calculate_critical_value_t(confidence_level, degrees_of_freedom):
    """
    Calculate the critical t-value for a given confidence level and degrees of freedom.

    Parameters:
    confidence_level (float): The desired confidence level (between 0 and 1).
    degrees_of_freedom (int): The degrees of freedom.

    Returns:
    float: The critical t-value.
    """
    critical_value_t = t.ppf((1 + confidence_level) / 2, degrees_of_freedom)
    return critical_value_t

# Example usage for a 90% confidence interval with 10 degrees of freedom
confidence_level_90 = 0.95
degrees_of_freedom = 25
critical_value_t_90 = calculate_critical_value_t(confidence_level_90, degrees_of_freedom)
print(f"The critical t-value for a {confidence_level_90 * 100}% confidence interval: {critical_value_t_90}")
