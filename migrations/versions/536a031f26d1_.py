"""empty message

Revision ID: 536a031f26d1
Revises: 0b6ad755fb54
Create Date: 2023-06-30 12:01:28.959099

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '536a031f26d1'
down_revision = '0b6ad755fb54'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('borrowed',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('on_shelf', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('borrowed', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_borrowed_on_shelf'), ['on_shelf'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('borrowed', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_borrowed_on_shelf'))

    op.drop_table('borrowed')
    # ### end Alembic commands ###
