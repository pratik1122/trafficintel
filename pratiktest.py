from pycel import ExcelCompiler


filename = "/home/kevit/Downloads/ppp.xlsx"


excel = ExcelCompiler(filename=filename)
excel.evaluate('Backtest')


excel.validate_calcs(output_addrs=['Backtest'])
print(" M17 is {}".format(excel.evaluate('Backtest!M17')))



# for col in worksheet.iter_cols(min_col=14, max_col=14, min_row=6, max_row=22):
        # # #      for cell in col:
        # # #          new_result = ((cell.value - temp) / temp) * 100
        # # #          print('cell value', cell.value)
        # # #          print('temp', temp)
        # # #          print('new_result', new_result)
        # # #          difference = new_result - result
        # # #          print('difference', difference)
        # # #          if difference > 10:
        # # #              print('There is problem with the market place requests data ', cell.value)
        # # #              l2.append(cell.row)
        # # #
        # # #          result = new_result
        # # #          print('result', result)
        # # #          temp = cell.value
        # # #          print('temp', temp)
        # #
        # #  # a = worksheet['V4'].value
        # #  # print('a', a)
        # #  # temp = worksheet['V5'].value
        # #  # print('temp', temp)
        # #  # result = ((temp - a) / a) * 100
        # #  # print('result', result)
        # #
        # #  # for col in worksheet.iter_cols(min_col= 22, max_col=22, min_row=6, max_row=21):
        # #  #     for cell in col:
        # #  #         new_result = ((cell.value - temp) / temp) * 100
        # #  #         print('cell value', cell.value)
        # #  #         print('temp', temp)
        # #  #
        # #  #         print('new_result', new_result)
        # #  #
        # #  #         difference = new_result - result
        # #  #         print('difference', difference)
        # #  #         if difference > 10:
        # #  #             print('There is problem with the market place  revenue data ', cell.value)
        # #  #         result = new_result
        # #  #         print('result', result)
        # #  #         temp = cell.value
        # #  #         print('temp', temp)
        # #
        # #                                                  ##########################
        # #
        # #
        # #
        # # # print(worksheet['P10'].value)
        #
        # #
        # # excel_data = list()
        # # # iterating over the rows and column
        # # # getting value from each cell in row
        # # for row in worksheet.iter_rows(min_row=5):
        # #     row_data = list()
        # #
        # #     for cell in row:
        # #         if cell.value is None:
        # #             continue
        # #
        # #         row_data.append(str(cell.value))
        # #     excel_data.append(row_data)
        # #
        # #
        # #
        #
        #
        # # # a = worksheet[first_cell_index].value
        # # # print('a', a)
        # # # temp = worksheet[second_cell_index].value
        # # # print('temp', temp)
        # # # result = ((temp - a) / a) * 100
        # # # print('result', result)
        # # # l1 = []
        # # #
        # # # mirow = int(min_row)
        # # # marow = int(max_row)
        # # # icol = int(column)
        # # #
        # # #
        # # #
        # # # for col in worksheet.iter_cols(min_col= icol, max_col= icol, min_row= mirow, max_row= marow):
        # # #     for cell in col:
        # # #         new_result = ((cell.value - temp) / temp) * 100
        # # #         print('cell value', cell.value)
        # # #         print('temp', temp)
        # # #         print('new_result', new_result)
        # # #         difference = new_result - result
        # # #         print('difference', difference)
        # # #         if difference > 10 or difference < -10:
        # # #             print('There is problem with the unique visitor data ', cell.value)
        # # #             l1.append(cell.row)
        # # #
        # # #         result = new_result
        # # #         print('result', result)
        # # #         temp = cell.value
        # # #         print('temp', temp)
        # # #     print(l1)
        # #
        # # #
        # # # icolumn = int(column)
        # # # imin_row = int(min_row)
        # # # imax_row = int(max_row)
        # # #
        # # # temp = worksheet[first_cell_index].value * 100
        # # # print('temp', temp)
        # # # l1=[]
        # # #
        # # #
        # # # for col in worksheet.iter_cols(min_col= icolumn,max_col= icolumn,min_row= imin_row,max_row= imax_row):
        # # #     for cell in col:
        # # #         a = cell.value *100
        # # #         difference = (a - temp)
        # # #         if difference >10 or difference < -10:
        # # #             print(cell.row)
        # # #             print('there is faulty data ',  cell.value)
        # # #             l1.append(cell.row)
        # # #
        # # #         temp = cell.value * 100




