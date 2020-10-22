from collections import Counter

# @@@연예인의 크롤링한 기사제목 파일 --> 읽기전용으로 호출함
file = open('/Users/iseungjin/text1.txt','r',encoding='utf-8')
lines = file.readlines()

# 2. 배열 news에 전체댓글을 다시저장(한줄씩)
news = []
for line in lines:
    news.append(line)
file.close()

# 3. 트윗터 패키지 안에 konlpy 모듈호출
from konlpy.tag import Okt
twitter = Okt()

# 각 문장별로 형태소 구분하기
sentences_tag = []
for sentence in news:
    # morpth - 형태소별로 나눠져서 저장됨.
    morph = twitter.pos(sentence)
    sentences_tag.append(morph)
    print(morph)
    print('-'*30,'다음기사제목입니당')

print(sentences_tag)
print(len(sentences_tag))
print('\n'*3)

# 형용사인 품사만 선별해 리스트에 담기 ( 명사도 포함해도 괜찮을듯? 아닌가?)
adj_list = []
for sentence1 in sentences_tag:
    for word, tag in sentence1:
        # 형용사인것만 adj_list에 담겠다.
        if tag in ['Adjective']:
            adj_list.append(word)

# 빈도수 계산 & 상위 빈도 10위 까지 출력
counts = Counter(adj_list)
print(counts.most_common(10))