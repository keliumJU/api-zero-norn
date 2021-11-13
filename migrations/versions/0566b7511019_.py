"""empty message

Revision ID: 0566b7511019
Revises: f87e618e2dbc
Create Date: 2021-11-11 22:38:52.742616

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0566b7511019'
down_revision = 'f87e618e2dbc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('token_fcm', sa.Text(), nullable=True))
    op.create_unique_constraint(None, 'user', ['token_fcm'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('user', 'token_fcm')
    # ### end Alembic commands ###