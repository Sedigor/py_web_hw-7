"""Init

Revision ID: 814e8081274c
Revises: 
Create Date: 2023-09-11 21:10:01.646497

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '814e8081274c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


# def upgrade() -> None:
#     # ### commands auto generated by Alembic - please adjust! ###
#     op.create_table('students',
#     sa.Column('id', sa.Integer(), nullable=False),
#     sa.Column('name', sa.String(length=50), nullable=False),
#     sa.Column('group_id', sa.Integer(), nullable=False),
#     sa.PrimaryKeyConstraint('id'),
#     sa.ForeignKeyConstraint(['group_id'], ['groups.id'], ondelete='CASCADE')
#     )
#     op.create_table('groups',
#     sa.Column('id', sa.Integer(), nullable=False),
#     sa.Column('name', sa.String(length=50), nullable=False),
#     sa.PrimaryKeyConstraint('id')
#     )
#     op.create_table('teachers',
#     sa.Column('id', sa.Integer(), nullable=False),
#     sa.Column('name', sa.String(length=50), nullable=False),
#     sa.PrimaryKeyConstraint('id')
#     )
#     op.create_table('subjects',
#     sa.Column('id', sa.Integer(), nullable=False),
#     sa.Column('name', sa.String(length=50), nullable=False),
#     sa.Column('teacher_id', sa.Integer(), nullable=False),
#     sa.PrimaryKeyConstraint('id'),
#     sa.ForeignKeyConstraint(['teacher_id'], ['teachers.id'], ondelete='CASCADE')
#     )
#     op.create_table('grades',
#     sa.Column('id', sa.Integer(), nullable=False),
#     sa.Column('grade', sa.Integer(), nullable=False),
#     sa.Column('date_received', sa.DateTime(), nullable=False),
#     sa.Column('student_id', sa.Integer(), nullable=False),
#     sa.Column('subject_id', sa.Integer(), nullable=False),
#     sa.PrimaryKeyConstraint('id'),
#     sa.ForeignKeyConstraint(['student_id'], ['students.id'], ondelete='CASCADE'),
#     sa.ForeignKeyConstraint(['subject_id'], ['subjects.id'], ondelete='CASCADE')
#     )
#     op.create_table('university',
#     sa.Column('id', sa.Integer(), nullable=False),
#     sa.Column('student', sa.Integer(), nullable=False),
#     sa.Column('teacher', sa.DateTime(), nullable=False),
#     sa.Column('subject', sa.Integer(), nullable=False),
#     sa.Column('group', sa.Integer(), nullable=False),
#     sa.Column('grade', sa.Integer(), nullable=False),
#     sa.PrimaryKeyConstraint('id'),
#     sa.ForeignKeyConstraint(['student'], ['students.id'], ondelete='CASCADE'),
#     sa.ForeignKeyConstraint(['teacher'], ['teachers.id'], ondelete='CASCADE'),
#     sa.ForeignKeyConstraint(['subject'], ['subjects.id'], ondelete='CASCADE'),
#     sa.ForeignKeyConstraint(['group'], ['groups.id'], ondelete='CASCADE'),
#     sa.ForeignKeyConstraint(['grade'], ['grades.id'], ondelete='CASCADE')
#     )
    # ### end Alembic commands ###

def upgrade():
    op.create_table(
        'students',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('group_id', sa.Integer(), sa.ForeignKey('groups.id')),
    )

    op.create_table(
        'groups',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
    )

    op.create_table(
        'grades',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('grade', sa.Integer(), nullable=True),
        sa.Column('date_received', sa.DateTime(), default=sa.func.now()),
        sa.Column('student_id', sa.Integer(), sa.ForeignKey('students.id')),
        sa.Column('subject_id', sa.Integer(), sa.ForeignKey('subjects.id')),
    )

    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
    )

    op.create_table(
        'subjects',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('teacher_id', sa.Integer(), sa.ForeignKey('teachers.id')),
    )

def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('university')
    op.drop_table('students')
    op.drop_table('groups')
    op.drop_table('teachers')
    op.drop_table('subjects')
    op.drop_table('grades')
    # ### end Alembic commands ###
