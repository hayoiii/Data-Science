# -*-coding:utf-8-*-

name_file = open('./namelist.txt', 'r')     # 연예인 이름 리스트의 텍스트 파일 (구분자는 '\n'으로 가정)
article_file = open('./data.txt', 'r')      # 크롤링한 기사 제목들의 텍스트 파일 (구분자는 '\n'으로 가정)
output_file = open('./output.txt', 'w')     # 언급 횟수의 내림차순으로 결과값을 쓸 텍스트파일 (비어있어야 함 구분자는 ','와 '\n')

# name_count_dict: {연예인 이름 : 언급 횟수}
name_count_dict = {}
# namelist: 연예인 이름 리스트.txt에 있는 모든 이름들의 리스트
namelist = []

# namelist 만들기
while True:
    name = name_file.readline()
    if name == '':
        break
    name = name[:-1]        # '\n' 제거
    namelist.append(name)

name_file.close()


while True:
    # 크롤링한 기사 제목 한 줄을 읽어옴
    article = article_file.readline()
    # 크롤링한 기사 제목을 모두 읽었으면 break
    if article == '':
        break

    # namelist 안의 모든 연예인 이름에 대해서 기사 제목에 포함되는 이름이 있는 지 확인
    for name in namelist:
        if name in article:
            # 아직 dict에 한 번도 추가된 적이 없으면 value = 1로 생성
            if not (name in name_count_dict):
                name_count_dict[name] = 1
            # dict에 추가된 적이 있으면 value++
            else:
                name_count_dict[name] += 1
            # 제목에 포함된 연예인 찾았으면 다음 기사로 넘어가기
            break

# dict의 value값 (언급 횟수)를 기준으로 내림차순 정렬
name_count_dict = sorted(name_count_dict.items(), reverse=True, key=lambda item: item[1])

print('name\tcount\t')
print('---------------')
for key, value in name_count_dict:
    # output 파일에 결과 쓰기
    output_file.write(key + ',' + str(value)+'\n')
    print(key + " \t", value)

output_file.readlines()
article_file.close()
output_file.close()
