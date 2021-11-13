"""empty message

Revision ID: 4b06c5f51113
Revises: 3eb119a924ca
Create Date: 2021-10-30 15:05:18.131258

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4b06c5f51113'
down_revision = '3eb119a924ca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'password',
               existing_type=mysql.VARCHAR(length=100),
               type_=sa.Text(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'password',
               existing_type=sa.Text(),
               type_=mysql.VARCHAR(length=100),
               existing_nullable=True)
    # ### end Alembic commands ###
