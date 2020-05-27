# Student Docs

This is a utility for making printable class rosters and student cards, both optionally with photos of students. It is intended for use in educational institutions. The student cards can be cheaply transformed into physical student cards of the same dimensions as a standard ATM card.

## Licence

This project is licensed under the terms of the GNU General Public License v3.0.

## Legacy

The `/legacy` folder contains the original (terrible) Java version of this utility, written by me in 2011/2012 when I had just finished my first year of studies.

## Requirements

* [Python](https://www.python.org/downloads/) 3.5 or later.
* [`python-barcode`](https://pypi.org/project/python-barcode/), install a compatible version with `pip install python-barcode`.

## Usage

### Input

The expected input consists of the following:

* A CSV file of the class list with filename `<class>.csv` where `<class>` is the class code/name, with the following columns (no header row):
  * Student ID (No longer than 8 characters)
  * Name (As you want it to appear on the card, e.g. `Firstname Lastname`, or `LASTNAME Firstname Secondname`. Note that commas are not supported yet and including one will make anything after the comma disappear.)
* (Optional) In the same folder as the CSV file, an institution logo with filename `logo.png`. This image should have a transparent background. Ideal dimensions 512x512px. Will not be cropped. If absent, layout will adjust for better fit.
* (Optional) In the same folder as the CSV file, photos of students with filenames `<student_id>.jpg` where `<student_id>` is the corresponding student ID for the student whose photo the file is. These can be of any dimensions, but ideally they should be 827x1063px (i.e. UK/EU ID photo size, equivalent to 35x45mm at 600dpi), or other 7:9 aspect ratio to minimise cropping. If absent, a blank placeholder will be used.

### Running

Open a command prompt terminal and run the following command:

`python student-docs.py <path/to/class.csv> [<mode>]`

Substitute `<path/to/class.csv>` for the path (relative or absolute) to the comma-delimited class list.

Optionally, substitute `<mode>` with one of `list`, `cards`, or `both` to select which output type to produce, or leave blank for default of `both`.

The script will output files in the same folder as the input file.

Example using sample data:

`python student-docs.py sample/NCC-1701-D.csv` will output:
* `sample/NCC-1701-D_list.html` which is a class roster.
* `sample/NCC-1701-D_cards.html` which is a set of student cards.

#### As a module

This utility can also be imported as a module. Please refer to the docstrings in the code on how to use the functions.

## Recommended post-processing for student cards

Note that the layouts of the output files are optimised for printing on standard A4 paper, and that the solid lines around each card are the standard dimensions for an ATM card for convenient fit into a wallet or purse.

### Method 1

* Print on paper
* Laminate entire sheet
* Separate by guillotine using the dotted lines as a guide
* Let students cut along the solid line

### Method 2

* Print on paper
* Separate by guillotine using the dotted lines as a guide
* Let students stick the card on cardboard and cut along the solid line.

### Method 3

* Print on thick paper/cardstock/cardboard
* Optionally, laminate the entire sheet
* Separate by guillotine using the dotted lines as a guide
* Let students cut along the solid line

Note that laminating before cutting will make the cards more durable, but not waterproof at the edges.

## Credits

Written by Michelle Arzul in May 2020.

Special thanks to my mother Anne-Françoise Arzul for requesting this do-over and providing user feedback.

Sample data photos from Unsplash, uploaded by: Engin Akyurt, Bence Balla-Schottner, Nikolai Chernichenko, Neha Deshmukh, Monika Grabkowska, Moritz Nie, Julien Pianetti, Thomas Q.
