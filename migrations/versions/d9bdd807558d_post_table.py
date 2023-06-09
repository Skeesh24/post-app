"""post table

Revision ID: d9bdd807558d
Revises: 
Create Date: 2023-06-09 14:45:05.702417

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd9bdd807558d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("posts",
                    sa.Column("id", sa.Integer,
                              primary_key=True, nullable=False),
                    sa.Column("title", sa.String(50), nullable=False),
                    sa.Column("published", sa.Boolean, nullable=False),
                    sa.Column("created_at", sa.DateTime(timezone=True),
                              nullable=False, server_default=sa.func.now())
                    )


def downgrade() -> None:
    op.drop_table('posts')
