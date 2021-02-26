import re


class CsvUtils:

    @staticmethod
    def remove_links(body):
        return re.sub(r'http\S+', '', body)
