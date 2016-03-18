# Cassandra imports
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

import datetime
from uuid import uuid1, uuid4

# Mongo imports
from django.conf import settings


# Data model to create a data collection
class Data(Model):
	uid = columns.UUID(primary_key = True, default = uuid4)
	auth_token = columns.Text(max_length=100, required = True)
	content = columns.Text(required = True)