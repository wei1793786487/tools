import re
import requests
from bs4 import BeautifulSoup
from mongoUtils import insertOne
from toos import md5

get = requests.get("http://127.0.0.1:5500/src/demo.html")
soup = BeautifulSoup(get.text, features="lxml")
all = soup.find_all(class_="shiti")
for one in all:
    choose=[]
    type = one.find("span").text
    title = one.find("strong").text

    print(title)
    hava = "[判断题]" in type
    if not hava:
        find = one.find("li").text
        choose.append(find)
        print(find)
    # 那个傻逼写的那么长的代码笑死我了
    answer = re.findall(r"标准答案[\s\S]+</div>", str(one).replace(" ", ""))[0].replace("\r", "").replace("\n", "").replace(
        "标准答案：", "").replace(r"</div>", "")
    print(answer)
    id = md5(title)
    data={"_id": id,"question":title,"choose":choose,"answer":answer}
    insertOne(data)
