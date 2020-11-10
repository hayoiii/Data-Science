import pandas as pd
import os
from konlpy.tag import Okt
import numpy as np

path = '/Users/iseungjin/PycharmProjects/DataScience/adj.txt'
star_list_path = './data/stars/'
output = './data/stars/star_adj/'


# 인덱스 작업에 포함되었던 최종 형용사 배열추출
def get_adj_list():
    f = open(path, 'r', encoding='utf-16')
    f = f.readlines()
    final_adj = []
    for i in f:
        i = i.replace('\n', '')
        final_adj.append(i)
    return final_adj



# 15명 연예인별로 5000개 기사에서 형용사 추출
def get_star_adj(star_name):
    twitter = Okt()

    star_txt = open(star_list_path + star_name, 'r', encoding='utf-8')
    star_txt = star_txt.readlines()

    sentences_tag = []
    for sentence in star_txt:
        # morpth - 형태소별로 나눠져서 저장됨.
        morph = twitter.pos(sentence)
        sentences_tag.append(morph)

    # 형용사인 품사만 선별해 리스트에 담기 ( 명사도 포함해도 괜찮을듯? 아닌가?)
    adj_list = []
    for sentence1 in sentences_tag:
        for word, tag in sentence1:
            # 형용사인것만 adj_list에 담겠다.
            if tag in ['Adjective']:
                adj_list.append(word)

    return adj_list


def check_adj(star_name):
    valid_adj = []
    for i in get_star_adj(star_name):
        if i in get_adj_list():
            valid_adj.append(i)
    return valid_adj

def execute():
    star_adj_list = []
    star_name = []
    star_list = os.listdir(star_list_path)
    for name in star_list:
        star_adj_list.append(check_adj(name))
        star_name.append(name)

    return star_name, star_adj_list

#execute()
















