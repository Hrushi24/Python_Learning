# 📘 Python Dictionary: Short Notes with Use Cases

# ✅ What is a Dictionary?
# A dictionary is a built-in Python data structure that stores data as key-value pairs.
# Think of it like a phonebook: name (key) → number (value).

# 📌 Syntax:
my_dict = {
    "name": "Alice",
    "age": 25,
    "is_student": True
}

# 🎯 Use Cases:
# - Fast lookups (O(1) time on average)
# - Mapping labels to values (e.g. user data, config settings)
# - Counting items, grouping, or storing structured data

# 🔍 Accessing Values:
print(my_dict["name"])   # Output: Alice

# 🧱 Adding or Updating:
my_dict["email"] = "alice@example.com"
my_dict["age"] = 26

# ❌ Deleting:
del my_dict["is_student"]

# ✅ Checking Key Existence:
if "email" in my_dict:
    print("Email is present!")

# 🔄 Looping Through:
for key, value in my_dict.items():
    print(f"{key} → {value}")

# 📦 Nesting: Dict inside List or vice versa
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92}
]

# Access nested value
print(students[1]["score"])  # Output: 92

# 📚 Real-World Examples:
# - JSON data from APIs
# - User profiles
# - Counting words or occurrences
# - Settings or configuration files
