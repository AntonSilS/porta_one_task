Щоб запустити программу:
1. В корневій директорії створіть нове віртуальне середовище venv: python3 -m venv venv
2. Активуйте його за допомогою команди: source venv/bin/activate
3. Запустіть команду:  pip install -r requirements.txt
для того, щоб встановити всі залежності
4. Запустіть программу в корневій директорії за допомогою: python src/main.py
в терміналі 
5. Перейдіть по адресі http://0.0.0.0:8000 і далі введіть там текст у поле 

6. Щоб запустити тестів запустіть в корневій директорії python -m pytest


Вирішив викорастити fast api для того, щоб зробити невиличкий і простий веб-застосунок
замість вводу в консоль в терміналі.
Віришив також викорастити ООП підхід для коду, шо виконує обробку тексту для того, щоб було можливо
росширювати програму при необхідності.
- Всі класи з методами для обробки тексту знаходяться в файлі classes.py.
- В main.py знаходиться код серверної частини веб-застосунку.

 які б питання перед тим, як почати вирішувати задачу:
1. Якщо є слово, в якому немає уникалних символів, чи потрібно його добавляти 
в список? В мене логіка реалізована таким чином, що в такому випадку я повертаю None. Також я поверну None, якщо є два однакових слова в тектсі, який складений тільки з цих слів. Наприклад, Hello Hello. По першій умові у кожного з слів унікальним першими будуть H, але по другій умові в списку будуть два символи H, тому унікальних вже немає і я повертаю None.
2. Чи маю я розглядати окремий символ, як слово? Наприлад, слово I в анг. мові?
В мене логіка працює, що так, але тільки якщо це слово складається з
литиниці, або з кирилиці + україньскі букви
- Я ігнорую комбінації цифрових символів, по типу 123, але не ігнорую слова С++, С123.
- Також я не ігорную слова в дужках, або буквені символи в дужках, по типу (с), с - розглядається, 
як слово
- Також якщо текст починається не з літер, кавичок, або дужок, то повертається стрінга з тексом, що "it's not a text!!!"
 
