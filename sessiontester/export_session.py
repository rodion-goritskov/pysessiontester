import datetime
import markdown


def export_session_to_html(text_field, session_config):
    '''Exports everything from text_field to html file
    with current session day and time'''
    export_path = session_config.read_config()
    session_date = datetime.datetime.today()
    session_date_string = session_date.strftime('%d %b %Y %X')
    
    with open(export_path + 'Session at ' + session_date_string + '.html',
              mode='w',
              encoding='utf-8') as export_file:
        html = markdown.markdown(text_field, output_format = 'html4');
        export_file.write(
            '<!DOCTYPE html><meta http-equiv="Content-Type" content="text/html;charset=UTF-8">\n')
        export_file.write(html);