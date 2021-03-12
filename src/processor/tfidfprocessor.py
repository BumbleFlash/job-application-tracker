from src.processor.processorutils import ProcessorUtils


class TfIdfProcessor:
    limit = 0

    def __init__(self, limit):
        self.limit = limit

    def process(self, messages):
        count = 0
        for msg in messages:
            if count == self.limit:
                break
        print(ProcessorUtils.pre_process(messages[8].body))
