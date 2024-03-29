"""Add new table for blogs

Revision ID: 0899fddcf3cf
Revises: d39fe31421d2
Create Date: 2019-11-29 19:03:23.822609

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0899fddcf3cf'
down_revision = 'd39fe31421d2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('blog_owner_id_fkey', 'blog', type_='foreignkey')
    op.drop_column('blog', 'owner_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog', sa.Column('owner_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('blog_owner_id_fkey', 'blog', 'users', ['owner_id'], ['id'])
    # ### end Alembic commands ###
