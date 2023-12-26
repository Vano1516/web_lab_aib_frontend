from base import BaseXlsBlock
from datetime import datetime


header_format = {
    'border': 2,
    'color': '#002060',
    'bold': True,
    'bg_color': '#FCD5B4',
    'font_size': 14,
    'font_name': 'Arial'
}

title_format = {
    'bold': True,
    'bg_color': '#C5D9F1',
    'border': 3,
    'font_size': 10,
    'font_name': 'Arial'
}

title2_format = {
    'bold': False,
    'bg_color': '#C5D9F1',
    'border': 3,
    'font_size': 10,
    'font_name': 'Arial'
}


class HeaderBlock(BaseXlsBlock):
    NAME = "Параметры запроса"
    DATE = "Дата выгрузки"
    PERIOD = "Период за который сделана выгрузка"

    def write_header(self):
        hf = self.workbook.add_format(header_format)
        hf.set_text_wrap()
        hf.set_align('center')

        tf = self.workbook.add_format(title_format)
        tf.set_text_wrap()
        tf.set_align('center')

        self.worksheet.write('A1', self.NAME, hf)
        self.worksheet.write('A2', self.DATE, tf)
        self.worksheet.write('A3', self.PERIOD, tf)
        self.row = 1
        self.col = 1

    def write_data(self):
        tf = self.workbook.add_format(title_format)
        tf.set_text_wrap()
        tf.set_align('center')

        date_now = datetime.now().strftime('%d.%m.%Y')
        self.worksheet.write(self.row, self.col, date_now, tf)

        self.row += 1
        dates = [payment['created_at'] for payment in self.data['payments']]
        dates = [datetime.fromisoformat(date[:-1]) for date in dates]
        dates.sort()
        date_low_str = dates[0].strftime('%d.%m.%Y')
        date_upp_str = dates[-1].strftime('%d.%m.%Y')
        period = f'{date_low_str} - {date_upp_str}'
        self.worksheet.write(self.row, self.col, period, tf)

        self.col = 0
        self.row += 2


class PayersBlock(BaseXlsBlock):
    NAME = "Отчёт по активным клиентам"
    TOP = "Топ клиентов по количеству платежей"

    def write_header(self):
        hf = self.workbook.add_format(header_format)
        hf.set_text_wrap()
        hf.set_align('center')

        tf = self.workbook.add_format(title_format)
        tf.set_text_wrap()
        tf.set_align('center')

        t2f = self.workbook.add_format(title2_format)
        t2f.set_text_wrap()
        t2f.set_align('center')

        self.row = 5
        self.col = 0
        self.worksheet.write(self.row, self.col, self.NAME, hf)
        self.worksheet.write('A7', self.TOP, tf)

    def write_data(self):
        t2f = self.workbook.add_format(title2_format)
        t2f.set_text_wrap()
        t2f.set_align('center')

        self.row += 1
        self.col += 1
        clients_payments = []

        for client in self.data['clients']:
            for payment in self.data['payments']:
                if client['id'] == payment['client_id']:
                    clients_payments.append({
                        'fio': client['fio'],
                        'payment_amount': payment['amount'],
                        'payment_created_at': payment['created_at']
                    })

        clients_payments.sort(key=lambda x: datetime.fromisoformat(x['payment_created_at']), reverse=True)

        quarters = {}
        for client_payment in clients_payments:
            payment_date = datetime.fromisoformat(client_payment['payment_created_at'])
            q = f'Q{(payment_date.month % 4 + 1)} {payment_date.year}'
            quarters.setdefault(q, []).append({
                'fio': client_payment['fio'],
                'payment_amount': client_payment['payment_amount']
            })

        for q in quarters:
            self.worksheet.write(self.row, self.col, q, t2f)
            srt = sorted(quarters[q], key=lambda x: x['payment_amount'])[:10]
            for s in srt:
                self.row += 1
                self.worksheet.write(self.row, self.col, s['fio'])
            self.row -= 10
            self.col += 1


