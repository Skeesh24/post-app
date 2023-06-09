"""post_user_fk

Revision ID: 2645ee7622bd
Revises: eb1681e68b42
Create Date: 2023-06-09 14:56:01.925955

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2645ee7622bd'
down_revision = 'eb1681e68b42'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("user_id", sa.Integer, sa.ForeignKey(
        "users.id", ondelete="CASCADE", name="post_user_fk"
    ), nullable=False))


def downgrade() -> None:
    op.drop_constraint("post_user_fk", "posts")
    op.drop_column("posts", "user_id")
