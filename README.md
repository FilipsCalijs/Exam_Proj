# Projekta nosaukums

Īss apraksts par projektu.

## Funkcionalitāte

1. **Datu pievienošana (Pievienot vienumu)** - Apraksts par funkcionalitāti.
2. **Datoju attēlošana** - Apraksts par funkcionalitāti.
3. **Datoju dzēšana** - Apraksts par funkcionalitāti.
4. **Datoju meklēšana un filtrēšana** - Apraksts par funkcionalitāti.
5. **Kārtošana** - Apraksts par funkcionalitāti.
6. **Datoju rediģēšana** - Apraksts par funkcionalitāti.
7. **Failu lasīšana/izveidošana/rediģēšana** - Apraksts par funkcionalitāti.
8. **Lietotāja reģistrācijas/pierakstīšanās parametru izveidošana** - Apraksts par funkcionalitāti.

## Instalācijas norādījumi

1. Lejupielādēt projektu no GitHub: `git clone <repository_URL>`
2. Izveidot virtuālo vidi: `python -m venv venv`
3. Aktivizēt virtuālo vidi:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
4. Instalēt nepieciešamās bibliotēkas: `pip install -r requirements.txt`
5. Veikt migrācijas: 
   - python manage.py makemigrations
   - python manage.py migrate

6. Palaidiet serveri: `python manage.py runserver`

## Kā mēs projektu iedomājamies

Detalizēts apraksts par to, kā projektu var izmantot, kāds ir galīgais mērķis un kādai auditorijai tas ir domāts.

## Autori

Andrejs Grānenko  
Filips Čalijs

## Licences

Šeit var ievietot informāciju par izmantojamo licenci.







## Функционал:
1. Добавление данных (Add item)
2. Отображение данных 
3. Удаление данных (по заданным критериям: by id Only or by name OR …)
4. Поиск и фильтрация данных (возможность установки различных критериев: By id or By неточное совпадение 
5. Сортировка (по нескольким критериям: by name OR by price or …(multipy sort)))
6. Редактирование данных (edit item)
7. Чтение/создание/редактирование файлов (read/create/edit files)
8. Создание параметры регистрации/входа пользователя. (login/register)


## Для того что бы устанвоить:
- скачиваем с github: git clone 'name of brunch'
- устанавливаем виртуальное окружение: python -m venv venv
- активируем его: source venv/bin/activate (путь может отлечаться от копмютера, проверти сами)
- там уже скачиваем django: pip insall django 
- Переходим в корневую папку (в нашем случае это Password)
- запускаем через команду python manage.py runserver
- если не работает, попробовать запустить миграции python manage.py makemigrations а потом python manage.py migrate

P.s: если долго не ищменяюеться css/html стили, то надо сделать жесткую очистку кэша: ctrl + f5


*возможно нужно немного подправить верську и функционал: дизайн и оформление css + что то не правильное показываеться на login/signup стоаницах

## Как представляем проект: 


Описание:
Проект связанные с менеджментов паролей, в котором нужно, для начала, зайти через модальное окно (логин/пароль), а после регистрации/логина пользователь заходит в само окно приложений в котором будет такая струкутра - логин пароля, пароль (хайден), ИД, гмайл и ... А из функции  а дальше после этой структуры (сверху или снизу), 


Сделанно с помощью:
Andrejs Granenko
Filips Calijs