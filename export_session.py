import datetime


def export_session_to_html(text_field):
    '''Exports everything from text_field to html file
    with current session day and time'''
    session_date = datetime.datetime.today()
    session_date_string = session_date.strftime('%d %b %Y %X')
    with open('Session at ' + session_date_string + '.html', mode='w',
              encoding='utf-8') as export_file:
        export_file.write(
            '<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">\n')
        export_file.write('<h1>Session at ' + session_date_string + '</h1>\n')
        export_file.write('<p>' + text_field + '</p>')
