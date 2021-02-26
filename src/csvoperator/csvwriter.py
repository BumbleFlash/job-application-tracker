import csv
from src.csvoperator.csvutils import CsvUtils


class CsvWriter:

    @staticmethod
    def write_few(messages, limit):
        with open('data/first_' + str(limit) + '_emails.csv', 'w', newline='', encoding='utf-8') as csvfile:
            headers = ['Sender', 'Sender_Email', 'Subject', 'Body', 'Time']
            writer = csv.DictWriter(csvfile, fieldnames=headers)
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
