"""empty message

Revision ID: 5bde9746c720
Revises: 5a2f557a74df
Create Date: 2021-11-20 10:17:03.868405

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5bde9746c720'
down_revision = '5a2f557a74df'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('notification', sa.Column('notification_object_id', sa.Integer(), nullable=True))
    op.drop_constraint('notification_ibfk_1', 'notification', type_='foreignkey')
    op.create_foreign_key(None, 'notification', 'notification_object', ['notification_object_id'], ['id'])
    op.drop_column('notification', 'notification_object')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('notification', sa.Column('notification_object', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'notification', type_='foreignkey')
    op.create_foreign_key('notification_ibfk_1', 'notification', 'notification_object', ['notification_object'], ['id'])
    op.drop_column('notification', 'notification_object_id')
    # ### end Alembic commands ###