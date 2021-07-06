def check_command(stroka):

    global global_text
    help_command = "!help"
    done_command = "!done"
    format_text = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'new-line', 'ordered-list', 'unordered-list', 'printall' ]

    if input_string == help_command:
        print("""Available formatters: plain bold italic header link inline-code new-line
Special commands: !help !done""")
    elif input_string == done_command:
        file = open('output.md', 'w', encoding='utf-8')
        file.write(global_text)
        print('File saved!')
        file.close
        exit()
    elif input_string in format_text:
        if input_string == 'header':
            global_text = global_text + hedaer()
        elif input_string == 'new-line':
            global_text = global_text + new_line()
        elif input_string == 'link':
            global_text = global_text + link()
        elif input_string == 'plain':
            global_text = global_text + plain_text()
        elif input_string == 'bold':
            global_text = global_text + bold_text()
        elif input_string == 'italic':
            global_text = global_text + italic_text()
        elif input_string == 'inline-code':
            global_text = global_text + inline_code()
        elif input_string == 'ordered-list':
            global_text = global_text + ordered_list()
        elif input_string == 'unordered-list':
            global_text = global_text + unordered_list()
        elif input_string == 'printall':
            print(global_text)
    else:
        print("Unknown formatting type or command")


def hedaer():
    level = 0
    text = ''
    while True:
        level = int(input('Input header level:'))
        if level in range(1, 7):
            level = '#' * level
            text = input('Text:')
            break
        else:
            print('Level must be from 1 to 6.')
    headertext = level + ' ' + text + '\n'
    return headertext

def new_line():
    return ('\n')

def link():
    link = ''
    label = ''
    while True:
        label = str(input('Label:'))
        if label != '':
            link = str(input('URL:'))
            break
        else:
            print('Link lable is empty')

    linktext = '[' + label + ']' + '(' + link + ')'
    return linktext

def plain_text():
    text = ''
    text = str(input('Text:'))
    return text

def bold_text():
    text = ''
    text = str(input('Text:'))
    return '**' + text + '**'

def italic_text():
    text = ''
    text = str(input('Text:'))
    return '*' + text + '*'

def inline_code():
    text = ''
    text = str(input('Text:'))
    return '`' + text + '`'

def ordered_list():
    while True:
        nuber_lines = int(input('Number of rows: '))
        if nuber_lines < 1:
            print("The number of rows should be greater than zero")
        else:
            rows = ''
            for i in range(nuber_lines):
                #row_number = f'Row #{i + 1}:'
                row_text = str(input(f'Row #{i + 1}:')) 
                rows += '* ' + row_text + '\n'
            return rows

def ordered_list():
    while True:
        nuber_lines = int(input('Number of rows:'))
        rows = ''
        if nuber_lines > 0:
            for i in range(nuber_lines):
                row_number = f'Row #{i + 1}:'
                row_text = input(f'{row_number}')
                rows += str(i + 1) + ". " + row_text + "\n"
            break
        else:
            print("The number of rows should be greater than zero")
    return rows
        
def unordered_list():
    while True:
        nuber_lines = int(input('Number of rows: '))
        rows = ''
        if nuber_lines > 0:
            for i in range(nuber_lines):
                row_number = f'Row #{i + 1}:'
                row_text = str(input(f'{row_number}')) 
                rows += "* " + row_text + "\n"
            break    
        else:
            print("The number of rows should be greater than zero")
    return rows        

global_text = ''
while True:
    input_string = str(input('Choose a formatter:'))
    check_command(input_string)
    print(global_text)