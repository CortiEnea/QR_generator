"""aggiunta utente

Revision ID: 868d79221e9f
Revises: 
Create Date: 2024-10-30 11:55:22.477102

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '868d79221e9f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('qr_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('link', sa.String(length=120), nullable=False),
    sa.Column('color', sa.String(length=10), nullable=False),
    sa.Column('back', sa.String(length=10), nullable=False),
    sa.Column('filename', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('qr_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('qr_user')
    op.drop_table('qr_data')
    # ### end Alembic commands ###
