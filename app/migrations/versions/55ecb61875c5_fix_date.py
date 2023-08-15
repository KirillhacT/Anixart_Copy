"""fix date

Revision ID: 55ecb61875c5
Revises: ab34aaa5f624
Create Date: 2023-08-15 08:47:49.029321

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '55ecb61875c5'
down_revision = 'ab34aaa5f624'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('test', sa.Float(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'test')
    # ### end Alembic commands ###