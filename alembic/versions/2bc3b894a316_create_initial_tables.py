"""create initial tables

Revision ID: 2bc3b894a316
Revises: 
Create Date: 2025-08-01 15:04:16.094591

"""
from sqlalchemy.dialects import postgresql
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2bc3b894a316'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.create_table(
        'votos',
        sa.Column('id_voto', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('id_eleicao', sa.String(length=50), nullable=False),
        sa.Column('id_candidato', sa.String(length=50), nullable=False),
        sa.Column('hash_voto', sa.String(length=64), nullable=False, unique=True),
        sa.Column('data_voto', sa.DateTime(), nullable=False, server_default=sa.text('NOW()')),
    )
    op.create_table(
        'registro_votantes',
        sa.Column('id_registro_voto', sa.Integer(), primary_key=True),
        sa.Column('id_eleicao', sa.String(length=50), nullable=False),
        sa.Column('id_eleitor', sa.Integer(), nullable=False),
        sa.Column('data_registro', sa.DateTime(), nullable=False, server_default=sa.text('NOW()')),
        sa.UniqueConstraint('id_eleitor', 'id_eleicao', name='uq_eleitor_eleicao'),
    )

def downgrade() -> None:
    op.drop_table('registro_votantes')
    op.drop_table('votos')
