import os
import logging
import mimetypes
import requests

from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from core.receive_mms import *


logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'receive_mms/index.html')


def config(request):
    return JsonResponse({'twilioPhoneNumber': os.getenv('TWILIO_NUMBER', '')})


def get_all_media(request):
    response = {'data': serializers.serialize('json', fetch_all_media())}
    return JsonResponse(response)


def delete_media_file(request, filename=None):
    try:
        media_content, mime_type = delete_media_file(filename)
    except MMSMedia.DoesNotExist as err:
        logger.error(err)
        return JsonResponse({
            'status': False,
            'message': 'Could not find any media file with name: {}'.format(filename)
          }, status=404)

    return HttpResponse(media_content, content_type=mime_type)


def reply_incoming_message(request):
    num_media = request.POST.get('NumMedia', 0)
    from_number = request.POST.get('From', '')
    message_sid = request.POST.get('MessageSid', '')
    media_files = [(request.POST.get("MediaUrl{}".format(i), ''),
                    request.POST.get("MediaContentType{}".format(i), ''))
                   for i in range(0, num_media)]

    response = reply_with_twiml_message(num_media, from_number, message_sid, media_files)
    return response
