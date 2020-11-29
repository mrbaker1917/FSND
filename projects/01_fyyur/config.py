import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgres://zwgefnbg:K5hk0evwHTD_hMsp4eaP_vEJzswOQPHq@lallah.db.elephantsql.com:5432/zwgefnbg'
