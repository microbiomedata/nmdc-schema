import requests
import xmltodict
import json


def download_biosample_xml(accession):
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample&id={accession}&rettype=xml"
    response = requests.get(url)

    if response.status_code == 200:
        xml_data = response.text
        biosample_dict = xmltodict.parse(xml_data)
        pretty_json = json.dumps(biosample_dict, indent=4)
        print(f"Biosample {accession} XML converted to dictionary and pretty printed:")
        print(pretty_json)
    else:
        print(f"Failed to download XML data for Biosample {accession}. Status code: {response.status_code}")


# Usage example
accession = "SAMN35136422"
download_biosample_xml(accession)
