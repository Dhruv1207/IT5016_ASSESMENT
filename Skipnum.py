
for num in range(1, 51):
    # Skip numbers that are multiples of 4
    if num % 4 == 0:
        continue

    # Stop the loop completely if the number exceeds 40
    if num > 40:
        break

    # Print the current number
    print(num)