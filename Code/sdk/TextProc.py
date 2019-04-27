import jieba
import re

class TextProc():
    def __init__(self):
        pass
    def Divide2Chapter(self, raw_novel):
        # 通过正则匹配 第xx回 ，然后通过匹配结果的分段
        # 因为 第一回 之前的那段是标题作者etc，与正文无关，故删去
        divided_parts = re.split('第.*.回 ', raw_novel)
        del divided_parts[0]

        return divided_parts
    def RmPuntuation(self, raw_text):
        # 通过正则匹配中文&空白符，然后取反^即是标点符号
        # 然后使用 sub 函数替换成 ' '
        regex = re.compile("[^\u4e00-\u9fa5a-zA-Z0-9\s]")
        return regex.sub(' ', raw_text)
    def RmEnter(self, raw_text):
        # 回车类似删去标点
        # 须注意 Unix/Linix 中换行 \n 回车 \r
        regex = re.compile("[\r\n]")
        return regex.sub(' ', raw_text)
    def Divide2Word(self, raw_text):
        # 使用 jieba 库分词，关闭全模式
        divided_list = jieba.cut(raw_text, cut_all=False)
        return ' '.join(divided_list)
    
if __name__ == "__main__":
    from IO import IO
    ioer = IO()

    raw_novel_path = "../../BackUpSource/RawNovel.txt"

    raw_novel = ioer.ReadFile(raw_novel_path)
    raw_novel = "".join(raw_novel)

    text_procer = TextProc()
    
    chapters = text_procer.Divide2Chapter(raw_novel)

    ioer.WriteFiles(chapters, "../../BackUpSource/Chapters/", "chapter", 1, 120)

    chapters = ioer.ReadFiles("../../BackUpSource/Chapters", 'chapter', 1, 120)

    for i in chapters:
        print(i[:1])

