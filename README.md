# project_django_celery_cassandra_rabbitmq
This is a Django project/app to show how to use cassadra with celery with default rabbitmq as the message broker. This project is a hit api server where one can post data in unicode ad the data gets stored in the cassandra database. This is a continuation project of my https://github.com/siddver007/project_django_allauth_slate_razorpay project. This is just an API. 

### NOTE:   
Celery doesn't usually directly work cassandra so you need to create and return a new session for cassadra. This is a basic workaround but you can improve this and also ping me by opening an issue on this repository.   
  

---
  
          
  
###                                                 HOW TO USE  
--- 

1. Clone the project or download the zip. Clone and download my other project         https://github.com/siddver007/project_django_allauth_slate_razorpay.  
2. Run the "project_django_allauth_slate_razorpay" project and register a user and get an Auth Token.
3. Go to settings.py and put your Cassandra database connection variables. Also put Celery's BROKER_URL and CELERY_RESULT_BACKEND by setting up RabbitMQ by following the link http://docs.celeryproject.org/en/latest/getting-started/brokers/rabbitmq.html.  
4. Go to tasks.py and enter "user_name", "password", "database_name", and "cassandra_keyspace". This "user_name", "password", and "database_name" is for the database you created for the "project_django_allauth_slate_razorpay" project.  
5. Now run command:-  
   a. python manage.py sync_cassandra    
6. Now run the app by typing in "python manage.py runserver 0.0.0.0:8001"
7. Try posting data in JSON format to http://localhost:8001/post/.   
   Data should have the format {"token":"{{YOUR_AUTH_TOKEN}}","data":"{{ANY_UNICODE_STRING}}"}.  

##### NOTE: You'll to verify your email which gets generated when you register the user using "project_django_allauth_slate_razorpay" project. The verification link is either sent to the provided e-mail or if SMTP settings are not specified then the e-mail gets generated in the CMD or Terminal. You could use any third party HTTP request client like "Postman" etc.  


## NOTE: There might be some issues so, you can open an issue on this repository if you want to ask something from me/ need my help. 

Cheers


  
  
  
  
   


