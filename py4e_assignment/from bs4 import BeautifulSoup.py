from bs4 import BeautifulSoup

# 测试代码
html = "<p>Hello, <b>BeautifulSoup</b>!</p>"
soup = BeautifulSoup(html, "html.parser")
print(soup.get_text())  # 输出: Hello, BeautifulSoup!