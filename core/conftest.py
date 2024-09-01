# It has to be next to the manage.py file.

import os

os.environ['PYTEST_RUNNING'] = 'true'

from app.tests.fixtures import *
