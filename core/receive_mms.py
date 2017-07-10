import os
import mimetypes
import requests

from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from core.models import MMSMedia

# Python 2 and 3: alternative 4
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse


def reply_with_twiml_message(num_media, from_number, message_sid, media_files):
    if not from_number or not message_sid:
        raise Exception('Please provide a From Number and a Message Sid')

    for (media_url, mime_type) in media_files:
        file_extension = mimetypes.guess_extension(mime_type)
        media_sid = os.path.basename(urlparse(media_url).path)
        content = requests.get(media_url).text
        filename = '{sid}.{ext}'.format(sid=media_sid, ext=file_extension)

        mms_media = MMSMedia(
            filename=filename,
            mime_type=mime_type,
            media_sid=media_sid,
            message_sid=message_sid,
            media_url=media_url,
            content=content)
        mms_media.save()

    response = MessagingResponse()
    message = 'Send us an image!' if not num_media else 'Thanks for the {} images.'.format(num_media)
    response.message(body=message, to=from_number, from_=os.getenv('TWILIO_NUMBER'))
    return response


def delete_media_file(filename=None):
    m = MMSMedia.objects.get(filename=filename)
    twilio_client().api.messages(m.message_sid) \
        .media(m.media_sid) \
        .delete()
    m.delete()

    return m.content, m.mime_type


def fetch_all_media():
    return MMSMedia.objects.all()


def twilio_client():
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')

    return Client(account_sid, auth_token)
