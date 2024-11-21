class Student:
    """
    A class to represent a student.

    Attributes:
        id (str): The ID of the student.
        name (str): The name of the student.
        email (str): The email of the student.
    """
    def __init__(self, id, name, email):
        """
        Initialize a student with an ID, name, and email.

        Args:
            id (str): The ID of the student.
            name (str): The name of the student.
            email (str): The email of the student.
        """
        self.id = id
        self.name = name
        self.email = email

    def print_details(self):
        """
        Return the details of the student in a formatted string.

        Returns:
            str: The student's details.
        """
        return 'Id: {}, Name: {}, Email: {}'.format(self.id, self.name, self.email)



student_1 = Student("xnct0258", "John Smith", "johnsmith@leeds.ac.uk")
student_2 = Student("jytbuwqr", "Varia Costantine", "v.constantine@leeds.ac.uk")


print("Student 1 details:", student_1.print_details())
print("Student 2 details:", student_2.print_details())
