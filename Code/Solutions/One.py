import pickle
import numpy as np
import sys
sys.path.append("../")
from sdk.IO import IO
from sdk.TextProc import TextProc
from sdk.Feature import FeatureDraw
from sdk.Classifier import Classifier
from sdk.DataPresentation import DataPresentation
from sdk.Cluster import Cluster

# 首先是将章分出来

# sdk related
ioer            = IO()
text_procer     = TextProc()
feature_drawer  = FeatureDraw()

# get raw novel
raw_novel_path = "../../BackUpSource/RawNovel.txt"
raw_novel = ioer.ReadFile(raw_novel_path)
raw_novel = "".join(raw_novel)

# get chapters
chapters = text_procer.Divide2Chapter(raw_novel) 

# 然后分词，统计词频

# remove punctuation&enter, then divide to words
for i in range(len(chapters)):
    chapters[i] = text_procer.RmPuntuation(chapters[i])
    chapters[i] = text_procer.RmEnter(chapters[i])
    chapters[i] = text_procer.Divide2Word(chapters[i])

# count the words in each chapter
word_count_dict_list = []
for i in range(len(chapters)):
    word_count = feature_drawer.CountWord(chapters[i])
    word_count = dict(word_count)
    word_count_dict_list.append(word_count)

# init the name list
name_list = [
    '贾宝玉',
    '宝玉',
    '林黛玉',
    '黛玉',
    '薛宝钗',
    '宝钗',
    '王熙凤',
    '熙凤',
    '晴雯'
]

# get the word count vector
name_freq_vecs = []
for chapter_word_freq_dict in word_count_dict_list:
    freq_vec = []
    for name in name_list:
        if name in chapter_word_freq_dict:
            freq_vec.append(chapter_word_freq_dict[name])
        else:
            freq_vec.append(0)
    freq_vec = np.array(freq_vec)
    # print(freq_vec)
    name_freq_vecs.append(freq_vec)


# save the vecs
with open("../../BackupSource/name_freq_vec.data", 'wb') as f:
    pickle.dump(name_freq_vecs, f)

# 先降维分析

dim_downer = DataPresentation(name_freq_vecs)
dim_downer.VecPic()


# former80 label 1
# latter40 label 0
labels = [0]*120
for i in range(80):
    labels[i] = 1
print(len(labels), len(name_freq_vecs))

# 进行分类分析
# become np array
name_freq_vecs  = np.array(name_freq_vecs).reshape(120, len(name_list))
labels          = np.array(labels).reshape(120, )

classifier = Classifier(name_freq_vecs, labels)
classifier.Train()
classifier.GetAccuracy()

# 再进行聚类分析
cluster = Cluster(name_freq_vecs)
cluster.Cluster()
cluster.ToPics()
