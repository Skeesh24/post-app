"""users table

Revision ID: 1344476b5f9e
Revises: f02b35a2de87
Create Date: 2023-06-15 14:52:47.069230

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1344476b5f9e'
down_revision = 'f02b35a2de87'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("users",
                    sa.Column("id", sa.Integer, autoincrement=True,
                              nullable=False, primary_key=True),
                    sa.Column("email", sa.String(50),
                              nullable=False, unique=True),
                    sa.Column("password", sa.String(100), nullable=False))


def downgrade() -> None:
    op.drop_table("users")
