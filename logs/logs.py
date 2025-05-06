from peewee import *
from datetime import datetime
import os
import json


# Получаем название текущего файла и путь к нему
full_ = os.path.abspath(__file__)
file_ = os.path.basename(__file__)
cur_dir = full_.replace(file_, '')

# Получаем место нахождения базы данных с логами
with open(f'{cur_dir}/conf.json', 'r') as setg:
    data_setg = json.load(setg)
dir_logs = data_setg['dir_db_logs']

os.chdir(dir_logs)


def logs(file_name, proc_name, status_info, text_logs):

    try:
        
        db = SqliteDatabase(f'{dir_logs}/logs.db')

        class Logs_t(Model):
            date_time = DateTimeField(default=datetime.today().replace(microsecond=0))
            login = TextField(default=os.environ['USER'])
            file_name = TextField(null=False)
            proc_name = TextField(null=False)
            status_info = TextField(null=False)
            text_logs = TextField(null=False)

            class Meta:
                database = db
        
        Logs_t.create_table()

        if text_logs:
            Logs_t.create(
                file_name=file_name,
                proc_name=proc_name,
                status_info=status_info,
                text_logs=text_logs,
            )
        else:
            print('Нет сообщения')

    except Exception as er:
        print(f'[ERROR]: {er}')