from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql.schema import ForeignKey
# from sqlalchemy.sql.sqltypes import Date


Base = declarative_base()


class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer(), primary_key=True)
    groupname = Column(Integer(), nullable=False)
    #власний зв'язок

    #зовнішній зв'язок
    students = relationship("Student", back_populates="group")


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer(), primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    group_id = Column(Integer(), ForeignKey("groups.id", ondelete="CASCADE"))
    #власний зв'язок
    group = relationship("Group", back_populates="students")
    #зовнішній зв'язок
    grades = relationship('Grade', back_populates='student')


class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer(), primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    #власний зв'язок

    #зовнішній зв'язок
    subjects = relationship("Subject", back_populates="teacher")


class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer(), primary_key=True)
    subject_name = Column(String(250), nullable=False)
    teacher_id = Column(Integer(), ForeignKey("teachers.id", ondelete="CASCADE"))
    #власний зв'язок
    teacher = relationship("Teacher", back_populates="subjects")
    #зовнішній зв'язок
    grades = relationship('Grade', back_populates='subject')


class Grade(Base):
    __tablename__ = "grades"
    id = Column(Integer(), primary_key=True)
    grade = Column(Integer())
    grade_date = Column(Date(), nullable=False)
    student_id = Column(Integer(), ForeignKey("students.id", ondelete="CASCADE"))
    subject_id = Column(Integer(), ForeignKey("subjects.id", ondelete="CASCADE"))
    #власний зв'язок
    student = relationship('Student', back_populates='grades')  
    subject = relationship('Subject', back_populates='grades')
    #зовнішній зв'язок