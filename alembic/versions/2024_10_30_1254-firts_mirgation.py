"""firts mirgation

Revision ID: ffa20d35a9d2
Revises: 
Create Date: 2024-10-30 12:54:46.510641

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ffa20d35a9d2'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('chat_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('registration_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('chat_id')
    )
    op.create_table('trip',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('chat_id', sa.Integer(), nullable=False),
    sa.Column('to_place', sa.JSON(), nullable=False),
    sa.Column('from_place', sa.JSON(), nullable=False),
    sa.Column('to_place_title', sa.String(length=150), nullable=False),
    sa.Column('from_place_title', sa.String(length=150), nullable=False),
    sa.Column('transport_type', sa.String(length=150), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.Column('travel_date', sa.DateTime(), nullable=False),
    sa.Column('notification_before_travel', sa.DateTime(), nullable=False),
    sa.Column('isEnded', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['chat_id'], ['user.chat_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('trip')
    op.drop_table('user')
    # ### end Alembic commands ###