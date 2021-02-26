import win32com.client
import re
from src.constants import email_constants


class OutlookExtractor(object):

    def to_suppress_static_warning(self):
        pass

    def extract_data(self):
        outlook = win32com.client.Dispatch(email_constants.OUTLOOK_APPLICATION).GetNamespace(
            email_constants.MAPI_NAMESPACE)
        inbox = outlook.GetDefaultFolder(email_constants.INBOX_FOLDER)
        messages = inbox.Items
        message = messages.GetLast()
        print(self.remove_links(message.body))

    def remove_links(self, body):
        self.to_suppress_static_warning()
        return re.sub(r'http\S+', '', body)
