"""empty message

Revision ID: af478a825597
Revises: 
Create Date: 2023-06-15 14:05:42.685617

"""
from datetime import datetime
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af478a825597'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("posts",
                    sa.Column("id", sa.Integer,
                              autoincrement=True, primary_key=True),
                    sa.Column("title", sa.String, nullable=False),
                    sa.Column("published", sa.Boolean,
                              nullable=True, server_default="1"),
                    sa.Column("created_at", sa.DateTime(timezone=True),
                              nullable=False, server_default=datetime.now()),
                    sa.Column("content", sa.String, nullable=False))


def downgrade() -> None:
    op.drop_table("posts")
