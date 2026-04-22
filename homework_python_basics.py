"""Phase 0 homework: Python basics."""

# 1. Print personal info
store = "Amazon"
name = "Vishal"
age = 48
city = "McKinney"

print(f"My name is {name}, I live in {city} and I am {age} years old.")


# 2. Sum a list
numbers = range(10)
total = 0
for n in numbers:
    total += n
print(f"Sum = {total}")


# 3. Even/odd check
def is_even(n: int) -> bool:
    """Return True if n is even, False otherwise."""
    return n % 2 == 0


print(f"4 is even? {is_even(4)}")
print(f"7 is even? {is_even(7)}")


# 4. Grade classifier
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


for s in [95, 82, 73, 50]:
    print(f"Score {s} → grade {grade(s)}")


# 5. Dictionary drill
students = {"Alice": 85, "Bob": 72, "Carol": 91}

for student_name, student_score in students.items():
    print(f"{student_name} scored {student_score}")