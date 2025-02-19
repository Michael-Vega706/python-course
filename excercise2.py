def sum(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

def divide(a: int, b: int) -> float | None:
    try:
        return a / b
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return None

a: int = 5
b: int = 0
print(f"Sum: {a} + {b} = {sum(a, b)}")
print(f"Subtract: {a} - {b} = {subtract(a, b)}")
print(f"Divide: {a} / {b} = {divide(a, b)}")

def greet(name: str) -> str:
    return f"Hello, {name}!"

def years_old(age: int) -> str:
    return f"Age: {age}"

def login(name, age) -> None:
    print(f"{greet(name)}")
    print(f"{years_old(age)}")
    
login("John Doe", 25)