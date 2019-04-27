import random
import numpy as np
import logging
import gensim

class FeatureDraw:
    def __init__(self):
        pass
    def CountWord(self, divided_text, chapter_idx):
        # 以词为 key ，频数为 value
        # 然后根据频数对 key 进行排序后返回
        word_freq = {}
        word_list = divided_text.split()

        for word in word_list:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1
        return sorted(word_freq.items(), key=lambda k:k[1], reverse=True)
    
    def Word2Vec(self, sentences, save_path):
        model = gensim.models.Word2Vec(sentences)
        model.save(save_path)

    def Doc2Vec(self, sentences, save_path, file_handler):
        sentences=gensim.models.doc2vec.TaggedLineDocument(file_handler)
        model = gensim.models.Doc2Vec(sentences)
        model.save(save_path)

class DataProcessing:
    def __init__(self):
        pass
    def DivideDataset(self, data_list, testset_ratio = 0.25):
        # random 划分测试集，剩下为训练集合
        testset_size = len(data_list)*testset_ratio
        
        testset = set()
        trainset = set()

        while len(testset) < testset_size:
            lucky_dog = random.choice(data_list)
            testset.add(lucky_dog)
        
        trainset = set(data_list) - testset

        return testset, trainset
    def ZeroCenterd(self, raw_vecs):
        raw_vecs -= np.mean(raw_vecs, axis=0)
        return raw_vecs
    def Normalized(self, raw_vecs):
        raw_vecs /= np.std(raw_vecs, axis=0)
        return raw_vecs
if __name__ == "__main__":
    from IO import IO
    ioer = IO()

    chapters = ioer.ReadFiles("../../BackUpSource/Chapters/", "chapter", 1, 120)
    chapters = [i[0] for i in chapters]

    feature_drawer = FeatureDraw()

    word_count = feature_drawer.CountWord(chapters[0], 1)
    
    # for i in word_count:
    #     print(i[0], i[1])
    
    feature_drawer.Word2Vec(chapters[0], "../../BackUpSource/Model/test.model")
    
    doc2vec_file = open("../../BackUpSource/chapter_in_line", mode='r', encoding='utf-8')
    feature_drawer.Doc2Vec(chapters, "../../BackUpSource/Model/test.model", doc2vec_file)
    