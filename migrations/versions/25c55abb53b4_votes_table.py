"""votes table

Revision ID: 25c55abb53b4
Revises: 1344476b5f9e
Create Date: 2023-06-15 14:58:30.840661

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25c55abb53b4'
down_revision = '1344476b5f9e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("votes",
                    sa.Column("user_id", sa.Integer,
                              nullable=False),
                    sa.Column("post_id", sa.Integer,
                              nullable=False),
                    )
    op.create_primary_key("pk_votes", "votes", ["user_id", "post_id"])


def downgrade() -> None:
    op.drop_constraint("pk_votes", "votes", "primary")
    op.drop_table("votes")
