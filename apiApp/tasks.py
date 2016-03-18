from __future__ import absolute_import
from celery import shared_task
import sched, time, math
from celery import task
from apiApp.models import *
import datetime
import threading
from cassandra.cqlengine import connection
from cassandra.cqlengine.connection import cluster , session
from cassandra.cluster import Cluster


# For raw requests to Register Project's Tables
from sqlalchemy import create_engine
engine = create_engine('postgresql://{{user_name}}:{{password}}@localhost/{{database_name}}')


# For creating a new session
thread_local = threading.local()

def get_session():
    if hasattr(thread_local, "cassandra_session"):
        return thread_local.cassandra_session

    cluster1 = Cluster({'127.0.0.1'})
    session = cluster1.connect('{{cassandra_keyspace}}')

    thread_local.cassandra_session = session

    return session

@task
def saveDb(token, data):
	try:
		get_session()
	except Exception:
		print 'Some error with getting the session'	

	try:
		# Check whether user exists
		user = engine.execute("select * from \"registerApp_customuser\" where auth_token=%s", (token,) ).fetchone()
		no_user_condition_auth_token = user['auth_token']

		user_email_address = user['email']
		email = engine.execute("select * from account_emailaddress where email=%s", (user_email_address,) ).fetchone()

		# Check whether user's e-mail has been verified or not
		if email.verified == True:

			# Check whether the posted data is unicode and if not then convert it to unicode
			try:
				finalData = data.decode('unicode-escape')
			except UnicodeEncodeError:
				finalData = data	
				
			# Flow for Free-plan users
			if user['plan'] == 'Free':
				if user['date_joined'].date() == datetime.datetime.now().date():
					if user['counter'] < 100:
						data = Data()
						data.auth_token = no_user_condition_auth_token
						data.content = finalData
						data.save()
						engine.execute("update \"registerApp_customuser\" set counter=%s where auth_token=%s", (user['counter'] + 1, no_user_condition_auth_token) )
						return 's101'
					else:
						return 'e101'	
				else:
					data = Data()
					data.auth_token = no_user_condition_auth_token
					data.content = finalData
					data.save()
					engine.execute("update \"registerApp_customuser\" set date_joined=%s where auth_token=%s", (datetime.datetime.now(), no_user_condition_auth_token) )
					engine.execute("update \"registerApp_customuser\" set counter=%s where auth_token=%s", (1, no_user_condition_auth_token) )
					return 's101'
			
			# Flow for Gold-plan users
			elif user.plan == 'Gold':
				if user['date_joined'].date() == datetime.datetime.now().date():
					if user.counter < 1000:
						data = Data()
						data.auth_token = no_user_condition_auth_token
						data.content = finalData
						data.save()
						engine.execute("update \"registerApp_customuser\" set counter=%s where auth_token=%s", (user['counter'] + 1, no_user_condition_auth_token) )
						return 's101'
					else:
						return 'e101'	
				else:
					data = Data()
					data.auth_token = no_user_condition_auth_token
					data.content = finalData
					data.save()
					engine.execute("update \"registerApp_customuser\" set date_joined=%s where auth_token=%s", (datetime.datetime.now(), no_user_condition_auth_token) )
					engine.execute("update \"registerApp_customuser\" set counter=%s where auth_token=%s", (1, no_user_condition_auth_token) )
					return 's101'	
			
			# Flow for Platinum-plan users
			elif user.plan == 'Platinum':
				data = Data()
				data.auth_token = no_user_condition_auth_token
				data.content = finalData
				data.save()
				engine.execute("update \"registerApp_customuser\" set counter=%s where auth_token=%s", (user['counter'] + 1, no_user_condition_auth_token) )
				return 's101'
			
			else:
				return 'e102'	
		
		else:
			return 'e103'
	
	except TypeError:
		return 'e104'



@task
def hitApi(hell):
    data = Data()
    data.user_id = 'sid'
    data.content = 'bloooo00'
    data.save()
    return 'OK'    