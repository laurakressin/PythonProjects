pdf_txt = 'en-final-table9.txt'
openfile = open(pdf_txt, 'r')

country_line = total_line = False
for line in openfile:
    if country_line or total_line:
        print line

    if line.startswith('and areas'):
        country_line = True
    elif country_line:
        if line == '/n':
            country_line = False

    if line.startswith('total'):
        total_line = True
    elif total_line:
        if line == '\n':
            total_line = False