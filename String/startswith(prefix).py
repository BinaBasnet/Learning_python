
text = "PythonProgramming.py"

# Basic usage
print(text.endswith(".py"))   # True
print(text.endswith(".txt"))  # False

# Using start and end
print(text.endswith("Programming", 6, 17))  # True (checks text[0:17])

# Checking multiple suffixes
print(text.endswith((".ty", ".txy")))  # True
