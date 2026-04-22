class Dog:
    """A dog with Name and Age."""

    def __init__(self, name:str, age:int) -> None:
        """Construct a Dog with a name and age."""
        self.name = name
        self.age = age

    def bark(self) -> str:
        """Return the Dog's bark message"""
        return f"{self.name} says woof"
    
d = Dog ("rex" ,5 )
print(d.bark())

# The Java way (works in Python too, but not idiomatic)
squares = []
for n in range(10):
    squares.append(n ** 2)

# The Python way — list comprehension
squares = [n ** 2 for n in range(10)]

students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 72},
    {"name": "Carol", "score": 91},
]

names = [s["name"] for s in students]
print(f" names = {names}")
# ['Alice', 'Bob', 'Carol']

passing_names = [s["name"] for s in students if s["score"] >= 80]
# ['Alice', 'Carol']
print(f" passing names {passing_names}")

score_lookup = {s["name"]: s["score"] for s in students}
# {'Alice': 85, 'Bob': 72, 'Carol': 91}
print(f"score lookup {score_lookup}")

def main() -> None:
    """Entry point of the script."""
    print("running main")


if __name__ == "__main__":
    main()

# The Java way (works in Python too, but not idiomatic)
squares = []
for n in range(10):
    squares.append(n ** 2)

print(f" Java way squares = {squares}")

# The Python way — list comprehension
squares = [n ** 2 for n in range(10)]

print(f"squares = {squares}")

#[ EXPRESSION for VARIABLE in ITERABLE ]

even_squares = [n ** 2 for n in range(10) if n % 2 == 0]
# [0, 4, 16, 36, 64]
print(f"even_squares = {even_squares}")

students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 72},
    {"name": "Carol", "score": 91},
]

names = [s["name"] for s in students]
# ['Alice', 'Bob', 'Carol']
print(f"s.name = {names}")

passing_names = [s["name"] for s in students if s["score"] >= 80]
# ['Alice', 'Carol']
print(f"passing names = {passing_names}")

score_lookup = {s["name"]: s["score"] for s in students}
# {'Alice': 85, 'Bob': 72, 'Carol': 91}
print(f"score lookup = {score_lookup}")

def main() -> None:
    """Entry point of the script."""
    print("running main")


if __name__ == "__main__":
    main()


"""Phase 0 homework: Python basics."""


def is_even(n: int) -> bool:
    """Return True if n is even, False otherwise."""
    return n % 2 == 0


def grade(score: int) -> str:
    """Convert a numeric score (0-100) to a letter grade."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"

class Dog:
    """A dog with Name and Age."""

    def __init__(self, name:str, age:int) -> None:
        """Construct a Dog with a name and age."""
        self.name = name
        self.age = age

    def bark(self) -> str:
        """Return the Dog's bark message"""
        return f"{self.name} says woof"
    


def main() -> None:
    """Run all the homework exercises."""
    print(f"4 is even? {is_even(4)}")
    print(f"Grade for 82: {grade(82)}")
    d = Dog ("Tilo" ,5 )
    print(d.bark())

    user_input = "str"
    try:
        x = int(user_input)
    except ValueError as e:
            print(f"Bad input: {e}")
    finally:
            print("done")
    



if __name__ == "__main__":
    main()