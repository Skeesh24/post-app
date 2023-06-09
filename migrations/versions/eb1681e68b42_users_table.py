"""users table

Revision ID: eb1681e68b42
Revises: d9bdd807558d
Create Date: 2023-06-09 14:51:04.301944

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb1681e68b42'
down_revision = 'd9bdd807558d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("users",
                    sa.Column("id", sa.Integer,
                              primary_key=True, nullable=False),
                    sa.Column("email", sa.String(50), nullable=False),
                    sa.Column("password", sa.String(100), nullable=False),
                    sa.Column("created_at", sa.DateTime(timezone=True),
                              nullable=False, server_default=sa.func.now())
                    )


def downgrade() -> None:
    op.drop_table("users")
