#파일안에 단어수 세기#
#단어 검색 후 개수 찾기
#반복
from msilib.schema import Directory
import re
while True:
    try:
        #인풋으로 파일 입력 받기
        filename = input("파일명을 입력해주세요 :")
        with open(filename, encoding='UTF-8') as data:
            words_list = data.readlines()
        str_words_list = " ".join(words_list)
        want_words = input("셀 단어수를 입력해 주세요 :")
    except FileNotFoundError as exception:
        print("찾으시는 파일이 디렉토리에 없습니다. 프로그램을 종료합니다.")
        break
    #리스트를 문자열로 변경
    print("파일 내 검색한 단어의 개수는 {}개 입니다.".format(str_words_list.count(want_words)))
    #세고싶은 단어 입력
    input_text = input("검색을 종료하시겠습니까?(y/n) :")
    if input_text in ["N", "n"]:
        continue
    if input_text in ["Y", "y"]:
        print("검색을 종료합니다.")
        break