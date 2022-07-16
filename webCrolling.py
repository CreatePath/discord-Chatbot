import requests
import re
from bs4 import BeautifulSoup

# 물리실험1 (순서대로 1페이지, 2페이지)
url1 = "https://physics.ssu.ac.kr/%ea%b0%95%ec%9d%98%ec%9e%90%eb%a3%8c/%ec%9d%bc%eb%b0%98%eb%ac%bc%eb%a6%ac%ec%8b%a4%ed%97%98/?term_id=29"
url2 = "https://physics.ssu.ac.kr/%ea%b0%95%ec%9d%98%ec%9e%90%eb%a3%8c/%ec%9d%bc%eb%b0%98%eb%ac%bc%eb%a6%ac%ec%8b%a4%ed%97%98/page/2/?term_id=29"
# 물리실험2&3 (순서대로 1페이지, 2페이지)
url3 = "https://physics.ssu.ac.kr/%ea%b0%95%ec%9d%98%ec%9e%90%eb%a3%8c/%ec%9d%bc%eb%b0%98%eb%ac%bc%eb%a6%ac%ec%8b%a4%ed%97%98/?term_id=30"
url4 = "https://physics.ssu.ac.kr/%ea%b0%95%ec%9d%98%ec%9e%90%eb%a3%8c/%ec%9d%bc%eb%b0%98%eb%ac%bc%eb%a6%ac%ec%8b%a4%ed%97%98/page/2/?term_id=30"

url_list = [url1, url2, url3, url4]

def findLink(experimentName):

    for url in url_list:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        for tag in soup.find_all('a'):
            if experimentName in tag.get_text():
                print(tag)
                tag_str = str(tag)
                start = tag_str.find('"')
                end = tag_str.rfind('"')
                link = tag_str[start+1:end].replace("amp;", "")
                print(link)         

findLink("등전위선")
