"""reviews

Revision ID: 690e22a5f6ef
Revises: 04b4a54ca034
Create Date: 2025-06-09 16:02:04.501781

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '690e22a5f6ef'
down_revision: Union[str, None] = '04b4a54ca034'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('text', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_DATE'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reviews')
    # ### end Alembic commands ###
