from django.core.exceptions import PermissionDenied
from django.shortcuts import render
import os
import sqlite3
import shutil
def index(request):
    if request.user.is_authenticated:

        print("Загружается таблица")
        i=0
        con = sqlite3.connect("db.sqlite3")
        cursor = con.cursor()
        f = open('open.txt', 'w', encoding='utf-8')

        Start = ['<!DOCTYPE html>\n'
                 '<html>\n'
                 '<head>\n'
                 '<meta charset="utf-8">\n'
                 '<title>Табличка</title>\n'
                 '<style>\n'
                 '.table{\n'
                 '   border: 1px solid #eee;\n'
                 #'   table-layout: fixed;\n'
                 '   width: 100%;\n'
                 '   margin-bottom: 20px;\n' #место под таблицей
                 '}\n'
                 '.table th {\n'
                 '   font-weight: bold;\n'
                 '   padding: 5px;\n'
                 '   background: #efefef;\n'
                 '   border: 1px solid #dddddd;\n'
                 '}\n'
                 '.table td{\n'
                 '   padding: 1px 1px;\n'
                 '   border: 1px solid #EFDCD7;\n'
                 '   text-align: left;\n'
                 '}\n'
                 '.table tbody tr:nth-child(odd){\n'
                 '   background: #fff;\n'
                 '}\n'
                 '.table tbody tr:nth-child(even){\n'
                 '   background: #F7F7F7;\n'
                 '}\n'
                 '</style>\n'

                
                 '</head>\n'
                 '<body>\n'
                 
                 '<table class="table">\n'

                 '<tr>\n'
                 '<th>Номер</th>\n'
                 '<th>Договор</th>\n'
                 '<th>Телефон</th>\n'
                 '<th>Задача</th>\n'
                 '<th>Адрес</th>\n'
                 '<th>Дата</th>\n'
                 '<th>Комментарий</th>\n'
                 '<th>Метка</th>\n'
                 '</tr>\n']
        f.writelines(Start)

        cursor.execute("SELECT * FROM Points ORDER BY Adress DESC")
        for p in cursor.fetchall():
            i=i+1
            DataPoint = ['<tr>\n'
                       '<td>'f"{i}"'</td>\n'
                       '<td>'f"<a href=\"{'http://192.168.31.65/main/map/'}\">{p[0]}</a>"'</td>\n'
                       '<td>'f"{p[1]}"'</td>\n'
                       '<td>'f"{p[2]}"'</td>\n'
                       '<td>'f"{p[3]}"'</td>\n'
                       '<td>'f"{p[4]}"'</td>\n'
                       '<td>'f"{p[5]}"'</td>\n'
                       '<td>'f"{p[6]}"'</td>\n'
                       '</tr>\n']
            f.writelines(DataPoint)

        Middle = ['</table>\n'
               
               '<table class="table">\n'

               '<tr>\n'
               '<th>Номер</th>\n'
               '<th>Договор</th>\n'
               '<th>Телефон</th>\n'
               '<th>ФИО</th>\n'
               '<th>Адрес</th>\n'
               '<th>Дата</th>\n'
               '<th>Комментарий</th>\n'
               '</tr>\n']

        f.writelines(Middle)

        cursor.execute("SELECT * FROM New ORDER BY Adress DESC")
        i = 0
        for p in cursor.fetchall():
            i = i + 1
            DataNew = ['<tr>\n'
                         '<td>'f"{i}"'</td>\n'
                         '<td>'f"<a href=\"{'http://192.168.31.65/main/map/'}\">{p[0]}</a>"'</td>\n'
                         '<td>'f"{p[1]}"'</td>\n'
                         '<td>'f"{p[2]}"'</td>\n'
                         '<td>'f"{p[3]}"'</td>\n'
                         '<td>'f"{p[4]}"'</td>\n'
                         '<td>'f"{p[5]}"'</td>\n'
                         '</tr>\n']
            f.writelines(DataNew)

        End = ['</table>\n'
               '</body>\n'
               '</html>\n']
        f.writelines(End)

        f.close()
        os.rename('open.txt', 'index' + ".html")
        shutil.move('index.html',
                    'main/templates/tab/index.html')
        print("Загруженна таблица")
        return render(request,'tab/index.html',{})
    else:
        raise PermissionDenied
