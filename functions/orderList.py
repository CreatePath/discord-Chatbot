def orderList():
    order_text = ">>> **명령어 모음**\n"
    order_list = {
        "./안녕" : "봇이 인사함.",
        "./따라하기 __*하고싶은말*__" : "봇이 사용자의 말을 따라함.",
        "./물리실험 __*실험키워드*__" : "물리학과 홈페이지에서 실험보고서 링크를 가져옴."
    }
    for order in order_list:
        order_text += "**" + order + "**\n"
        order_text += order_list[order] + "\n"
    return order_text