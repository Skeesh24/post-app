"""pass longitude update

Revision ID: ee2696ba5fe7
Revises: 48ca20493a05
Create Date: 2023-06-09 15:07:33.131419

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ee2696ba5fe7'
down_revision = '48ca20493a05'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column("users", "password",
                    type_=sa.String(100))


def downgrade() -> None:
    op.alter_column("users", "password",
                    type_=sa.String(50))
