# Let's create some variables
a = 42
b = 3.14
c = "Hello, World!"
d = [1, 2, 3]
e = (1, 2, 3)
f = {"name": "John", "age": 30}

# Check and print the data type of each variable
print("Data Types:")
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

# Convert b to string
b_str = str(b)
print("String version of b:", b_str)

# Exponential of b (b squared)
exp_b = b ** 2
print("b squared:", exp_b)

# Modulus (remainder when a is divided by b)
mod = a % b
print("a % b:", mod)

# Assignment operations on a
print("Assignment operations with a:")
a += 10
print("a + 10 =", a)

a -= 5
print("a - 5 =", a)

a *= 2
print("a * 2 =", a)

a /= 3
print("a / 3 =", a)

# Make c uppercase
c_upper = c.upper()
print("Uppercase version of c:", c_upper)

# Convert a and b to strings and join them together
a_str = str(a)
b_str = str(b)
combined = a_str + b_str
print("Combined a and b as strings:", combined)