from src.csvoperator.csvwriter import CsvUtils


def test_clean_message():
    test_message = " Hi \t <https://www.linkedin.com/in/sudarshansampathkumar/> \n "
    assert CsvUtils.clean_msg_body(test_message) == " Hi  <  "
