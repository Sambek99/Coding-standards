"""Main entry point to demonstrate student grading system requirements."""

from test import Student


def main() -> None:
    """Execute scenarios validating system requirements and error handling."""
    print("==================================================")
    print(" REQ 1 & 6: STUDENT CREATION & INPUT VALIDATION   ")
    print("==================================================")
    # Casos de creación inválida manejados sin interrupción
    s_invalid1 = Student.create("", "Alan Turing")
    s_invalid2 = Student.create("STU001", "   ")
    print(f"Instancia inválida 1: {s_invalid1}")
    print(f"Instancia inválida 2: {s_invalid2}")

    # Creación exitosa
    student = Student.create("STU101", "Ada Lovelace")
    if not student:
        return
    print(f"Estudiante creado: {student.name} ({student.student_id})")

    print("\n==================================================")
    print(" REQ 2 & 6: ADD GRADES & RANGE/TYPE VALIDATIONS   ")
    print("==================================================")
    student.add_grade("Cien")     # Tipo inválido
    student.add_grade(True)       # Booleano no permitido
    student.add_grade(-15.0)      # Límite inferior violado
    student.add_grade(105.0)      # Límite superior violado
    student.add_grade(95.0)       # Nota válida
    student.add_grade(88.5)       # Nota válida
    student.add_grade(92.0)       # Nota válida
    student.add_grade(70.0)       # Nota válida

    print("\n==================================================")
    print(" REQ 3, 4, 5, 7 & 9: REPORT & STATUS EVALUATION   ")
    print("==================================================")
    student.generate_summary_report()

    print("\n==================================================")
    print(" REQ 8: REMOVE GRADES (BY INDEX & BY VALUE)       ")
    print("==================================================")
    # Errores manejados controladamente
    student.remove_grade_by_index(99)
    student.remove_grade_by_value(50.0)

    # Remociones válidas
    student.remove_grade_by_value(70.0)
    student.remove_grade_by_index(1)

    print("\n==================================================")
    print(" HONOR ROLL VERIFICATION & FINAL SUMMARY REPORT   ")
    print("==================================================")
    student.add_grade(98.0)
    student.add_grade(96.0)
    student.generate_summary_report()


if __name__ == "__main__":
    main()