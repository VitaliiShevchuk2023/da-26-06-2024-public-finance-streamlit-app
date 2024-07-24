import streamlit as st
import pandas as pd
import requests
from datetime import datetime, timedelta

# Функція для завантаження даних з API
def get_transaction_function(current_datetime):
    st.write("Processing for date:", current_datetime)

    timestamp_str = current_datetime.strftime("%Y-%m-%d")
    start_date = (current_datetime - timedelta(days=1)).strftime("%Y-%m-%d")
    end_date = (current_datetime - timedelta(days=1)).strftime("%Y-%m-%d")

    url = "https://api.spending.gov.ua/api/v2/api/transactions/"
    params = {"startdate": start_date, "enddate": end_date}
    headers = {"accept": "application/json"}

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()

        # Якщо отриманих даних немає, виводимо повідомлення та завершуємо функцію
        if not data:
            st.write("No data received for the specified date range.")
            return None

        new_data = pd.DataFrame(data)

        # Список колонок, які потрібно видалити
        columns_to_drop = [
            'id', 'doc_vob', 'doc_vob_name', 'doc_number', 'doc_date', 'doc_v_date',
            'trans_date', 'amount_cop', 'currency', 'payer_account', 'payer_mfo',
            'payer_bank', 'payer_edrpou_fact', 'payer_name_fact', 'recipt_account',
            'recipt_mfo', 'recipt_bank', 'recipt_edrpou_fact', 'recipt_name_fact',
            'doc_add_attr', 'region_id', 'payment_type', 'payment_data', 'source_id',
            'source_name', 'kekv', 'kpk', 'contractId', 'contractNumber', 'budgetCode',
            'system_key', 'system_key_ff'
        ]

        # Видалення колонок, якщо вони існують
        columns_to_drop_existing = [col for col in columns_to_drop if col in new_data.columns]
        df = new_data.drop(columns=columns_to_drop_existing)

        # Перелік кодів ЄДРПОУ для фільтрації
        edrpou_codes = [
            '04358000', '33800777', '04360623', '04376624', '04369848', '25299709', '04054903', '04363662',
            '04362489', '04054636', '26376375', '04360586', '04358477', '26376300', '34627780', '04363834',
            '04054866', '04054628', '04359732', '04363509', '04358508', '04359146', '04360617', '04359152',
            '04363647', '04359488', '04412395', '04361491', '04363876', '04360296', '04363538', '04054613',
            '04359873', '04363886', '04363811', '04359287', '04359904', '04362697', '04360600', '04362183',
            '04358619', '04363343', '04054984', '04359867', '35161650', '04054978', '04359620', '04361723',
            '04527520', '04359643', '40883878', '04358218', '04358997', '04054961', '26425731', '04360913',
            '04358916', '04054955', '04361605', '42096329', '04361284', '04054990', '35161509', '34446857',
            '04362148', '04363225', '04361628', '04362160', '05408823'
        ]

        # Фільтрація DataFrame за двома полями
        filtered_df = df[(df['payer_edrpou'].isin(edrpou_codes)) | (df['recipt_edrpou'].isin(edrpou_codes))]

        return filtered_df

# Заголовок Streamlit додатка
st.title("Використання публічних коштів територіальними громадами Київської області")

# Вибір дати для завантаження даних
date = st.date_input("Виберіть дату для завантаження даних", datetime.now())

# Завантаження даних з API
new_data = get_transaction_function(date)

if new_data is not None and not new_data.empty:
    st.write(f"Кількість записів: {len(new_data)}")
    st.write(new_data.head())  # Відображення перших 5 рядків

    # Базовий аналіз даних
    total_amount = new_data['amount'].sum()
    st.write(f"Загальна сума транзакцій: {total_amount}")

    # Візуалізація даних
    st.bar_chart(new_data.groupby('payer_name')['amount'].sum())

else:
    st.write("No new data to process.")

    
