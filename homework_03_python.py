import math 

class Student:
   
   """A Student with Name and Score."""
   def __init__(self, name:str, score:int) -> None:
        """Construct a Student with a name and score."""
        self.name = name
        self.score = score   

   def letter_grade(self) -> str:
       """Convert a numeric score (0-100) to a letter grade."""
       if self.score >= 90:
           return "A"
       elif self.score >= 80:
           return "B"
       elif self.score >= 70:
           return "C"
       else:
           return "F"
        
   def __repr__(self) -> str:
       return f"Student [ name = '{self.name}', score = {self.score}]"


def main() -> None:
        """Run all the homework exercises."""
        print("home work for session 3 !")
        
        students = [
            Student("Alice", 85),
            Student("Bob", 72),
            Student("Carol", 91),
            Student("Ray", 65),
            Student("Alex", 50),
        ]

        print(f"Students: {students}")


        high_score = [s.name for s in students if s.score >= 80]
        print(f" high_score : {high_score}")

        grades = {s.name: s.letter_grade() for s in students }
        print(f"Grades: {grades}")

        user_input = "not a number"
        try:
            x = int(user_input)
        except ValueError as e:
            print(f"Bad input: {e}")
        finally:
            print("done")

        for s in students:
            print(f"sqrt({s.score}) = {math.sqrt(s.score):.2f}")      


if __name__ == "__main__":
    main()