import pytest

from src.extractor.outlook_extractor import OutlookExtractor


def test_extract_data():
    messages = OutlookExtractor().extract_data()
    length = len(messages)
    assert messages[length - 1].SenderEmailAddress == "notifications@instructure.com"
