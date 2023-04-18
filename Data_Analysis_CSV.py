"""
Project for Week 3 of "Python Data Analysis".
Read and write CSV files using a dictionary of dictionaries.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv

def read_csv_fieldnames(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Ouput:
      A list of strings corresponding to the field names in
      the given CSV file.
    """
    with open(filename, "r", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=separator, quotechar=quote)
        field_names = []
        for row in csv_reader:
            field_names.append(row)
    return field_names[0]


def read_csv_as_list_dict(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a list of dictionaries where each item in the list
      corresponds to a row in the CSV file.  The dictionaries in the
      list map the field names to the field values for that row.
    """
    with open(filename, "r", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=separator, quotechar=quote)
        list_of_dict = []
        for row in csv_reader:
            list_of_dict.append(row)
    return list_of_dict


def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      keyfield  - field to use as key for rows
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the
      field values for that row.
    """
    csv_dict = {}
    list_of_csv = read_csv_as_list_dict(filename, separator, quote)
    for row in list_of_csv:
        key = row[keyfield]
        csv_dict[key] = row
    return csv_dict


def write_csv_from_list_dict(filename, table, fieldnames, separator, quote):
    """
    Inputs:
      filename   - name of CSV file
      table      - list of dictionaries containing the table to write
      fieldnames - list of strings corresponding to the field names in order
      separator  - character that separates fields
      quote      - character used to optionally quote fields
    Output:
      Writes the table to a CSV file with the name filename, using the
      given fieldnames.  The CSV file should use the given separator and
      quote characters.  All non-numeric fields will be quoted.
    """
    with open(filename, 'w', newline='', encoding="utf-8") as file:
        writer = csv.DictWriter(file, delimiter=separator, quotechar=quote,
                                 fieldnames=fieldnames, quoting=csv.QUOTE_ALL) 
        writer.writeheader()
        first_line = True
        for row in table:
            if first_line:
                writer = csv.DictWriter(file, delimiter=separator,
                                         quotechar=quote, fieldnames=fieldnames) 
                writer.writerow(row)
                first_line = False
            else:
                writer.writerow(row)

