"""Renaming students to scholars

Revision ID: 644a464a8131
Revises: 791279dd0760
Create Date: 2024-03-18 22:23:14.679874

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '644a464a8131'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
