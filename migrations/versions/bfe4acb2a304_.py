"""empty message

Revision ID: bfe4acb2a304
Revises: 59c170d304e0
Create Date: 2017-07-03 22:21:13.744323

"""

# revision identifiers, used by Alembic.
revision = 'bfe4acb2a304'
down_revision = '59c170d304e0'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('chess')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('chess',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('room', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('created_at', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('chess_board', mysql.LONGTEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    # ### end Alembic commands ###
