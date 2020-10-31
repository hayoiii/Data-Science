import os
import sys
import urllib.request
import json

# 하루 오백개엿나 제한있음.
client_id = "1gqRqGiKGu9mMxJtPJTt" # 개발자센터에서 발급받은 Client ID 값
client_secret = "2Qpbm0AYfT" # 개발자센터에서 발급받은 Client Secret 값

url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)

f = open('./data/sentiment_test.txt', 'r', encoding='utf-8')
output = open('./data/translated.txt', 'w')
line = f.readline()
kor_array = line.split(',')

eng_array = []

for i in range(len(kor_array)):
    encText = urllib.parse.quote(kor_array[i])
    data = "source=ko&target=en&text=" + encText

    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        #print(response_body.decode('utf-8'))
        data = response_body.decode('utf-8')
        data = json.loads(data)
        trans_text = data["message"]["result"]["translatedText"]
        output.write(trans_text)
        # sentimental분석할때 입력이 한줄씩 들어가는걸로 짜놔서 
        output.write('\n')
        eng_array.append(trans_text)
    else:
        print("Error Code:" + rescode)



print(kor_array)
print(eng_array)
