#ctreate a list from 1 to 10
numbers = list(range(1, 11))
print(numbers)

#create a list by using for loop from 1 to 10
numbers = list(range(1, 11))

for num in numbers:
    print(num)

#add number by using .append
numbers = list(range(1, 11))

numbers.append(11)
numbers.append(12)
numbers.append(13)

print(numbers)

# Remove number 5
numbers.remove(5)

# Print the final list
print(numbers)

