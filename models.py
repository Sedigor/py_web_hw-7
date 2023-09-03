from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.sql.sqltypes import DateTime
from faker import Faker

conn_string = "host='localhost' dbname='university_postgresql' user='postgres' password='university'"
engine = create_engine(conn_string, echo=False)
DBSession = sessionmaker(bind=engine)
session = DBSession()

Base = declarative_base()

university = Table(
    "university",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("student", Integer, ForeignKey("students.id", ondelete="CASCADE")),
    Column("teacher", Integer, ForeignKey("teacher.id", ondelete="CASCADE")),
    Column("subject", Integer, ForeignKey("subjects.id", ondelete="CASCADE")),
    Column("group", Integer, ForeignKey("groups.id", ondelete="CASCADE")),
    Column("grade", Integer, ForeignKey("grades.id", ondelete="CASCADE")),
)

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    group_id = Column(Integer, ForeignKey('groups.id'))
    group = relationship("Group", back_populates="students")
    grades = relationship("Grade", back_populates="student")

class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    students = relationship("Student", back_populates="group")

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    subjects = relationship("Subject", back_populates="teacher")
    
class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    teacher = relationship("Teacher", back_populates="subjects")
    grades = relationship("Grade", back_populates="subject")

class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    grade = Column(Integer)
    date_received = Column(DateTime, default=datetime.utcnow)
    student_id = Column(Integer, ForeignKey('students.id'))
    student = relationship("Student", back_populates="grades")
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    subject = relationship("Subject", back_populates="grades")
