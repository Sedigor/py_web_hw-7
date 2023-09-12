from datetime import datetime
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.sql.sqltypes import DateTime


Base = declarative_base()


university = Table(
    "university",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("student", Integer, ForeignKey("students.id", ondelete="CASCADE")),
    Column("teacher", Integer, ForeignKey("teachers.id", ondelete="CASCADE")),
    Column("subject", Integer, ForeignKey("subjects.id", ondelete="CASCADE")),
    Column("group", Integer, ForeignKey("groups.id", ondelete="CASCADE")),
    Column("grade", Integer, ForeignKey("grades.id", ondelete="CASCADE"))
)

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    group_id = Column(Integer, ForeignKey('groups.id'))
    group = relationship("Group", back_populates="student")
    grade = relationship("Grade", back_populates="student")
    

class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    student = relationship("Student", back_populates="group")

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    subject = relationship("Subject", back_populates="teacher")
    
class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    teacher = relationship("Teacher", back_populates="subject")
    grade = relationship("Grade", back_populates="subject")

class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    grade = Column(Integer)
    date_received = Column(DateTime, default=datetime.utcnow)
    student_id = Column(Integer, ForeignKey('students.id'))
    student = relationship("Student", back_populates="grade")
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    subject = relationship("Subject", back_populates="grade")
