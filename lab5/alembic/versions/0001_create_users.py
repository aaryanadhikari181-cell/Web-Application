"""create users table

Revision ID: 0001_create_users
Revises: 
Create Date: 2025-01-01 00:00:00.000000

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

revision: str = "0001_create_users"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id",              sa.Integer(),     nullable=False),
        sa.Column("full_name",       sa.String(100),   nullable=False),
        sa.Column("email",           sa.String(150),   nullable=False),
        sa.Column("hashed_password", sa.String(255),   nullable=False),
        sa.Column("is_active",       sa.Boolean(),     nullable=False, server_default="1"),
        sa.Column("created_at",      sa.DateTime(timezone=True), server_default=sa.text("(CURRENT_TIMESTAMP)")),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_users_id",    "users", ["id"],    unique=False)
    op.create_index("ix_users_email", "users", ["email"], unique=True)


def downgrade() -> None:
    op.drop_index("ix_users_email", table_name="users")
    op.drop_index("ix_users_id",    table_name="users")
    op.drop_table("users")
