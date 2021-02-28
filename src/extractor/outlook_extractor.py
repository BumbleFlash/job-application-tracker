import win32com.client
from src.constants import email_constants


class OutlookExtractor(object):

    def to_suppress_static_warning(self):
        pass

    def extract_data(self):
        self.to_suppress_static_warning()
        outlook = win32com.client.Dispatch(email_constants.OUTLOOK_APPLICATION).GetNamespace(
            email_constants.MAPI_NAMESPACE)
        inbox = outlook.GetDefaultFolder(email_constants.INBOX_FOLDER)
        messages = inbox.Items
        messages.Sort("[ReceivedTime]", True)
        return messages
