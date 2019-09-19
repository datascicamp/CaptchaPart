"""Captcha matching

Revision ID: 3cb6673ad55e
Revises: 
Create Date: 2019-09-19 12:17:10.210326

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3cb6673ad55e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('CaptchaMatching',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hash_code', sa.String(length=64), nullable=True),
    sa.Column('captcha_code', sa.String(length=120), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_CaptchaMatching_captcha_code'), 'CaptchaMatching', ['captcha_code'], unique=True)
    op.create_index(op.f('ix_CaptchaMatching_hash_code'), 'CaptchaMatching', ['hash_code'], unique=True)
    op.create_index(op.f('ix_CaptchaMatching_timestamp'), 'CaptchaMatching', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_CaptchaMatching_timestamp'), table_name='CaptchaMatching')
    op.drop_index(op.f('ix_CaptchaMatching_hash_code'), table_name='CaptchaMatching')
    op.drop_index(op.f('ix_CaptchaMatching_captcha_code'), table_name='CaptchaMatching')
    op.drop_table('CaptchaMatching')
    # ### end Alembic commands ###