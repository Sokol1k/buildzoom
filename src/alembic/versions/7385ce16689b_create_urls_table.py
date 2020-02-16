"""create urls table

Revision ID: 7385ce16689b
Revises: 
Create Date: 2019-12-21 13:59:56.376042

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7385ce16689b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'urls',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('url', sa.String(255), nullable=False),
        sa.Column('status', sa.Integer())
    )
    op.create_unique_constraint('url', 'urls', ['url'])


def downgrade():
    op.drop_table('urls')
