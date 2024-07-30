from django.db import models

# Program model to store information about different programs
class Program(models.Model):
    name = models.CharField(max_length=100)  # Name of the program
    duration_months = models.IntegerField()  # Duration of the program in months

    def __str__(self):
        return self.name  # String representation of the program


# Lecturer model to store information about lecturers
class Lecturer(models.Model):
    name = models.CharField(max_length=100)  # Name of the lecturer
    email = models.EmailField(unique=True)  # Email of the lecturer, must be unique
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='lecturers')  # Program the lecturer is associated with

    def __str__(self):
        return self.name  # String representation of the lecturer


# Student model to store information about students
class Student(models.Model):
    name = models.CharField(max_length=100)  # Name of the student
    email = models.EmailField(unique=True)  # Email of the student, must be unique
    program = models.ForeignKey(Program, on_delete=models.CASCADE)  # Program the student is enrolled in
    status = models.CharField(max_length=10, default='N/A')  # Status of the student's mark

    def __str__(self):
        return self.name  # String representation of the student


# StudentMark model to store marks of students in different courses
class StudentMark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  # Reference to the student
    course = models.CharField(max_length=100)  # Name of the course
    mark = models.IntegerField()  # Mark obtained by the student
    # status = models.CharField(max_length=10, default='N/A')  # Status of the student's mark
    #
    # def save(self, *args, **kwargs):
    #     if self.mark >= 75:
    #         self.status = "Passed"
    #     else:
    #         self.status = "Failed"
    #     super().save(*args, **kwargs)     ##Mark may use in the future --Jean

    def __str__(self):
        return f'{self.student.name} - {self.course} ({self.status})'  # String representation of the student's mark



# Parent model to store information about parents of students
class Parent(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  # Reference to the student
    name = models.CharField(max_length=100)  # Name of the parent
    contact = models.CharField(max_length=15)  # Contact number of the parent

    def __str__(self):
        return self.name  # String representation of the parent


# TuitionFee model to store information about tuition fees paid by students
class TuitionFee(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  # Reference to the student
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Amount of the tuition fee
    paid_date = models.DateField()  # Date when the fee was paid

    def __str__(self):
        return f'{self.student.name} - {self.amount}'  # String representation of the tuition fee
    
class Registration(models.Model):
    name = models.CharField(max_length=100)  # Name of the student
    email = models.EmailField(unique=True)  # Email of the student, must be unique
    username = models.CharField(max_length=100)  # Username of the student
    passworrd = models.CharField(max_length=100)  # Password of the student
    program = models.ForeignKey(Program, on_delete=models.CASCADE)  # Program the student is enrolled in

    def __str__(self):
        return self.name
