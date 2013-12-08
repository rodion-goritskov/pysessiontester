import datetime


def export_session_to_html(text_field):
    session_date = str(datetime.date.today())
    with open('session' + session_date, mode='w',
              encoding='utf-8') as export_file:
        export_file.write(text_field)
