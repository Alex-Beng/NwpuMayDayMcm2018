import string
# import jieba
import sys
import re

class TextProc():
    def __init__(self):
        pass
    def Divide2Chapter(self, raw_novel):
        pass
    def RmPuntuation(self, raw_text):
        pass
    def RmEnter(self, raw_text):
        pass
    def Divide2Word(self, chapter_text):
        pass

if __name__ == "__main__":
    raw_novel_path = "../../BackUpSource/RawNovel.txt"
    raw_novel_file = open(raw_novel_path, 'r', encoding="utf-8")

    raw_novel = ""
    line = raw_novel_file.readlines()
    print(line[:3])
    print(type(line))
    raw_novel = "".join(line)
    print(raw_novel[:100])
    print(type(raw_novel))

    # regex = re.compile('[\u4e00-\u9fa5]')
    regex = re.split('第.*.回 ',raw_novel)
    print(len(regex))
    print(regex[0])
    print()
    print(regex[1])
    # for i in regex:
    #     print(i[:10])