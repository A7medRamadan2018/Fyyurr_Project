"""empty message

Revision ID: 120c5cdcb3d3
Revises: ea6241e8d734
Create Date: 2020-09-16 20:21:55.408473

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '120c5cdcb3d3'
down_revision = 'ea6241e8d734'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('genres_artist_artist_id_fkey', 'genres_artist', type_='foreignkey')
    op.create_foreign_key(None, 'genres_artist', 'Artist', ['artist_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('genres_venue_venue_id_fkey', 'genres_venue', type_='foreignkey')
    op.create_foreign_key(None, 'genres_venue', 'Venue', ['venue_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('show_artist_id_fkey', 'show', type_='foreignkey')
    op.drop_constraint('show_venue_id_fkey', 'show', type_='foreignkey')
    op.create_foreign_key(None, 'show', 'Venue', ['venue_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'show', 'Artist', ['artist_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'show', type_='foreignkey')
    op.drop_constraint(None, 'show', type_='foreignkey')
    op.create_foreign_key('show_venue_id_fkey', 'show', 'Venue', ['venue_id'], ['id'])
    op.create_foreign_key('show_artist_id_fkey', 'show', 'Artist', ['artist_id'], ['id'])
    op.drop_constraint(None, 'genres_venue', type_='foreignkey')
    op.create_foreign_key('genres_venue_venue_id_fkey', 'genres_venue', 'Venue', ['venue_id'], ['id'])
    op.drop_constraint(None, 'genres_artist', type_='foreignkey')
    op.create_foreign_key('genres_artist_artist_id_fkey', 'genres_artist', 'Artist', ['artist_id'], ['id'])
    # ### end Alembic commands ###
