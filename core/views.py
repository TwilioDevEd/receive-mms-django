import os
import sys
import logging
import mimetypes
import requests

from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from core.receive_mms import *


logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'receive_mms/index.html')


def config(_):
    return JsonResponse({'twilioPhoneNumber': os.getenv('TWILIO_NUMBER', '')})


def get_all_media(_):
    response = {'data': serializers.serialize('json', fetch_all_media())}
    return JsonResponse(response)


# /images/:filename
@csrf_exempt
def delete_media_file(_, filename=None):
    try:
        media_content, mime_type = delete_media_file(filename)
        return HttpResponse(media_content, content_type=mime_type)
    except MMSMedia.DoesNotExist as err:
        logger.error(err)
        return JsonResponse({
            'status': False,
            'message': 'Could not find any media file with name: {}'.format(filename)
          }, status=404)


# /incoming/
@csrf_exempt
def handle_incoming_message(request):
    message_sid = request.POST.get('MessageSid', '')
    from_number = request.POST.get('From', '')
    num_media = int(request.POST.get('NumMedia', 0))

    media_files = [(request.POST.get("MediaUrl{}".format(i), ''),
                    request.POST.get("MediaContentType{}".format(i), ''))
                   for i in range(0, num_media)]

    response = reply_with_twiml_message(message_sid, from_number, num_media, media_files)
    return HttpResponse(response, content_type='application/xml')
