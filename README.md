# Використання публічних коштів територіальними громадами Київської област




Пояснення коду:

Імпорт бібліотек: Імпорт необхідних бібліотек для роботи (Streamlit, pandas, requests, datetime).

Функція get_transaction_function:

Завантажує дані з API.
Фільтрує та очищає дані.
Повертає DataFrame з відфільтрованими даними.
Streamlit інтерфейс:

Встановлюється заголовок.
Додається вибір дати для завантаження даних.
Викликається функція завантаження даних з API.
Відображаються перші 5 рядків завантажених даних.
Виконується базовий аналіз та візуалізація.
Інструкції:
Запустіть цей код у вашому Streamlit додатку.
Оберіть дату для завантаження даних.
Перегляньте результати аналізу та візуалізацію.


A simple Streamlit app template for you to modify!

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://blank-app-template.streamlit.app/)

### How to run it on your own machine

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```
