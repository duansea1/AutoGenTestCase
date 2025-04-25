import xlsxwriter


def generate_testcase_excel(testcases, output_path):
    if isinstance(testcases, str):
        testcases = [{'编号': testcases}]
    workbook = xlsxwriter.Workbook(output_path)
    worksheet = workbook.add_worksheet('测试用例')

    # 写入表头
    headers = ['测试用例编号', '测试目的', '前置条件', '测试步骤', '预期结果', '实际结果', '测试状态']
    for col, header in enumerate(headers):
        worksheet.write(0, col, header)

    # 写入测试用例数据
    for row, testcase in enumerate(testcases, start=1):
        worksheet.write(row, 0, testcase.get('编号', ''))
        worksheet.write(row, 1, testcase.get('目的', ''))
        worksheet.write(row, 2, testcase.get('前置条件', ''))
        worksheet.write(row, 3, testcase.get('步骤', ''))
        worksheet.write(row, 4, testcase.get('预期结果', ''))
        worksheet.write(row, 5, testcase.get('实际结果', ''))
        worksheet.write(row, 6, testcase.get('状态', ''))

    workbook.close()