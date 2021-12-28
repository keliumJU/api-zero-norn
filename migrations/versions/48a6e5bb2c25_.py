"""empty message

Revision ID: 48a6e5bb2c25
Revises: b6c607f1ba91
Create Date: 2021-11-30 15:07:59.538347

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '48a6e5bb2c25'
down_revision = 'b6c607f1ba91'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'img')
    op.add_column('user_profile', sa.Column('img', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profile', 'img')
    op.add_column('user', sa.Column('img', mysql.TEXT(), nullable=True))
    # ### end Alembic commands ###