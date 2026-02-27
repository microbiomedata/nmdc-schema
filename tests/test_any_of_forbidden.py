import os
import re
import unittest


class TestNoAnyOfInSchemaFiles(unittest.TestCase):

    def test_no_any_of_in_schema_files(self):
        schema_dir = os.path.join(os.path.dirname(__file__), '..', 'src', 'schema')
        files_with_any_of = []

        pattern = re.compile(r"^ +any_of:")

        # Walk through the schema directory and check each file
        for root, dirs, files in os.walk(schema_dir):
            for file in files:
                if file.endswith(".yaml") or file.endswith(".yml"):  # You can add other extensions if needed
                    # print(f"searching yaml file {file} for any_of")
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r') as f:
                        # Read the file line by line and check for the pattern
                        for line_num, line in enumerate(f, 1):
                            if pattern.match(line):
                                files_with_any_of.append(f"{file_path} (line {line_num})")
                                break  # Stop after finding the first match in the file
                else:
                    pass
                    # print(f"skipping non-yaml file {file}")

        self.assertListEqual(files_with_any_of, [],
                             msg=f"The following files contain 'any_of': {files_with_any_of}")
