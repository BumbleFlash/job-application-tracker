import re


class ProcessorUtils:
    @staticmethod
    def pre_process(body):
        body = re.sub("&lt;/?.*?&gt;", " &lt;&gt ", body)  # removes tags
        return re.sub(r'http\S+', '', body)  # remove urls
