import csv
from src.csvoperator.csvutils import CsvUtils
from src.os.osutils import OsUtils


class CsvWriter:

    @staticmethod
    def write_few(messages, limit):

        OsUtils.create_directory_if_not_exists("data")

        with open('data/first_' + str(limit) + '_emails.csv', 'w', newline='', encoding='utf-8') as csvFile:
            headers = ['Sender', 'Sender_Email', 'Subject', 'Body', 'Time']
            writer = csv.DictWriter(csvFile, fieldnames=headers)
            writer.writeheader()
            count = 1
            for message in messages:
                if count == limit:
                    break
                data = {'Sender': message.SenderName, 'Sender_Email': message.SenderEmailAddress,
                        'Subject': message.Subject, 'Body': CsvUtils.remove_links(message.Body),
                        'Time': message.ReceivedTime}
                print(data)
                count += 1
                writer.writerow(data)
