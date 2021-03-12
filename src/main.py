from src.extractor.outlook_extractor import OutlookExtractor
from src.processor.tfidfprocessor import TfIdfProcessor

extractor = OutlookExtractor()
messages = extractor.extract_data()
# CsvWriter.write_few(messages, 200)
TfIdfProcessor(1).process(messages)
