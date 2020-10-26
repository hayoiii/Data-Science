# 1. NLTK (natural language toolkit패키지 - 자연어처리패키지)
# VADER어휘사전이용 - nltk. sentiment.vader 모듈에 구현되어있는것 가져옴

#nltk.download() --> 이거먼저 실행시켜서 패키지파일 다운받아야 nltk사용가능!!! ( 실행하면 새로운 윈도우창이 뜸)
from nltk.sentiment.vader import SentimentIntensityAnalyzer

analyser = SentimentIntensityAnalyzer()
# txt파일읽은걸로 바꾸면댐
input_file = open("/Users/iseungjin/PycharmProjects/DataScience/data/sentiment_test.txt",'r',encoding='utf-8')
lines = input_file.readlines()
input_file.close()

star_name = "유이"
output_file = open('./data/'+ star_name + '의 평판분석.txt', 'w', encoding='utf-8')

# 해당 텍스트를 긍정/부정을 0.0~1.0사이의 값으로 알려줌
# score = pos(positive), neg(negative), neu(neutral), compound(혼합점수(?))
def text_to_binary(text):
    score = analyser.polarity_scores(text)
    # 부정점수가 0이상, 혼합점수가 음수면 부정적이라고 판단하기로 직접 설정
    if score['neg']>0 and score['compound']<0:
        sentiment = '부정적'
    # 긍정점수가 0이상, 혼합점수가 양수면 긍정적이라고 판단
    elif score['pos']>0 and score['compound']>0:
        sentiment = '긍정적'
    # 나머지에 대해서는 중립적
    else:
        sentiment = '중립적'

    return sentiment


print(star_name,'평판분석')
output_file.write(star_name)
output_file.write('\n')

pos = 0
neg = 0

for i, f in enumerate(lines):
    f = f.replace('\n', '')
    sentiment_test = text_to_binary(f)
    print('%s번째 형용사 %s는 %s입니다.\n'%(i,f,sentiment_test))
    output = '%s번째 형용사 %s는 %s입니다.\n'%(i,f,sentiment_test)
    # 중립은 그냥 빼는걸로함
    if sentiment_test == '긍정적':
        pos += 1
    elif sentiment_test == '부정적':
        neg += 1
    output_file.write(output)

pos_rate = float(pos / len(lines))
neg_rate = float(neg / len(lines))

percentage = '긍정적 비율-%f, 부정적비율-%f\n'%(pos_rate, neg_rate)
print(percentage)
output_file.write(percentage)