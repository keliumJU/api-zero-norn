"""empty message

Revision ID: 920b4b46f825
Revises: 7021a40f62ad
Create Date: 2021-11-25 09:37:01.205484

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '920b4b46f825'
down_revision = '7021a40f62ad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('job_offer', 'salary',
               existing_type=mysql.FLOAT(),
               type_=sa.Numeric(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('job_offer', 'salary',
               existing_type=sa.Numeric(),
               type_=mysql.FLOAT(),
               existing_nullable=True)
    # ### end Alembic commands ###
