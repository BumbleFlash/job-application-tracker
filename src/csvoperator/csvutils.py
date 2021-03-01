import re


class CsvUtils:

    @staticmethod
    def clean_msg_body(body):
        # removes URLS
        body = re.sub(r'http\S+', '', body)
        # removes carriage returns, line breaks and horizontal tabs
        return body.replace('\r', '').replace('\n', '').replace('\t', '')
