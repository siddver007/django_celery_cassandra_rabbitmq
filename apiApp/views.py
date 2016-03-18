from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
import json
from models import *

# Celery imports
from tasks import saveDb, hitApi




# View to post data by registered users
class postView(TemplateView):
	template_name = 'user_post.html'
	
	def post(self,req):
		received_json_data = req.body
		processed_data = json.loads(received_json_data)
		if 'token' in processed_data.keys() and 'data' in processed_data.keys() and len(processed_data.keys()) == 2:
			res = saveDb.delay(processed_data['token'], processed_data['data'])
			code = res.get()
			if code == 's101':
				return JsonResponse({'code':'200','success':'Data successfully posted'})
			elif code == 'e101':
				return JsonResponse({'code':'503', 'error':'API rate limit exceeded for today'})
			elif code == 'e102':
				return JsonResponse({'code':'500', 'error':'Some error occurred. Please try again.'})
			elif code == 'e103':
				return JsonResponse({'code':'404', 'error':'User not verified. Please verify your e-mail.'})
			elif code == 'e104'	:
				return JsonResponse({'code':'401', 'error':'Invalid user credentials. Please try again.'})
		else:
			return JsonResponse({'code':'400', 'error':'Please check the request you made.'})		



def registerView(req):
	return HttpResponseRedirect('http://localhost:8000/')
