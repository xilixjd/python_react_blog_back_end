"""empty message

Revision ID: 8a5b1dec9693
Revises: d24b3245969f
Create Date: 2017-03-23 10:53:24.059664

"""

# revision identifiers, used by Alembic.
revision = '8a5b1dec9693'
down_revision = 'd24b3245969f'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('sender', sa.String(length=255), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('messages', 'sender')
    ### end Alembic commands ###