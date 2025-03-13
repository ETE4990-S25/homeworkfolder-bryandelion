from functools import reduce

# 1 Basic Lambda Function - Check if a number is even or odd
is_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(is_even(4))  # Output: Even
print(is_even(7))  # Output: Odd

# 2️ Advanced Lambda Function - Sum of a list
sum_list = lambda lst: sum(lst)
print(sum_list([1, 2, 3, 4, 5]))  # Output: 15

# 3️ Sorting with Lambda - Sort a list of tuples by the second element
data = [(1, 5), (3, 2), (7, 9), (4, 1)]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)  # Output: [(4, 1), (3, 2), (1, 5), (7, 9)]

# 4️ Filtering with Lambda - Filter out even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
filtered_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(filtered_numbers)  # Output: [2, 4, 6, 8]

# 5️ Mapping with Lambda - Square each number in a list
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81]

# 6️ Reducing with Lambda - Find product of all elements in a list
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 362880

# 7️ Enumerate with or without Lambda - Add index to elements in a list
indexed_list = list(enumerate(["apple", "banana", "cherry"]))
print(indexed_list)  # Output: [(0, 'apple'), (1, 'banana'), (2, 'cherry')]

# 8️ Zip with or without Lambda - Combine two lists into pairs
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
zipped_data = list(zip(names, ages))
print(zipped_data)  # Output: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
