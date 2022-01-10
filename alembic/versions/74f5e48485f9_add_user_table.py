"""add user table

Revision ID: 74f5e48485f9
Revises: b2b8cae9d03e
Create Date: 2022-01-09 11:46:47.296763

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.expression import null


# revision identifiers, used by Alembic.
revision = '74f5e48485f9'
down_revision = 'b2b8cae9d03e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), 
                            server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
