import wikipediaapi
import re

company_names = ['Infineon', 'Volkswagen AG', 'Daimler AG', 'Bayerische Motoren Werke AG', 'Deutsche Bahn AG',
                 'Robert Bosch GmbH',
                 'Siemens AG', 'Deutsche Telekom AG', 'REWE-Gruppe', 'Deutsche Lufthansa AG', 'Deutsche Bank AG',
                 'BASF SE', 'SAP SE',
                 'Airbus-Gruppe Deutschland', 'Fresenius SE & Co. KGaA', 'ZF Friedrichshafen AG', 'Vonovia SE',
                 'Schwarz-Gruppe',
                 'thyssenkrupp AG', 'E.ON SE', 'Adesso SE', 'Roche-Gruppe Deutschland', 'Allianz SE', 'MERCK KGaA',
                 'EDEKA-Gruppe',
                 'Münchener Rückversicherungs-Gesellschaft AG']

wiki_wiki = wikipediaapi.Wikipedia('de')


def load_data():
    company_to_sentences = {company_name: [] for company_name in company_names}

    for company_name in company_names:
        text = wiki_wiki.page(company_name).text
        cleaned_text = text.replace('\n', ' ').strip()
        if len(cleaned_text) == 0:
            continue
        sentences = re.split('(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)[0:50]
        company_to_sentences[company_name] = sentences

    return company_to_sentences
