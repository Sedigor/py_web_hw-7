from sqlalchemy import func, desc, select

import connect_db
from models import Student, Group, Teacher, Subject, Grade


session = connect_db.session


def select_1():
    query = session.query(Student.first_name, Student.last_name, func.round(func.avg(Grade.grade)).label('avg_grade')) \
        .join(Grade, Student.id == Grade.student_id) \
        .group_by(Student.id) \
        .order_by(func.round(func.avg(Grade.grade)).desc()) \
        .limit(5) \
        .all()
    
    for first_name, last_name, avg_grade in query:
        print(f"Student: {first_name} {last_name}, Average Grade: {avg_grade}")
        
        
def select_2(subject_id):
    query = session.query(Student.first_name, Student.last_name, Subject.subject_name, func.round(func.avg(Grade.grade)).label('avg_grade')) \
        .join(Grade, Student.id == Grade.student_id) \
        .join(Subject, Grade.subject_id == Subject.id) \
        .filter(Grade.subject_id == subject_id) \
        .group_by(Student.id) \
        .order_by(func.round(func.avg(Grade.grade)).desc()) \
        .limit(1) \
        .first()
    
    if query:
        first_name, last_name, subject_name, avg_grade = query
        print(f"Student with Highest Average Grade in {subject_name} : {first_name} {last_name}, Average Grade: {avg_grade}")
    else:
        print("No data found")
        
        
def select_3(subject_id):
    query = session.query(Student.group_id, Grade.subject_id, func.round(func.avg(Grade.grade)).label('avg_grade')) \
        .join(Grade, Student.id == Grade.student_id) \
        .filter(Grade.subject_id == subject_id) \
        .group_by(Student.group_id, Grade.subject_id) \
        .all()
    
    for group_id, subject_id, avg_grade in query:
        print(f"Group: {group_id}, Subject: {subject_id}, Average Grade: {avg_grade}")


def select_4():
    query = session.query(func.round(func.avg(Grade.grade)).label('avg_grade')).first()
    
    if query:
        avg_grade = query[0]
        print(f"Average Grade: {avg_grade}")
    else:
        print("No data found")
        
        
def select_5():
    query = session.query(Teacher.first_name, Teacher.last_name, Subject.subject_name) \
        .join(Subject, Teacher.id == Subject.teacher_id) \
        .all()
    
    for first_name, last_name, subject_name in query:
        print(f"Teacher: {first_name} {last_name}, Subject: {subject_name}")
        
        
def select_6(group_id):
    query = session.query(Student.first_name, Student.first_name) \
        .filter(Student.group_id == group_id) \
        .all()
    
    for first_name, last_name in query:
        print(f"Student: {first_name} {last_name}")
    
    
def select_7(group_id, subject_id):
    query = session.query(Student.first_name, Student.last_name, Grade.grade) \
        .join(Grade, Student.id == Grade.student_id) \
        .filter(Student.group_id == group_id, Grade.subject_id == subject_id) \
        .group_by(Student.last_name) \
        .all()
    
    for first_name, last_name, grade in query:
        print(f"Student: {first_name} {last_name}, Grade: {grade}")


def select_8():
    query = session.query(Teacher.first_name, Teacher.last_name, func.round(func.avg(Grade.grade)).label('avg_grade')) \
        .join(Subject, Teacher.id == Subject.teacher_id) \
        .join(Grade, Subject.id == Grade.subject_id) \
        .group_by(Teacher.first_name) \
        .all()

    for first_name, last_name, avg_grade in query:
        print(f"Teacher: {first_name} {last_name}, Average Grade: {avg_grade}")


def select_9(student_id):
    query = session.query(Student.first_name, Student.last_name, Subject.subject_name) \
        .join(Grade, Student.id == Grade.student_id) \
        .join(Subject, Grade.subject_id == Subject.id) \
        .filter(Grade.id == student_id) \
        .all()
    
    for first_name, last_name, subject_name in query:
        print(f"Student: {first_name} {last_name} Subject: {subject_name}")


def select_10(student_id, teacher_id):
    query = session.query(Student.first_name, Student.last_name, Teacher.first_name, Teacher.last_name, Subject.subject_name) \
        .join(Grade, Student.id == Grade.student_id) \
        .join(Subject, Grade.subject_id == Subject.id) \
        .join(Teacher, Subject.teacher_id == Teacher.id) \
        .filter(Student.id == student_id, Teacher.id == teacher_id) \
        .group_by(Grade.subject_id) \
        .all()
    
    for student_first_name, student_last_name, teacher_first_name, teacher_last_name, subject_name in query:
        print(f"Student: {student_first_name} {student_last_name}, Teacher: {teacher_first_name} {teacher_last_name}, Subject: {subject_name}")

