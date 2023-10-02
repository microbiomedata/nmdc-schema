import logging

import click
import click_log
import requests

turtle_data_file_path = "../examples/output/Database-sample_preparation_set.ttl"
png_output_file_path = "../examples/output/Database-sample_preparation_set.png"

logger = logging.getLogger(__name__)
click_log.basic_config(logger)


def open_text_file_as_one_string(file_path):
    """Opens a text file as a single string.

    Args:
      file_path: The path to the text file.

    Returns:
      A string containing the contents of the text file.
    """

    with open(file_path, "r") as f:
        return f.read()


def download_image_and_save_as_file(
        params_dict,
        file_path,
        base_url="http://www.ldf.fi/service/rdf-grapher"
):
    """Downloads an image from the given URL and saves it to the given file path.

    Args:
      base_url: The base URL of the RDF visualization service
      params_dict: rdf text, from format and to format
      file_path: The filesystem path for saving the generated image
    """

    response = requests.post(url=base_url, params=params_dict)

    if response.status_code == 200:
        with open(file_path, "wb") as f:
            f.write(response.content)
    else:
        raise Exception("Failed to download generated image")


@click.command()
@click_log.simple_verbosity_option(logger)
@click.option("--input-turtle", required=True, type=str, help="Path to RDF/TTL input file")
@click.option("--output-png", required=True, type=str, help="Path for PNG output file")
def main(input_turtle, output_png):
    file_contents = open_text_file_as_one_string(input_turtle)
    params = {"rdf": file_contents, "from": "ttl", "to": "png"}
    download_image_and_save_as_file(params_dict=params, file_path=output_png)


if __name__ == "__main__":
    main()
