"""Module for managing student records, grades, and academic performance."""

from typing import List, Optional, Union


class Student:
    """Represents a student and manages their grades and academic status."""

    def __init__(self, student_id: str, name: str) -> None:
        """Initialize a student with ID, name, and an empty list of grades.

        Raises:
            ValueError: If student_id or name is empty or not a string.
        """
        if not isinstance(student_id, str) or not student_id.strip():
            raise ValueError("Student ID must be a non-empty string.")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Student name must be a non-empty string.")

        self.student_id: str = student_id.strip()
        self.name: str = name.strip()
        self.grades: List[float] = []

    def add_grade(self, grade: Union[int, float]) -> bool:
        """Validate and add a grade between 0 and 100."""
        if not isinstance(grade, (int, float)) or isinstance(grade, bool):
            print(f"Error: Grade '{grade}' must be a numeric value.")
            return False

        if not 0.0 <= float(grade) <= 100.0:
            print(f"Error: Grade {grade} is out of bounds (must be 0-100).")
            return False

        self.grades.append(float(grade))
        return True

    def calculate_average(self) -> float:
        """Calculate and return the average of all grades."""
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def determine_letter_grade(self) -> str:
        """Determine the letter grade based on the average grade."""
        avg = self.calculate_average()
        if avg >= 90.0:
            return "A"
        if avg >= 80.0:
            return "B"
        if avg >= 70.0:
            return "C"
        if avg >= 60.0:
            return "D"
        return "F"

    def is_passed(self) -> bool:
        """Determine whether the student passed (average >= 60.0)."""
        return self.calculate_average() >= 60.0

    def is_honor_roll(self) -> bool:
        """Determine if student qualifies for honor roll (average >= 90.0)."""
        return self.calculate_average() >= 90.0

    def remove_grade_by_index(self, index: int) -> bool:
        """Remove a grade using its zero-based index."""
        if not isinstance(index, int) or isinstance(index, bool):
            print(f"Error: Index '{index}' must be an integer.")
            return False

        if 0 <= index < len(self.grades):
            removed = self.grades.pop(index)
            print(f"Success: Grade {removed} removed at index {index}.")
            return True

        print(f"Error: Index {index} is out of range.")
        return False

    def remove_grade_by_value(self, grade: Union[int, float]) -> bool:
        """Remove the first occurrence of a specific grade value."""
        if not isinstance(grade, (int, float)) or isinstance(grade, bool):
            print(f"Error: Target grade '{grade}' must be numeric.")
            return False

        grade_val = float(grade)
        if grade_val in self.grades:
            self.grades.remove(grade_val)
            print(f"Success: Grade {grade_val} removed.")
            return True

        print(f"Error: Grade {grade_val} was not found in records.")
        return False

    def generate_summary_report(self) -> None:
        """Display a formatted summary report for the student."""
        avg = self.calculate_average()
        letter = self.determine_letter_grade()
        status = "Passed" if self.is_passed() else "Failed"
        honor = self.is_honor_roll()

        print("=" * 45)
        print("          STUDENT SUMMARY REPORT             ")
        print("=" * 45)
        print(f"Student ID:        {self.student_id}")
        print(f"Student Name:      {self.name}")
        print(f"Number of Grades:  {len(self.grades)}")
        print(f"Average Grade:     {avg:.2f}")
        print(f"Letter Grade:      {letter}")
        print(f"Pass/Fail Status:  {status}")
        print(f"Honor Roll Status: {honor}")
        print("=" * 45)

    @classmethod
    def create(cls, student_id: str, name: str) -> Optional["Student"]:
        """Factory method to validate inputs and safely instantiate a Student."""
        if not isinstance(student_id, str) or not student_id.strip():
            print("Error: Student ID must be a non-empty string.")
            return None

        if not isinstance(name, str) or not name.strip():
            print("Error: Student name must be a non-empty string.")
            return None

        return cls(student_id, name)

