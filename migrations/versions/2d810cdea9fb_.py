"""empty message

Revision ID: 2d810cdea9fb
Revises: f830ed9bbde2
Create Date: 2019-12-18 19:03:23.170713

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d810cdea9fb'
down_revision = 'f830ed9bbde2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('car',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('brand', sa.String(length=100), nullable=True),
    sa.Column('model', sa.String(length=100), nullable=True),
    sa.Column('manufacture', sa.String(length=100), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('code', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('users')
    op.drop_table('cars')
    op.drop_constraint(None, 'advt', type_='foreignkey')
    op.drop_constraint(None, 'advt', type_='foreignkey')
    op.create_foreign_key(None, 'advt', 'car', ['car_id'], ['id'])
    op.create_foreign_key(None, 'advt', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'advt', type_='foreignkey')
    op.drop_constraint(None, 'advt', type_='foreignkey')
    op.create_foreign_key(None, 'advt', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'advt', 'cars', ['car_id'], ['id'])
    op.create_table('cars',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('brand', sa.VARCHAR(length=100), nullable=True),
    sa.Column('model', sa.VARCHAR(length=100), nullable=True),
    sa.Column('manufacture', sa.VARCHAR(length=100), nullable=True),
    sa.Column('year', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('phone', sa.VARCHAR(), nullable=True),
    sa.Column('code', sa.VARCHAR(), nullable=True),
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('user')
    op.drop_table('car')
    # ### end Alembic commands ###
