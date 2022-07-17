import requests
from bs4 import BeautifulSoup

# 물리실험1 (순서대로 1페이지, 2페이지)
url1 = "https://physics.ssu.ac.kr/%ea%b0%95%ec%9d%98%ec%9e%90%eb%a3%8c/%ec%9d%bc%eb%b0%98%eb%ac%bc%eb%a6%ac%ec%8b%a4%ed%97%98/?term_id=29"
url2 = "https://physics.ssu.ac.kr/%ea%b0%95%ec%9d%98%ec%9e%90%eb%a3%8c/%ec%9d%bc%eb%b0%98%eb%ac%bc%eb%a6%ac%ec%8b%a4%ed%97%98/page/2/?term_id=29"
# 물리실험2&3 (순서대로 1페이지, 2페이지)
url3 = "https://physics.ssu.ac.kr/%ea%b0%95%ec%9d%98%ec%9e%90%eb%a3%8c/%ec%9d%bc%eb%b0%98%eb%ac%bc%eb%a6%ac%ec%8b%a4%ed%97%98/?term_id=30"
url4 = "https://physics.ssu.ac.kr/%ea%b0%95%ec%9d%98%ec%9e%90%eb%a3%8c/%ec%9d%bc%eb%b0%98%eb%ac%bc%eb%a6%ac%ec%8b%a4%ed%97%98/page/2/?term_id=30"

url_list = [url1, url2, url3, url4]

def exp_url(experimentName):
    for url in url_list:
        response = requests.get(url) # url로 get요청을 보냄
        soup = BeautifulSoup(response.content, 'html.parser') # response로 받은 html 파일을 분석 

        for tag in soup.find_all('a'): # 모든 a 태그 반환
            if experimentName in tag.get_text(): # 태그의 텍스트를 가져와서 사용자가 입력한 문자열을 갖고 있는지 검사. 있으면 link 추출 및 반환
                tag_str = str(tag)
                start = tag_str.find('"')
                end = tag_str.rfind('"')
                link = tag_str[start+1:end].replace("amp;", "")
    try: 
        print(link)
    except UnboundLocalError: # link가 정의되지 않았다는 에러가 뜨면 링크를 못찾겠다는 msg 생성. 에러가 없으면 msg에 link 복사.
        msg = "링크를 못찾겠어요."
    else:
        msg = link
    return msg

