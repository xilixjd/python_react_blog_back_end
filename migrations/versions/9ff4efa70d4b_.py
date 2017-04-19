"""empty message

Revision ID: 9ff4efa70d4b
Revises: 31a3569b6369
Create Date: 2017-04-07 11:43:35.939601

"""

# revision identifiers, used by Alembic.
revision = '9ff4efa70d4b'
down_revision = '31a3569b6369'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('zan', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comments', 'zan')
    # ### end Alembic commands ###