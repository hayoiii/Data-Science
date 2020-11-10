import os
import sys
import urllib.request
import urllib.parse
import json
import popular

star_name, star_adj_kor = popular.execute()
print('임포트완료...')


# 하루 오백개엿나 제한있음.
client_id = "1gqRqGiKGu9mMxJtPJTt" # 개발자센터에서 발급받은 Client ID 값
client_secret = "2Qpbm0AYfT" # 개발자센터에서 발급받은 Client Secret 값

url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)

output_path = './data/eng_adj/'


for i in range(len(star_adj_kor)):
    output = open('./data/eng_adj/{}'.format(star_name[i]), 'w', encoding='utf-8')
    print('./data/eng_adj/{}.... 생성...'.format(star_name[i]))
    print('번역 요청...')
    for j in star_adj_kor[i]:
        encText = urllib.parse.quote(j)
        data = "source=ko&target=en&text=" + encText
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        rescode = response.getcode()
        if (rescode == 200):
            response_body = response.read()
            # print(response_body.decode('utf-8'))
            data = response_body.decode('utf-8')
            data = json.loads(data)
            trans_text = data["message"]["result"]["translatedText"]
            output.write(trans_text)
            # sentimental분석할때 입력이 한줄씩 들어가는걸로 짜놔서
            output.write('\n')
            #eng_array.append(trans_text)
        else:
            print("Error Code:" + rescode)

