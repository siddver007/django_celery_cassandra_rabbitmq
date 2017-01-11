# django_celery_cassandra_rabbitmq
A Django example-project to show how to use cassadra with celery(with rabbitmq as the message broker). It creates an API server where one can post unicode data which gets stored in a Cassandra database. This project is a continuation of my https://github.com/siddver007/django_allauth_slate_razorpay project. This project only exposes an API and not any UI. 

**NOTE:**   
Celery usually doesn't work directly with cassandra. So, you need to create and return a new session for cassadra. This is a basic workaround but you can improve this and also ping me by opening an issue on this repository.   
  

         
  
## HOW TO USE  

1. Clone this project. Clone my other project https://github.com/siddver007/django_allauth_slate_razorpay.  
2. Firstly, run "django_allauth_slate_razorpay" project, register a user and get an Auth Token.
3. Go to settings.py of this project and put your Cassandra database connection variables. Also put Celery's BROKER_URL and CELERY_RESULT_BACKEND by setting up RabbitMQ(Follow this link http://docs.celeryproject.org/en/latest/getting-started/brokers/rabbitmq.html for help). 
4. Go to tasks.py of this project and fill "user_name", "password", "database_name", and "cassandra_keyspace". This "user_name", "password", and "database_name" is for the database you created for the "django_allauth_slate_razorpay" project.  
5. Now run command:-  
   a. python manage.py sync_cassandra    
6. Now run the app by typing in "python manage.py runserver 0.0.0.0:8001"
7. Try posting data in JSON format to http://localhost:8001/post/.   
   Data should have the format {"token":"{{YOUR_AUTH_TOKEN}}","data":"{{ANY_UNICODE_STRING}}"}.  

**NOTE: You'll to verify your email which gets generated when you register the user using "django_allauth_slate_razorpay" project. You can find the verification link in the logs or your e-mail inbox.**  


**NOTE: There might be some issues so, you can open an issue on this repository if you want to ask something from me/ need my help.** 

Cheers


  
  
  
  
   


