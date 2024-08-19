#Explain the difference between the = operator and the == operator in Python.
#What does the ** operator do in Python, and how is it used?
#What does the ^ operator do in Python, and in what context is it commonly used?




# 1. Using the = operator (Assignment)
a = 10  # Assigning the value 10 to variable a
b = 20  # Assigning the value 20 to variable b

# 2. Using the == operator (Equality check)
are_equal = (a == b)  # Checking if a and b are equal, which should be False
print(f"Are a and b equal? {are_equal}")  # Output: Are a and b equal? False

# 3. Using the ** operator (Exponentiation)
base = 2
exponent = 3
result = base ** exponent  # Raising 2 to the power of 3
print(f"{base} raised to the power of {exponent} is {result}")  # Output: 2 raised to the power of 3 is 8

# 4. Using the ^ operator (Bitwise XOR)
a = 5  # In binary: 0101
b = 3  # In binary: 0011
xor_result = a ^ b  # Performing bitwise XOR, which should be 6 (0110 in binary)
print(f"The result of {a} ^ {b} is {xor_result}")  # Output: The result of 5 ^ 3 is 6

#The Python Bitwise XOR (^) Operator also known as the exclusive OR operator,
#is used to perform the XOR operation on two operands. XOR stands for “exclusive or”,
#and it returns true if and only if exactly one of the operands is true. In the context of bitwise operations,
#it compares corresponding bits of two operands.
# If the bits are different, it returns 1; otherwise, it returns 0.

#Example: Take two bit values X and Y, where X = 7= (111)2 and Y = 4 = (100)2 .
#Take Bitwise and of both X & Y