"""Fix on hold

Revision ID: e56f1c781e46
Revises: 714f227201a7
Create Date: 2023-11-03 20:47:52.601783
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e56f1c781e46'
down_revision = '714f227201a7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('on_hold_timeout', sa.DateTime))
    op.add_column('users', sa.Column('on_hold_expire_duration', sa.BigInteger(), nullable=True))
    op.drop_column('users', 'timeout')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('timeout', sa.Integer))
    op.drop_column('users', 'on_hold_timeout')
    op.drop_column('users', 'on_hold_expire_duration')
    # ### end Alembic commands ###
