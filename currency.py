from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
browser = webdriver.Edge()
def get_currency_name():
    # 创建浏览器对象

    # 打开目标网页
    url = "https://www.11meigui.com/tools/currency"
    browser.get(url)
    # 找到符合条件的 table 元素
    table = browser.find_element(By.ID, "desc")

    # 找到除去 align="center" 的每个 tr 元素
    rows = table.find_elements(By.XPATH, '//tr[not(@align="center")]')

    # 遍历每个 tr 元素，获取第一个和第五个 td 元素的文本内容
    data = []
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        if len(cells) == 6:
            first_td_content = cells[1].text.strip()
            fifth_td_content = cells[4].text.strip()
            data.append((first_td_content, fifth_td_content))

    # 关闭浏览器
    browser.quit()

    # 将数据写入指定文件
    output_file = "result.txt"
    with open(output_file, "w") as f:
        for item in data:
            f.write(f"{item[0]}\t{item[1]}\n")

    print(f"数据已写入文件: {output_file}")
def find_item_in_file(file_path, search_item):
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            items = line.split("\t")  # 根据空格分割每一行的数据项
            if search_item in items:
                index = items.index(search_item)
                currence_name = items[index-1]
                # print(currence_name)
                return currence_name
    # 没有找到匹配的行
    return None
def get_prince():
    # 日期和货币代号通过命令行参数传入
    date = sys.argv[1]
    currency = sys.argv[2]
    date = datetime.strptime(date, "%Y%m%d")
    date = date.strftime("%Y-%m-%d")
    currency=find_item_in_file("./result.txt",currency)
    if currency==None:
        print("货币查找失败，请确认输入")
    url = "https://www.boc.cn/sourcedb/whpj/"
    browser.get(url)
    table = browser.find_element(By.XPATH, '//table[@align="left"]')
    table_rows = table.find_elements(By.TAG_NAME, 'tr')
    for row in table_rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        if len(cells) == 8:
            if cells[0].text == currency and cells[6].text == date:
                print(cells[3].text )
    # 关闭浏览器
    browser.quit()
if __name__ == "__main__":
    # get_currency_name()
    get_prince()