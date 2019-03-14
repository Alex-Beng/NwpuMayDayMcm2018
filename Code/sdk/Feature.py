import random
import numpy as np
import logging

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
    
    def Word2Vec(self):
        pass
    def Doc2Vec(self):
        pass 

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
    pass