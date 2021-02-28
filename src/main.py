from src.csvoperator.csvwriter import CsvWriter
from src.extractor.outlook_extractor import OutlookExtractor

extractor = OutlookExtractor()
CsvWriter.write_few(extractor.extract_data(), 200)
