"""votes table

Revision ID: 48ca20493a05
Revises: 2645ee7622bd
Create Date: 2023-06-09 15:00:45.984008

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48ca20493a05'
down_revision = '2645ee7622bd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("votes",
                    sa.Column("post_id", sa.Integer, sa.ForeignKey(
                        "posts.id", ondelete="CASCADE"), primary_key=True, nullable=False),
                    sa.Column("user_id", sa.Integer, sa.ForeignKey(
                        "users.id", ondelete="CASCADE"), primary_key=True, nullable=False),
                    )


def downgrade() -> None:
    op.drop_table("votes")
