"""empty message

Revision ID: ea1e70083a1f
Revises: 7177a96a5c18
Create Date: 2024-03-01 21:10:43.941231

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea1e70083a1f'
down_revision = '7177a96a5c18'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blacklistedTokens',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('jti', sa.String(length=36), nullable=False),
    sa.Column('creationDate', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('blacklistedTokens', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_blacklistedTokens_jti'), ['jti'], unique=False)

    op.create_table('motor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('esp32pin', sa.String(length=2), nullable=False),
    sa.Column('pinFunction', sa.String(length=200), nullable=True),
    sa.Column('pinName', sa.String(length=200), nullable=True),
    sa.Column('switchState', sa.String(length=2), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('esp32pin'),
    sa.UniqueConstraint('pinFunction'),
    sa.UniqueConstraint('pinName')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=150), nullable=False),
    sa.Column('email', sa.String(length=150), nullable=False),
    sa.Column('role', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(length=150), nullable=False),
    sa.Column('token', sa.String(length=5000), nullable=True),
    sa.Column('otp', sa.String(length=6), nullable=True),
    sa.Column('verifiedEmail', sa.String(length=5), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('motor')
    with op.batch_alter_table('blacklistedTokens', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_blacklistedTokens_jti'))

    op.drop_table('blacklistedTokens')
    # ### end Alembic commands ###
