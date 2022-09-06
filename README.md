# Тестовое задание на позицию SDET/QA Automation Engineer

## Задание:
> Написать несколько сценариев для процесса аутентификации.

Примеры сценариев:
 - Успешная аутент. по sms/email
 - Аутент. по sms/email с неправильным кодом, введенным один и более раз
 - Слишком большое ожидание ввода кода

# Приложение:
Приложение для тестирования находится по адресу https://dev1.torrow.net
Отправленный код на телефон/email можно получить по адресам:
- https://smsdev1.torrow.net/api/phone/{phoneNumber} (прим. https://smsdev1.torrow.net/api/phone/7911123456)
- https://emaildev1.torrow.net/api/email/{email} (прим. https://emaildev1.torrow.net/api/email/asdsad@dsfsdf.sdf)

# Требования:
- Тестовый проект должен быть написан на языке Python и Selenium.
- Использовать паттерн PageObject (прим. https://docs.specflow.org/projects/specflow/en/latest/ui-automation/Selenium-with-Page-Object-Pattern.html) 

### Копирование репозитория и установка зависимостей
```bash
git clone https://github.com/p2cbbb/torrow_qa_test
cd torrow_qa_test
virtualenv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Запуск тестов
 - Перед запуском тестов необходимо перейти в каталог проекта `torrow_qa_test`
 
Аргументы запуска:
- -s - показывать принты в процессе выполнения
- -v - verbose режим, чтобы видеть, какие тесты были запущены
```bash
python -m pytest -v -s test_torrow_auth.py
```