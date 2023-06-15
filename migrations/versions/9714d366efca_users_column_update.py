"""users column update

Revision ID: 9714d366efca
Revises: 28fd2035b9a1
Create Date: 2023-06-15 15:48:26.015125

"""
from datetime import datetime
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9714d366efca'
down_revision = '28fd2035b9a1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("users", sa.Column("created_at", sa.DateTime, nullable=False,
                  server_default=datetime.now().strftime("%Y-%m-%d %H:%M:%S")))


def downgrade() -> None:
    op.drop_column("users", "created_at")
