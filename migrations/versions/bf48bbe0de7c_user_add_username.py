"""user add username

Revision ID: bf48bbe0de7c
Revises: e7fe4e0d4ab8
Create Date: 2022-05-17 17:52:20.898182

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "bf48bbe0de7c"
down_revision = "e7fe4e0d4ab8"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "account_user",
        sa.Column("username", sa.String(length=16), nullable=False, comment="用户名"),
    )
    op.create_unique_constraint(
        op.f("uq_account_user_username"), "account_user", ["username"]
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f("uq_account_user_username"), "account_user", type_="unique")
    op.drop_column("account_user", "username")
    # ### end Alembic commands ###
