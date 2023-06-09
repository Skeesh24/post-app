"""post table

Revision ID: e0c4458caf1a
Revises: 
Create Date: 2023-06-10 00:15:34.916121

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e0c4458caf1a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("posts",
                    op.Column("id", sa.Integer, primary_key=True,
                              autoincrement=True),
                    op.Column("title", sa.String(50), nullable=False),
                    op.Column("content", sa.String(200), nullable=False),
                    op.Column("published", sa.Boolean,
                              server_default="1", nullable=False),
                    op.Column("created_at", sa.DateTime(timezone=True),
                              nullable=False, server_default=sa.func.now()),)


def downgrade() -> None:
    op.drop_table("posts")
