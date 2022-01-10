"""add foreign key to post table

Revision ID: 335aee010274
Revises: 74f5e48485f9
Create Date: 2022-01-09 11:58:33.472262

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '335aee010274'
down_revision = '74f5e48485f9'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_user_fk', source_table="posts", referent_table="users", 
                            local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_user_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
