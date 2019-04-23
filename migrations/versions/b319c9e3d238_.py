"""empty message

Revision ID: b319c9e3d238
Revises: 0a6b82b55983
Create Date: 2019-04-23 11:37:59.533097

"""
from alembic import op
import sqlalchemy as sa
import geoalchemy2
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b319c9e3d238'
down_revision = '0a6b82b55983'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('priorities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('project_id', sa.BigInteger(), nullable=True),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('geometry', geoalchemy2.types.Geometry(srid=4326), nullable=True),
    sa.Column('uploaded_by', sa.BigInteger(), nullable=True),
    sa.Column('uploaded_on', sa.DateTime(), nullable=False),
    sa.Column('filesize', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['project_id'], ['projects.id'], name='fk_priority_project'),
    sa.ForeignKeyConstraint(['uploaded_by'], ['users.id'], name='fk_users_uploader'),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('projects', sa.Column('selected_priorities', postgresql.ARRAY(sa.Integer()), nullable=True))
    op.alter_column('projects', 'task_creation_mode',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.add_column('tasks', sa.Column('priority', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tasks', 'priority')
    op.alter_column('projects', 'task_creation_mode',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_column('projects', 'selected_priorities')
    op.drop_table('priorities')
    # ### end Alembic commands ###