def days_since_birthday(birthday):
    # Split the birthday string into day, month, year
    day, month, year = birthday.split('-')

# Convert the split strings into integers
    birth_day = int(day)
    birth_month = int(month)
    birth_year = int(year)

# Assume today's date for the sake of this exercise (e.g., "25-02-2024")
    today_day = 25
    today_month = 2
    today_year = 2024

# Calculate the number of full years since the birthday
    full_years_passed = today_year - birth_year - 1  # Subtract 1 to exclude the current year

# Convert full years to days
    days_passed = full_years_passed * 365

# Add extra day for each leap year passed (every 4 years starting from birth year + 4)
    for leap_year in range(birth_year + 4, today_year, 4):
        # Assuming no starting and ending edge cases for February 29
        days_passed += 1

    return days_passed


# Test the function with a sample birthday
print(days_since_birthday("13-09-2002"))  # Replace "13-09-2002" with your actual birthday