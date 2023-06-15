"""initial revision

Revision ID: f02b35a2de87
Revises: 
Create Date: 2023-06-09 13:48:17.894805

"""
from datetime import datetime
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f02b35a2de87'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("posts",
                    sa.Column("id", sa.Integer, autoincrement=True,
                              nullable=False, primary_key=True),
                    sa.Column("title", sa.String(30), nullable=False),
                    sa.Column("content", sa.String(240), nullable=False),
                    sa.Column("published", sa.Boolean,
                              nullable=False, server_default="1"),
                    sa.Column("created_at", sa.DateTime,
                              nullable=False, server_default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                    )


def downgrade() -> None:
    op.drop_table("posts")
