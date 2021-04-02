from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

from src.processor.processorutils import ProcessorUtils


class TfIdfProcessor:
    limit = 0
    sampleBody = "< Software Engineer Hi Sudarshan,Thanks for applying to Amazon! We've received your application for the position of " \
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
        pre_processed_body = ProcessorUtils.pre_process(self.sampleBody)
        stopwords = ProcessorUtils.get_stop_words("../resources/stopwords.txt")
        cv = CountVectorizer(max_df=1, stop_words=stopwords)
        word_count_vector = cv.fit_transform([pre_processed_body])

        tfidf_transformer = TfidfTransformer(norm='l2', smooth_idf=True, sublinear_tf=False, use_idf=True)
        tfidf_transformer.fit(word_count_vector)

        feature_names = cv.get_feature_names()
        tfidf_vector = tfidf_transformer.transform(cv.transform([pre_processed_body]))
        sorted_items = ProcessorUtils.sort_coo(tfidf_vector.tocoo())
        keywords = ProcessorUtils.extract_top_n_from_vector(feature_names, sorted_items, 50)
        for k in keywords:
            print(k, keywords[k])
