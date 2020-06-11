#!/usr/bin/env python

"""A utility for making rosters and membership cards with photos."""

__author__ = "Michelle Arzul"
__copyright__ = "Copyright 2020, Michelle Arzul"
__credits__ = ["Michelle Arzul", "Anne-Françoise Arzul"]
__maintainer__ = "Michelle Arzul"
__email__ = "michelle.arzul@gmail.com"
__status__ = "Development"

import csv
import os
import sys

import barcode

blank_pic = 'data:image/png;base64,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'

style = '''<style>
.header {
    padding: 10mm;
    margin: 0;
}
.header .logo {
    width: 10mm;
    height: 10mm;
    object-fit: contain;
    margin-right: 10mm;
}
.header h1 {
    font-family: "Helvetica";
    margin: 0;
}
.header td {
    padding: 0;
    vertical-align: middle;
}
table, tr, td {
    border-spacing: 0;
    border-collapse: collapse;
    padding: 0;
    margin: 0;
}
p {
    font-family: "Helvetica";
    margin: 0;
}
.parent .column {
    border: 1px dashed black;
}
.card {
    width: 85.60mm;
    height: 53.98mm;
    border-radius: 3.48mm;
    border: 1px solid black;
    padding: 0;
    margin: 5mm;
}
.card table {
    height: 100%;
}
.card td {
    height: 100%;
    text-align: center;
    vertical-align: middle;
}
.card .pic {
    width: 35mm;
    height: 45mm;
    border-radius: 2.5mm;
    object-fit: cover;
    object-position: 50% 50%;
    margin-left: 4.5mm;
}
.card .infoColumn {
    width: 100%;
}
.card .info {
    height: 100%;
    padding: 4.5mm;
    justify-content: space-between;
    flex: 1;
}
.card .logo {
    height: 10mm;
    width: 10mm;
    object-fit: contain;
}
.card .name {
    font-size: 16;
    margin-top: 4.5mm;
    margin-bottom: 1mm;
}
.card .barcode {
    padding: 0;
    margin: 0;
}
.card svg {
    transform: scale(1, 0.5)
}
.card .id {
    font-weight: lighter;
    font-size: 12;
}
.list_entry td {
    text-align: center;
}
.list_entry .pic {
    width: 35mm;
    height: 45mm;
    border-radius: 2.5mm;
    object-fit: cover;
    object-position: 50% 50%;
    margin: 2mm;
}
.list_entry .name {
    font-size: 12;
    margin-bottom: 1mm;
}
</style>'''

def htmlDoc(title, content):
    """Returns a string representing an HTML document with the specified title and content."""
    return '''<!DOCTYPE html>
<html>
    <head>
        <title>{}</title>
    </head>
    <body>
{}
    </body>
</html>
{}'''.format(title, content, style)

def header(output_folder, title):
    """Returns a string representing an HTML header for the list page, with logo and class name."""
    if os.path.exists(os.path.join(output_folder, 'logo.png')):
        logo_element = '<img class="logo" src="logo.png" />'
    else:
        logo_element = ''
    
    return '        <div class="header"><table><tr><td>{}</td><td><h1>{}</h1></td></tr></table></div>'.format(logo_element, title)
    
def table(content, n_columns):
    """Returns a string representing an HTML table with the number of columns specified and with cells each containing one element of the list content."""
    rows = ''
    i = 0
    while i < (len(content)):
        columns = ''
        for _ in range(n_columns):
            try:
                columns += '''                <td class="column">
{}
                </td>'''.format(content[i])
                i += 1
            except IndexError:
                break
        rows += '''            <tr>
{}
            </tr>'''.format(columns)
    return '''        <table class="parent">
{}
        </table>'''.format(rows)

def generate_barcode(member_id):
    """Returns a string representing an SVG element of a Code 39 Barcode of the provided member ID."""
    return barcode.Code39(member_id.zfill(8)).render(writer_options={}, text="").decode('utf-8')

