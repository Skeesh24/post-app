"""posts foreign key

Revision ID: 3eb7271cefe2
Revises: 9808a5413488
Create Date: 2023-06-10 00:28:17.401081

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3eb7271cefe2'
down_revision = '9808a5413488'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_foreign_key("posts_users_fk", "posts",
                          "users", ['user_id'], ['id'], ondelete="CASCADE")


def downgrade() -> None:
    op.drop_constraint("posts_users_fk", 'posts', 'foreignkey')
