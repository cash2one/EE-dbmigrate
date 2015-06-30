"""Add a column

Revision ID: 37d1722a4621
Revises: None
Create Date: 2015-06-26 10:08:07.026259

"""

# revision identifiers, used by Alembic.
revision = '37d1722a4621'
down_revision = None

from alembic import op
import sqlalchemy as sa

def upgrade():
    op.add_column('sites', sa.Column('redis', sa.DateTime))


def downgrade():
    with op.batch_alter_table("sites") as batch_op:
    	batch_op.drop_column('redis')


# Output
# ========
# root@vagrant-ubuntu-trusty-64:/vagrant/dbmigrate/easyengine# sqlite3 /var/lib/ee/ee.db
# SQLite version 3.8.2 2013-12-06 14:53:30
# Enter ".help" for instructions
# Enter SQL statements terminated with a ";"
# sqlite> .schema sites
# CREATE TABLE sites (
#         id INTEGER NOT NULL, 
#         sitename VARCHAR, 
#         site_type VARCHAR, 
#         cache_type VARCHAR, 
#         site_path VARCHAR, 
#         created_on DATETIME, 
#         is_enabled BOOLEAN NOT NULL, 
#         is_ssl BOOLEAN, 
#         storage_fs VARCHAR, 
#         storage_db VARCHAR, 
#         db_name VARCHAR, 
#         db_user VARCHAR, 
#         db_password VARCHAR, 
#         db_host VARCHAR, 
#         is_hhvm BOOLEAN, 
#         is_pagespeed BOOLEAN,
#         PRIMARY KEY (id), 
#         UNIQUE (sitename), 
#         CHECK (is_enabled IN (0, 1)), 
#         CHECK (is_ssl IN (0, 1)), 
#         CHECK (is_hhvm IN (0, 1)), 
#         CHECK (is_pagespeed IN (0, 1))
# );
# sqlite> 
# root@vagrant-ubuntu-trusty-64:/vagrant/dbmigrate/easyengine# alembic upgrade 37d1722a4621
# INFO  [alembic.migration] Context impl SQLiteImpl.
# INFO  [alembic.migration] Will assume non-transactional DDL.
# INFO  [alembic.migration] Running upgrade  -> 37d1722a4621, Add a column
# root@vagrant-ubuntu-trusty-64:/vagrant/dbmigrate/easyengine# sqlite3 /var/lib/ee/ee.db
# SQLite version 3.8.2 2013-12-06 14:53:30
# Enter ".help" for instructions
# Enter SQL statements terminated with a ";"
# sqlite> .schema sites
# CREATE TABLE sites (
#         id INTEGER NOT NULL, 
#         sitename VARCHAR, 
#         site_type VARCHAR, 
#         cache_type VARCHAR, 
#         site_path VARCHAR, 
#         created_on DATETIME, 
#         is_enabled BOOLEAN NOT NULL, 
#         is_ssl BOOLEAN, 
#         storage_fs VARCHAR, 
#         storage_db VARCHAR, 
#         db_name VARCHAR, 
#         db_user VARCHAR, 
#         db_password VARCHAR, 
#         db_host VARCHAR, 
#         is_hhvm BOOLEAN, 
#         is_pagespeed BOOLEAN, redis DATETIME,
#         PRIMARY KEY (id), 
#         UNIQUE (sitename), 
#         CHECK (is_enabled IN (0, 1)), 
#         CHECK (is_ssl IN (0, 1)), 
#         CHECK (is_hhvm IN (0, 1)), 
#         CHECK (is_pagespeed IN (0, 1))
# );
# sqlite> 
# root@vagrant-ubuntu-trusty-64:/vagrant/dbmigrate/easyengine# alembic downgrade -1
# INFO  [alembic.migration] Context impl SQLiteImpl.
# INFO  [alembic.migration] Will assume non-transactional DDL.
# INFO  [alembic.migration] Running downgrade 37d1722a4621 -> , Add a column
# root@vagrant-ubuntu-trusty-64:/vagrant/dbmigrate/easyengine# sqlite3 /var/lib/ee/ee.db
# SQLite version 3.8.2 2013-12-06 14:53:30
# Enter ".help" for instructions
# Enter SQL statements terminated with a ";"
# sqlite> .schema sites
# CREATE TABLE sites (
#         id INTEGER NOT NULL, 
#         sitename VARCHAR, 
#         site_type VARCHAR, 
#         cache_type VARCHAR, 
#         site_path VARCHAR, 
#         created_on DATETIME, 
#         is_enabled BOOLEAN NOT NULL, 
#         is_ssl BOOLEAN, 
#         storage_fs VARCHAR, 
#         storage_db VARCHAR, 
#         db_name VARCHAR, 
#         db_user VARCHAR, 
#         db_password VARCHAR, 
#         db_host VARCHAR, 
#         is_hhvm BOOLEAN, 
#         is_pagespeed BOOLEAN,
#         PRIMARY KEY (id), 
#         UNIQUE (sitename), 
#         CHECK (is_enabled IN (0, 1)), 
#         CHECK (is_ssl IN (0, 1)), 
#         CHECK (is_hhvm IN (0, 1)), 
#         CHECK (is_pagespeed IN (0, 1))
# );
# sqlite> 
# root@vagrant-ubuntu-trusty-64:/vagrant/dbmigrate/easyengine# 
