"""votes table

Revision ID: 09d83d2eb56b
Revises: 3eb7271cefe2
Create Date: 2023-06-10 00:32:07.507766

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09d83d2eb56b'
down_revision = '3eb7271cefe2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("votes",
                    op.Column("post_id", sa.Integer, sa.ForeignKey(
                        "posts.id", ondelete="CASCADE"), primary_key=True),
                    op.Column("user_id", sa.Integer, sa.ForeignKey(
                        "users.id", ondelete="CASCADE"), primary_key=True),)


def downgrade() -> None:
    op.drop_table("votes")
