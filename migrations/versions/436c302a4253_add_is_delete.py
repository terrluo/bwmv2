"""add is_delete

Revision ID: 436c302a4253
Revises: 7a615743cb3d
Create Date: 2022-05-17 18:46:54.279209

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '436c302a4253'
down_revision = '7a615743cb3d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('account_user', sa.Column('is_delete', sa.SmallInteger(), nullable=False, comment='是否删除 0否 1是'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('account_user', 'is_delete')
    # ### end Alembic commands ###
