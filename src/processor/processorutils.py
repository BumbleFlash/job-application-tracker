import re


class ProcessorUtils:
    @staticmethod
    def pre_process(body):
        body = re.sub("&lt;/?.*?&gt;", " &lt;&gt ", body)  # removes tags
        body = body.replace('\r', '').replace('\n', '').replace('\t', '')  # removes breaks and returns
        body = body.replace("<", "")
        return re.sub(r'http\S+', '', body)  # remove urls
