"""empty message

Revision ID: ff6d307591b4
Revises: e0059fa95a84
Create Date: 2020-08-03 16:59:54.460813

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff6d307591b4'
down_revision = 'e0059fa95a84'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('url_image', sa.String(length=256), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'url_image')
    # ### end Alembic commands ###
