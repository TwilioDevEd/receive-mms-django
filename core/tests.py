from django.test import TestCase
from core.receive_mms import reply_with_twiml_message, delete_media_file, fetch_all_media


class ReceiveMmsTestCase(TestCase):
    def test_reply_with_twiml_message(self):
        self.assertRaises(Exception, reply_with_twiml_message(None, None, None, None))
        pass
