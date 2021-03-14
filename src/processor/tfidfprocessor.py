from src.processor.processorutils import ProcessorUtils


class TfIdfProcessor:
    limit = 0
    sampleBody = "<  Hi Sudarshan,Thanks for applying to Amazon! We've received your application for the position of " \
                 "Software Dev Engineer, Amazon Halo <  (ID: 1399549).What happens next?If we decide to move forward " \
                 "with your application, the Amazon recruiting team will reach out to you to discuss next steps. Any " \
                 "updates to your application status will be reflected on your Application dashboard < , so be sure " \
                 "to check back regularly.Go to your application dashboard <  Due to the high volume of applications " \
                 "we receive, we're unable to speak with everyone who applies, but we encourage you to continue " \
                 "exploring other career opportunities at Amazon < .If you'd like to learn more about our culture and " \
                 "peculiar ways, visit amazon.jobs < . Or you can get the latest Amazon news and stories by following " \
                 "our Day One blog < .Best regards,Amazon Recruiting TeamPlease do not reply to this email - we are " \
                 "unable to review or respond to messages at this address.     <   <   <   <   < [EXTERNAL EMAIL] DO " \
                 "NOT CLICK links or attachments unless you recognize the sender and know the content is safe. "

    def __init__(self, limit):
        self.limit = limit

    def process(self, messages=None):
        count = 0
        # for msg in messages:
        #     if count == self.limit:
        #         break
        print(ProcessorUtils.pre_process(self.sampleBody))
