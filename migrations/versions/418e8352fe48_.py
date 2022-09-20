"""empty message

Revision ID: 418e8352fe48
Revises: 
Create Date: 2022-09-20 09:52:50.991346

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '418e8352fe48'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('upload',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image', sa.TEXT(), nullable=False),
    sa.Column('name', sa.TEXT(), nullable=False),
    sa.Column('mimetype', sa.TEXT(), nullable=False),
    sa.Column('like', sa.String(length=20), nullable=False),
    sa.Column('dislike', sa.String(length=20), nullable=False),
    sa.Column('comentario', sa.String(length=20), nullable=False),
    sa.Column('usuario', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.TEXT(length=20), nullable=False),
    sa.Column('mail', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('upload')
    # ### end Alembic commands ###
