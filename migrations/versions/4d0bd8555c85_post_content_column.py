"""post content column

Revision ID: 4d0bd8555c85
Revises: ee2696ba5fe7
Create Date: 2023-06-09 15:12:59.159940

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d0bd8555c85'
down_revision = 'ee2696ba5fe7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column(
        "content", sa.String(400), nullable=False))


def downgrade() -> None:
    op.drop_column("posts", "content")
