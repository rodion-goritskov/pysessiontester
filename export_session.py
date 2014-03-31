import datetime
from config_utils import SessionConfig


def export_session_to_html(text_field):
    '''Exports everything from text_field to html file
    with current session day and time'''
    settings_file = SessionConfig('export.ini')
    EXPORT_PATH = settings_file.read_config()
    res = ""
    pair = False
    session_date = datetime.datetime.today()
    session_date_string = session_date.strftime('%d %b %Y %X')
    with open(EXPORT_PATH + '/Session at ' + session_date_string + '.html',
              mode='w',
              encoding='utf-8') as export_file:
        export_file.write(
            '<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">\n')
        export_file.write('<h1>Session at ' + session_date_string + '</h1>\n')
        text_field = text_field.replace("\n", "</br>")
        for i in text_field:
            if ((i == "*") & (pair is False)):
                res = res + '<text style="font-weight: bold;">'
                pair = True
            elif ((i == "*") & (pair is True)):
                res = res + "</text>"
                pair = False
            else:
                res = res + i
        export_file.write('<p>' + res + '</p>')
