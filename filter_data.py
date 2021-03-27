# Example 1: Value below avg

data = [1.3, 2.7, 2.3, 3.6]
avg = sum(data) / len(data)
below_avg = list(filter(lambda x: x < avg, data))
print(below_avg)


# Example 2: Remove missing data

countries = ["", "Bangladesh", "Canada", "USA", "", "", "Germany"]
valid_countries = list(filter(None, countries))
print(valid_countries)
