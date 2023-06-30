"""authors table and relation to books

Revision ID: 0b6ad755fb54
Revises: a49fbd0d7cd3
Create Date: 2023-06-30 11:31:21.149962

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b6ad755fb54'
down_revision = 'a49fbd0d7cd3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('author', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_author_name'), ['name'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('author', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_author_name'))

    op.drop_table('author')
    # ### end Alembic commands ###
