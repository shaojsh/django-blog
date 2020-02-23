from django.shortcuts import render
from django.http import JsonResponse,HttpResponse,HttpRequest,HttpResponseBadRequest
import json
import logging
import simplejson
# Create your views here.

def reg(request:HttpRequest):
    try:
        # payload = json.loads(request.body.decode())
        payload = simplejson.loads(request.body)
        # email = payload['email']
        return HttpResponse('welcome to shanghai')
    except Exception as e:
        logging.info(e)
    return HttpResponseBadRequest()

