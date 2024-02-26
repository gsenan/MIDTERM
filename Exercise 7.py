import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))
# continue here
for i in range(len(random_numbers)):  # Use range(len()) to iterate over indices
    if random_numbers[i] > 50:
        random_numbers[i] = "Remove"  # Mark numbers greater than 50 for removal
    else:
        random_numbers[i] = "XX"  # Replace other numbers with "XX"

# Remove all "Remove" entries from the list
random_numbers = [num for num in random_numbers if num != "Remove"]

# Print the modified list
print(random_numbers)