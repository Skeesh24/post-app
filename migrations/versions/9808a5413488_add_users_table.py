"""add users table

Revision ID: 9808a5413488
Revises: e0c4458caf1a
Create Date: 2023-06-10 00:26:22.474489

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9808a5413488'
down_revision = 'e0c4458caf1a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("users",
                    op.Column("id", sa.Integer, primary_key=True,
                              autoincrement=True),
                    op.Column("email", sa.String(50),
                              unique=True, nullable=False),
                    op.Column("password", sa.String(100), nullable=False),
                    op.Column("created_at", sa.DateTime(timezone=True),
                              nullable=False, server_default=sa.func.now()))


def downgrade() -> None:
    op.drop_table("users")
