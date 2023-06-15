"""foreign keys

Revision ID: 28fd2035b9a1
Revises: 25c55abb53b4
Create Date: 2023-06-15 15:34:00.910270

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28fd2035b9a1'
down_revision = '25c55abb53b4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("user_id", sa.Integer, nullable=False))
    op.create_foreign_key("fk_posts_user", "posts", "users",
                          ["user_id"], ["id"])
    op.create_foreign_key("fk_vote_user", "votes",
                          "users", ["user_id"], ["id"])
    op.create_foreign_key("fk_vote_post", "votes",
                          "posts", ["post_id"], ["id"])


def downgrade() -> None:
    op.drop_column("posts", "user_id")
    op.drop_constraint("fk_posts_user", 'posts', 'foreignkey')
    op.drop_constraint("fk_vote_user", 'votes', 'foreignkey')
    op.drop_constraint("fk_vote_post", 'votes', 'foreignkey')
