"""create users and todos tables

Revision ID: 0001_create_users_todos
Revises:
Create Date: 2025-01-01 00:00:00.000000

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

revision: str = "0001_create_users_todos"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ── users ──────────────────────────────────────────────
    op.create_table(
        "users",
        sa.Column("id",              sa.Integer(),    nullable=False),
        sa.Column("full_name",       sa.String(100),  nullable=False),
        sa.Column("email",           sa.String(150),  nullable=False),
        sa.Column("hashed_password", sa.String(255),  nullable=False),
        sa.Column("is_active",       sa.Boolean(),    nullable=False, server_default="1"),
        sa.Column("created_at",      sa.DateTime(timezone=True),
                  server_default=sa.text("(CURRENT_TIMESTAMP)")),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_users_id",    "users", ["id"],    unique=False)
    op.create_index("ix_users_email", "users", ["email"], unique=True)

    # ── todos ──────────────────────────────────────────────
    op.create_table(
        "todos",
        sa.Column("id",          sa.Integer(),   nullable=False),
        sa.Column("title",       sa.String(200), nullable=False),
        sa.Column("description", sa.Text(),      nullable=True),
        sa.Column("completed",   sa.Boolean(),   nullable=False, server_default="0"),
        sa.Column("user_id",     sa.Integer(),   nullable=False),
        sa.Column("created_at",  sa.DateTime(timezone=True),
                  server_default=sa.text("(CURRENT_TIMESTAMP)")),
        sa.Column("updated_at",  sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_todos_id",      "todos", ["id"],      unique=False)
    op.create_index("ix_todos_user_id", "todos", ["user_id"], unique=False)


def downgrade() -> None:
    op.drop_index("ix_todos_user_id", table_name="todos")
    op.drop_index("ix_todos_id",      table_name="todos")
    op.drop_table("todos")
    op.drop_index("ix_users_email",   table_name="users")
    op.drop_index("ix_users_id",      table_name="users")
    op.drop_table("users")
