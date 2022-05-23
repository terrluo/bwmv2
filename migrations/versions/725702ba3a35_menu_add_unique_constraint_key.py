"""menu add unique constraint key

Revision ID: 725702ba3a35
Revises: 8ebac08cbeca
Create Date: 2022-05-21 23:45:34.684124

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "725702ba3a35"
down_revision = "8ebac08cbeca"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(
        op.f("uq_menu_menu_parent_id"),
        "menu_menu",
        ["parent_id", "menu_type", "menu_name"],
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f("uq_menu_menu_parent_id"), "menu_menu", type_="unique")
    # ### end Alembic commands ###
