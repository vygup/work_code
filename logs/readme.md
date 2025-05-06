# Инфо по работе

Установка:
```py
sys.path.append('') # Путь до функции
# OR
os.chdir('') # Путь до функции

from logs import logs
```

Работа с функцией:
```py
logs('file_name', 'proc_name', 'status_info', 'text_logs')
```
- file_name - название файла (в py скрипте можно передать `os.path.basename(__file__)`)
- proc_name - название процесса
- status_info - тип лога (`INFO`, `ERROR`, `OK`) 
- text_logs - развернутое сообщение лога

Просмотр логов в `show_logs.ipynb`

Пример:

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>id</th>
      <th>date_time</th>
      <th>login</th>
      <th>file_name</th>
      <th>proc_name</th>
      <th>status_info</th>
      <th>text_logs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>3</td>
      <td>2025-05-06 20:54:09</td>
      <td>vyg</td>
      <td>test.py</td>
      <td>test proc</td>
      <td>INFO</td>
      <td>OK</td>
    </tr>
    <tr>
      <td>4</td>
      <td>2025-05-06 20:55:46</td>
      <td>vyg</td>
      <td>test.py</td>
      <td>test proc</td>
      <td>ERROR</td>
      <td>...</td>
    </tr>
  </tbody>
</table>
</div>
