## 📘 Python Docstrings

Docstrings help you **document what your function does and how to use it**.  
They act like built-in user manuals for your code.

- ✅ Useful when working in teams or revisiting your code later.
- ✅ Shows up automatically when someone uses `help(function_name)` or hovers over the function in an editor.

### 📌 Your Note (Improved & Cleaned Up)

> **Docstrings**  
> - Help us add information about our function  
> - Explain **what the function does** and **how to use it**  
> - So when someone tries to use our function, they can easily understand its purpose

---

## ✨ Syntax

```python
def greet(name):
    """
    This function takes a name as input and returns a greeting.
    
    Parameters:
    name (str): The name of the person
    
    Returns:
    str: Greeting message
    """
    return f"Hello, {name}!"
