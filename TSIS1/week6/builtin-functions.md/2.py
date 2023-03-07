def count_upper_lower(string):
    upper_count = sum(1 for c in string if c.isupper())
    lower_count = sum(1 for c in string if c.islower())
    return (upper_count, lower_count)

# Example usage:
string = "The Quick Brown Fox Jumps Over The Lazy Dog"
upper_count, lower_count = count_upper_lower(string)
print("Upper case count:", upper_count)
print("Lower case count:", lower_count)
