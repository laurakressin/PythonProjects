"""
    This is a script to parse child labor and
    child marriage data.
    The Excel file used in this script can be
    found here: http://www.unicef.org/sowc2014/numbers/
"""

import xlrd
import pprint

book = xlrd.open_workbook('SOWC 2014 Stat Tables_Table 9.xlsx')
sheet = book.sheet_by_name('Table 9 ')

count = 0
data = {}

for i in xrange(14, sheet.nrows):
    row = sheet.row_values(i)
    country = row[1]

    data[country] = {
        'child_labor': {
            'total': [row[4], row[5]],
            'male': [row[6], row[7]],
            'female': [row[8], row[9]],
        },
        'child_marriage': {
            'married_by_15': [row[10], row[11]],
            'married_by_18': [row[12], row[13]],
        }
    }

    if country == 'Zimbabwe':
        break

pprint.pprint(data)