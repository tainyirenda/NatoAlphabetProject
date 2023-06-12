numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# Square numbers
squared_numbers = [num * num for num in numbers]
print(squared_numbers)

# Filter even numbers
results = [num for num in numbers if num % 2 == 0]
print(results)


# new_dict = {new_key:new_value for (key, value) in dict.items() if test}


