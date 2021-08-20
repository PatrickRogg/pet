from data.data_fetcher import load_data
import csv

FOLDER = 'input/'
# Set this to the name of the file containing the train examples
TRAIN_FILE_NAME = "train.csv"

# Set this to the name of the file containing the dev examples
DEV_FILE_NAME = "dev.csv"

# Set this to the name of the file containing the test examples
TEST_FILE_NAME = "test.csv"

# Set this to the name of the file containing the unlabeled examples
UNLABELED_FILE_NAME = "unlabeled.csv"

header = ['label', 'sentence', 'company']
company_to_sentences = load_data()


def create_input_files():
    with open(FOLDER + UNLABELED_FILE_NAME, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        for company in company_to_sentences:
            for sentence in company_to_sentences[company]:
                writer.writerow(['1', sentence, company])

    with open(FOLDER + TRAIN_FILE_NAME, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        for company in company_to_sentences:
            for sentence in company_to_sentences[company]:
                writer.writerow(['1', sentence, company])

    with open(FOLDER + DEV_FILE_NAME, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        for company in company_to_sentences:
            for sentence in company_to_sentences[company]:
                writer.writerow(['1', sentence, company])

    with open(FOLDER + TEST_FILE_NAME, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        for company in company_to_sentences:
            for sentence in company_to_sentences[company]:
                writer.writerow(['1', sentence, company])


create_input_files()
