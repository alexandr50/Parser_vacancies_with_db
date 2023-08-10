# CourseWork_5

Проэкт для работы с базой данных: получает вакансии с по 10ти компаниям с HeadHunter:
    1.Альфа-банк
    2.Сбер
    3.Тинькофф
    4.Ozon
    5.Газпром
    6.Почта
    7.Яндекс
    8.Metro
    9.ВТБ
    10.Северсталь

1. для запуск проэкта нужно установить зависимости из файла pyproject.toml 
2. создать конфигурационный файл database.ini в дериктории data_files вида:
[postgresql]
host=localhost
user=postgres(по умолчанию)
password=****(ваш пароль)
port=5432(по умолчанию)
3.Запустить файл main.py и следовать сценарию программы
    
В дериктории classes находяться классы для взвимодействия с бд и HeadHunter
В дериктории data_files находяться файлы с названиями и id компаний для поиска скрипты sql и конфигурационный файл для подключения к бд database.ini
В дериктории utils на ходятся функция считывания конфигурационного файла для подключения к бд и функция возвращающая список компаний из файла employers.json
В дериктории tests находятся тесты


 
