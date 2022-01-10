"""add content column to post table

Revision ID: b2b8cae9d03e
Revises: 767a2450a41f
Create Date: 2022-01-09 11:20:21.749433

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b2b8cae9d03e'
down_revision = '767a2450a41f'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
