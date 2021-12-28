"""empty message

Revision ID: 8fd92e715309
Revises: 920b4b46f825
Create Date: 2021-11-30 14:47:16.813308

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8fd92e715309'
down_revision = '920b4b46f825'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_profile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('full_name', sa.String(length=255), nullable=True),
    sa.Column('phone', sa.String(length=45), nullable=True),
    sa.Column('mobile', sa.String(length=45), nullable=True),
    sa.Column('address', sa.Text(), nullable=True),
    sa.Column('web_site', sa.Text(), nullable=True),
    sa.Column('github', sa.Text(), nullable=True),
    sa.Column('twitter', sa.Text(), nullable=True),
    sa.Column('facebook', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_profile')
    # ### end Alembic commands ###