def card_div(output_folder, item):
    """Returns a string representing a div of a nicely formatted membership card. Images are relative links."""
    pic = item['id'] + '.jpg'
    if not os.path.exists(os.path.join(output_folder, pic)):
        pic = blank_pic
    if os.path.exists(os.path.join(output_folder, 'logo.png')):
        logo_element = '<img class="logo" src="logo.png" />'
    else:
        logo_element = ''
    return '''                    <div class="card">
                        <table>
                            <tr>
                                <td>
                                    <img class="pic" src="{}" />
                                </td>
                                <td class="infoColumn">
                                    <div class="info">
                                        {}
                                        <p class="name">{}</p>
                                        <div class="barcode">
                                            {}
                                            <p class="id">{}</p>
                                        </div>
                                    </div>
                                </td>
                            </tr>
                        </table>
                    </div>'''.format(pic, logo_element, item['name'], generate_barcode(item['id']), item['id'].zfill(8))

def card_divs(output_folder, member_data):
    """Returns a list of membership card divs, see card_div."""
    cards = []
    for item in member_data:
        cards.append(card_div(output_folder, item))
    return cards

def list_entry(output_folder, item):
    """Returns a string representing a div of a nicely formatted member list entry. Images are relative links."""
    pic = item['id'] + '.jpg'
    if not os.path.exists(os.path.join(output_folder, pic)):
        pic = blank_pic
    return '''                    <div class="list_entry">
                        <table>
                            <tr>
                                <td>
                                    <img class="pic" src="{}" />
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    <p class="name">{}</p>
                                </td>
                            </tr>
                        </table>
                    </div>'''.format(pic, item['name'])

def list_divs(output_folder, member_data):
    """Returns a list of member list entry divs, see list_div."""
    list_entries = []
    for item in member_data:
        list_entries.append(list_entry(output_folder, item))
    return list_entries

def parse_csv(input_file_path):
    """Returns the location, name minus extension, and list of member data parsed from a CSV file."""
    prev_cwd = os.getcwd()
    output_folder = os.path.dirname(input_file_path)
    os.chdir(output_folder)
    list_name = '.'.join(os.path.basename(input_file_path).split('.')[:-1])
    input_filename = os.path.basename(input_file_path)
    member_data = []
    with open(input_filename, 'r') as input_file:
        reader = csv.reader(input_file, delimiter=',')
        for row in reader:
            member_data.append({
                'id': row[0],
                'name': row[1]
            })
    os.chdir(prev_cwd)
    return (output_folder, list_name, member_data)

def generate_list(output_folder, list_name, member_data):
    """Write an HTML file to the specified folder containing a list of the given members."""
    output_file = list_name + '_list.html'
    write_output(os.path.join(output_folder, output_file), htmlDoc(list_name + ' List', header(output_folder, list_name) + table(list_divs(output_folder, member_data), 4)))

def generate_cards(output_folder, list_name, member_data):
    """Write an HTML file to the specified folder containing membership cards for the given members."""
    output_file = list_name + '_cards.html'
    write_output(os.path.join(output_folder, output_file), htmlDoc(list_name + ' Cards', table(card_divs(output_folder, member_data), 2)))

def write_output(output_path, content):
    """Writes the given content to the given path."""
    with open(output_path,'w') as output:
        output.write(content)

if __name__ == '__main__':
    try:
        input_file_path = sys.argv[1]
    except IndexError:
        print('No input file path specified.')
        exit()
    
    if not os.path.exists(input_file_path):
        print('Input file path specified does not exist.')
        exit()
    
    if not os.path.isfile(input_file_path):
        print('Input provided is not a file.')
        exit()
    
    try:
        mode = sys.argv[2]
        if mode not in ['list', 'cards', 'both']:
            raise ValueError
    except IndexError:
        mode = 'both'
    except ValueError:
        print('Please specify a valid mode.')
        exit()

    output_folder, list_name, member_data = parse_csv(input_file_path)

    if mode == 'list' or mode == 'both':
        generate_list(output_folder, list_name, member_data)
    if mode == 'cards' or mode == 'both':
        generate_cards(output_folder, list_name, member_data)
    
    print('Done.')
