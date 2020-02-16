"""create contractor table

Revision ID: 70c13e429ad5
Revises: 7385ce16689b
Create Date: 2019-12-24 09:39:53.142505

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70c13e429ad5'
down_revision = '7385ce16689b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'contractor',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(150), nullable=False),
        sa.Column('url', sa.String(255), nullable=False),
        sa.Column('description', sa.String(500)),
        sa.Column('category', sa.String(50)),
        sa.Column('rating', sa.Float()),
        sa.Column('rating_buildzoom', sa.Integer()),
        sa.Column('phone', sa.String(30)),
        sa.Column('email', sa.String(100)),
        sa.Column('website', sa.String(255)),
        sa.Column('is_licensed', sa.Boolean(), default=False),
        sa.Column('license_info', sa.JSON),
        sa.Column('insured_value', sa.String(50)),
        sa.Column('bond_value', sa.String(50)),
        sa.Column('street_address', sa.String(50)),
        sa.Column('city', sa.String(50)),
        sa.Column('state', sa.String(50)),
        sa.Column('zipcode', sa.String(50)),
        sa.Column('full_address', sa.String(50)),
        sa.Column('image', sa.String(255)),
        sa.Column('info_updated_at', sa.String(50)),
        sa.Column('employee',  sa.JSON),
        sa.Column('work_preferences',  sa.JSON),
        sa.Column('create_at',  sa.TIMESTAMP,
                  server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at',  sa.TIMESTAMP,
                  server_default=sa.text('now()'), server_onupdate=sa.text('now()'), nullable=False),
    )
    op.create_unique_constraint('url', 'contractor', ['url'])


def downgrade():
    op.drop_table('contractor')
