from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from models import Student, Group, Teacher, Subject, Grade

# Підключення до бази даних
engine = create_engine('postgresql+psycopg2://user:university@localhost/university_postgresql')
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()

# Створення груп
groups = [Group(name=fake.random_element(elements=("Group A", "Group B", "Group C"))) for _ in range(3)]

# Створення вчителів
teachers = [Teacher(name=fake.name()) for _ in range(5)]

# Створення предметів та призначення їх вчителям
subjects = [Subject(name=fake.random_element(elements=("Math", "History", "English"))) for _ in range(8)]
for subject in subjects:
    subject.teacher = fake.random_element(teachers)

# Створення студентів
students = [Student(name=fake.name(), group=fake.random_element(groups)) for _ in range(50)]

# Створення оцінок для студентів із предметів
for student in students:
    for subject in subjects:
        session.add(Grade(student=student, subject=subject, grade=fake.pyfloat(left_digits=1, right_digits=1, positive=True)))

# Збереження даних у базу даних
session.commit()
