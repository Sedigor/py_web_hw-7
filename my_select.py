from sqlalchemy import func, desc, select

from connect_db import session
from models import Student, Group, Teacher, Subject, Grade


def query_1():
    query = session.query(Student.name, func.round(func.avg(Grade.grade)).label('avg_grade')) \
        .join(Grade, Student.id == Grade.student_id) \
        .group_by(Student.id) \
        .order_by(func.round(func.avg(Grade.grade)).desc()) \
        .limit(5) \
        .all()
    
    for student_name, avg_grade in query:
        print(f"Student: {student_name}, Average Grade: {avg_grade}")
        
        
def query_2():
    query = session.query(Student.name, func.round(func.avg(Grade.grade)).label('avg_grade')) \
        .join(Grade, Student.id == Grade.student_id) \
        .filter(Grade.subject_id == 4) \
        .group_by(Student.id) \
        .order_by(func.round(func.avg(Grade.grade)).desc()) \
        .limit(1) \
        .first()
    
    if query:
        student_name, avg_grade = query
        print(f"Student with Highest Average Grade in Subject 4: {student_name}, Average Grade: {avg_grade}")
    else:
        print("No data found")
        
        
def query_3():
    query = session.query(Student.group_id, Grade.subject_id, func.round(func.avg(Grade.grade)).label('avg_grade')) \
        .join(Grade, Student.id == Grade.student_id) \
        .filter(Grade.subject_id == 2) \
        .group_by(Student.group_id, Grade.subject_id) \
        .all()
    
    for group_id, subject_id, avg_grade in query:
        print(f"Group: {group_id}, Subject: {subject_id}, Average Grade: {avg_grade}")


def query_4():
    query = session.query(func.round(func.avg(Grade.grade)).label('avg_grade')).first()
    
    if query:
        avg_grade = query[0]
        print(f"Average Grade: {avg_grade}")
    else:
        print("No data found")
        
        
def query_5():
    query = session.query(Teacher.teacher_name, Subject.subject_name) \
        .join(Subject, Teacher.id == Subject.id) \
        .all()
    
    for teacher_name, subject_name in query:
        print(f"Teacher: {teacher_name}, Subject: {subject_name}")
        
        
def query_6(group_id):
    query = session.query(Student.student_name) \
        .filter(Student.group_id == group_id) \
        .all()
    
    for student_name in query:
        print(f"Student: {student_name[0]}")
    
    
def query_7(group_id, subject_id):
    query = session.query(Student.student_name, Grade.grade) \
        .join(Grade, Student.id == Grade.student_id) \
        .filter(Student.group_id == group_id, Grade.subject_id == subject_id) \
        .all()
    
    for student_name, grade in query:
        print(f"Student: {student_name}, Grade: {grade}")


def query_8():
    query = session.query(Teacher.teacher_name, func.round(func.avg(Grade.grade)).label('avg_grade')) \
        .join(Subject, Teacher.id == Subject.teacher_id) \
        .join(Grade, Subject.id == Grade.subject_id) \
        .group_by(Teacher.teacher_name) \
        .all()

    for teacher_name, avg_grade in query:
        print(f"Teacher: {teacher_name}, Average Grade: {avg_grade}")


def query_9(grade_id):
    query = session.query(Student.student_name, Subject.subject_name) \
        .join(Grade, Student.id == Grade.student_id) \
        .join(Subject, Grade.subject_id == Subject.id) \
        .filter(Grade.id == grade_id) \
        .all()
    
    for student_name, subject_name in query:
        print(f"Student: {student_name}, Subject: {subject_name}")


def query_10(student_id, teacher_id):
    query = session.query(Student.student_name, Teacher.teacher_name, Subject.subject_name) \
        .join(Grade, Student.id == Grade.student_id) \
        .join(Subject, Grade.subject_id == Subject.id) \
        .join(Teacher, Subject.teacher_id == Teacher.id) \
        .filter(Student.id == student_id, Teacher.id == teacher_id) \
        .all()
    
    for student_name, teacher_name, subject_name in query:
        print(f"Student: {student_name}, Teacher: {teacher_name}, Subject: {subject_name}")

