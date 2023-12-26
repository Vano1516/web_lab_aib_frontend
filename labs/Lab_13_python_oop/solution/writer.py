import xlsxwriter
from datetime import datetime
from base import BaseXlsBlock
from blocks import PayersBlock, CitiesBlock, BankAccountBlock, HeaderBlock


class XlsAnalyticPaymentWriter:
    ANALYTICS_BLOCKS_CLASSES = [
        HeaderBlock,
        PayersBlock,
        CitiesBlock,
        BankAccountBlock
    ]

    def __init__(self, data):
        self.data = data

    def write_excel_report(self, output_file):
        workbook = xlsxwriter.Workbook(output_file)
        worksheet = workbook.add_worksheet()
        row = 0
        col = 0

        for i in range(0, len(self.ANALYTICS_BLOCKS_CLASSES)):
            worksheet.set_column("A:ZZ", 30)
            block_instance = self.ANALYTICS_BLOCKS_CLASSES[i](worksheet, workbook, row, col, self.data)
            block_instance.write_header()
            block_instance.write_data()

        workbook.close()