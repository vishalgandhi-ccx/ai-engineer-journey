name = "Vishal"
age = 48
is_engineer = True

print(name)
print(f"Hello, {name}. You are {age} years old")

numbers = [10, 20, 30, 40, 50]

print(numbers)
print(numbers[0])       # first element
print(numbers[-1])      # last element (negative index works backward!)
print(len(numbers))     # 

for i in range(5):
    print(i)

numbers = [10, 20, 30]
for n in numbers:
    print(n)

for i, n in enumerate(numbers):
    print(f"Index {i}: value {n}")

x = 10
if x > 5:
    print("big")
elif x == 5:
    print("equal")
else:
    print("small")

def add(a: int, b: int) -> int:
    """Add two integers and return the sum."""
    return a + b

result = add(3, 4)
print(result)  # 7


scores = {"math": 90, "science": 85}
print(scores["math"])        # 90
scores["english"] = 75       # add a new entry
print(scores)                # {'math': 90, 'science': 85, 'english': 75}