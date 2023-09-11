from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.sql.sqltypes import DateTime
from faker import Faker

# import database connection config
from config import db_user, db_password, db_host, db_port, db_name

# running docker container
# docker run --name postgres_db_07 -p 5432:5432 -e POSTGRES_PASSWORD=secretpass -d postgres


db_url = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

engine = create_engine(db_url)
DBSession = sessionmaker(bind=engine)
session = DBSession()

Base = declarative_base()


university = Table(
    "university",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("student", Integer, ForeignKey("students.id", ondelete="CASCADE")),
    Column("teacher", Integer, ForeignKey("teachers.id", ondelete="CASCADE")),
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


Base.metadata.create_all(engine)
Base.metadata.bind = engine