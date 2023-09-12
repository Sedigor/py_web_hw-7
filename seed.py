from connect_db import session
from models import Student, Teacher, Group, Subject, Grade
import faker
import random


fake = faker.Faker()


def create_students(num_students, num_groups):
    for _ in range(num_students):
        student = Student(
            name=fake.name(),
            group_id=random.randint(1, num_groups)
        )
        session.add(student)
    session.commit()
    
def create_groups(num_groups):
    for i in range(num_groups):
        i+=1
        group = Group(
            name='Group_' + str(i)
        )
        session.add(group)
    session.commit()
    
def create_teachers(num_teachers):
    for _ in range(num_teachers):
        teacher = Teacher(
            name=fake.name()
        )
        session.add(teacher)
    session.commit()
    
def create_subjects(subjects, num_teachers):
    for subject in subjects:
        subject = Subject(
            name=subject,
            teacher_id=random.randint(1, num_teachers)
        )
        session.add(subject)
    session.commit()

def create_grades(num_grades, num_students, subjects):
    for _ in range(num_grades):
        grade = Grade(
            grade=random.randint(60, 100),
            date_received=fake.date_this_year(),
            student_id = random.randint(1, num_students),
            subject_id = random.randint(1, len(subjects))
        )
        session.add(grade)
    session.commit()
    
    
if __name__ == '__main__':
    
    number_students = 40
    number_teachers = 5
    number_groups = 3
    subjects = ['Mathematics', 'Literature', 'History', 'Geography', 'Physics']
    number_grades = 10 * len(subjects) * number_students
    
    create_students(number_students, number_groups)
    create_groups(number_groups)
    create_teachers(number_teachers)
    create_subjects(subjects, number_teachers)
    create_grades(number_grades, number_students, subjects)