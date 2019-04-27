import numpy as np
import gensim
import sys
sys.path.append("../")
from sdk.IO import IO
from sdk.TextProc import TextProc
from sdk.Feature import FeatureDraw
from sdk.Classifier import Classifier
from sdk.DataPresentation import DataPresentation
from sdk.Cluster import Cluster
from sdk.Feature import DataProcessing

feature_drawer = FeatureDraw()

# doc2vec_file = open("../BackUpSource/chapter_in_line", mode='r', encoding='utf-8')
# feature_drawer.Doc2Vec("../BackUpSource/Model/doc2vec_backup.model", doc2vec_file)

model = gensim.models.Doc2Vec.load("../../BackUpSource/Model/doc2vec_backup.model")
# scalars = np.array([model[word]for word in (model.wv.vocab) ])

labels = [0]*120
for i in range(80):
    labels[i] = 1

docvecs = [np.array(model.docvecs[i]) for i in range(len(model.docvecs))]
docvecs = np.array(docvecs)
print(docvecs.shape)
labels  = np.array(labels).reshape(120, )

# do data preproc
data_preprocer = DataProcessing()
docvecs = data_preprocer.ZeroCenterd(docvecs)
docvecs = data_preprocer.Normalized(docvecs)


# 先降维分析
dim_downer = DataPresentation(docvecs)
dim_downer.VecPic()


# 进行分类分析
classifier = Classifier(docvecs, labels)
classifier.Train()
classifier.GetAccuracy()

# 再进行聚类分析
cluster = Cluster(docvecs)
cluster.Cluster()
cluster.ToPics()