class CitiesBlock(BaseXlsBlock):
    NAME = "География клиентов"
    STATISTIC = 'Статистика распределения клиентов'
    CITY = 'Города'
    AMOUNT = 'Kоличество клиентов по городам'
    Russia = 'Russia'

    def write_header(self):
        hf = self.workbook.add_format(header_format)
        hf.set_text_wrap()
        hf.set_align('center')

        tf = self.workbook.add_format(title_format)
        tf.set_text_wrap()
        tf.set_align('center')

        t2f = self.workbook.add_format(title2_format)
        t2f.set_text_wrap()
        t2f.set_align('center')

        self.worksheet.write('A19', self.NAME, hf)
        self.worksheet.merge_range('A20:A21', self.STATISTIC, tf)
        self.worksheet.write('B21', self.CITY, t2f)
        self.worksheet.write('C21', self.AMOUNT, t2f)
        self.worksheet.merge_range('B20:C20', self.Russia, t2f)

    def write_data(self):
        self.row = 20
        self.row += 1
        self.col += 1
        clients = self.data['clients']

        city_counts = {}
        for client in clients:
            city = client['city']
            city_counts[city] = city_counts.get(city, 0) + 1

        top_cities = sorted(city_counts.items(), key=lambda x: x[1], reverse=True)[:10]

        for i, (city, count) in enumerate(top_cities, start=1):
            self.worksheet.write(self.row + i - 1, self.col, f"{i}. {city}")
            self.worksheet.write(self.row + i - 1, self.col + 1, f"{count}")


class BankAccountBlock(BaseXlsBlock):
    NAME = "Анализ состояния счёта"
    STATISTIC = 'Статистика состояния счета'
    CLIENT = 'Клиент'
    STATE = 'Состояние счета клиента'
    DEBT = 'Задолженность'
    PROFIT = 'Прибыль'

    def write_header(self):
        hf = self.workbook.add_format(header_format)
        hf.set_text_wrap()
        hf.set_align('center')

        tf = self.workbook.add_format(title_format)
        tf.set_text_wrap()
        tf.set_align('center')

        t2f = self.workbook.add_format(title2_format)
        t2f.set_text_wrap()
        t2f.set_align('center')

        self.worksheet.write('A34', self.NAME, hf)
        self.worksheet.merge_range('A35:A36', self.STATISTIC, tf)
        self.worksheet.merge_range('B35:C35', self.DEBT, t2f)
        self.worksheet.merge_range('E35:D35', self.PROFIT, t2f)
        self.worksheet.write('B36', self.CLIENT, t2f)
        self.worksheet.write('E36', self.STATE, t2f)
        self.worksheet.write('D36', self.CLIENT, t2f)
        self.worksheet.write('C36', self.STATE, t2f)

    def write_data(self):
        self.col = 1
        self.row = 36
        clients = self.data['clients']
        payments = self.data['payments']

        account_balances = {}
        for payment in payments:
            client_id = payment['client_id']
            amount = payment['amount']
            account_balances[client_id] = account_balances.get(client_id, 0) + amount

        top_balances = sorted(account_balances.items(), key=lambda x: x[1], reverse=True)[:10]
        self.col = 1
        self.row = 36
        for i, (client_id, balance) in enumerate(top_balances, start=1):
            client_info = next(client for client in clients if client['id'] == client_id)
            fio = client_info['fio']
            rounded_balance = round(balance, 2)
            self.worksheet.write(self.row + i - 1, self.col, f"{i}. {fio}")
            self.worksheet.write(self.row + i - 1, self.col + 1, f"{rounded_balance}")

        bottom_balances = sorted(account_balances.items(), key=lambda x: x[1])[:10]
        self.col = 3
        self.row = 36
        for i, (client_id, balance) in enumerate(bottom_balances, start=1):
            client_info = next(client for client in clients if client['id'] == client_id)
            fio = client_info['fio']
            rounded_balance = round(balance, 2)
            self.worksheet.write(self.row + i - 1, self.col, f"{i}. {fio}")
            self.worksheet.write(self.row + i - 1, self.col + 1, f"{rounded_balance}")