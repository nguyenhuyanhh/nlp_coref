# Author: GAO Shengheng
# cleaned up unused imports and functionalities

import numpy as np
from sklearn.datasets import load_files
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn import metrics
from sklearn.cross_validation import train_test_split

# Loading data
print("starting reading")
inpath = "/home/nhanh/TDT2_top20"
all_texts = load_files(inpath)
print("finish reading")

(data_train, data_test,
 target_train, target_test=train_test_split(all_texts.data,
                                            all_texts.target,
                                            test_size=0.1))

print("training " + str(len(data_train)))
print("test " + str(len(data_test)))

text_clf = Pipeline([('vect', CountVectorizer(stop_words='english')),
                     ('tfidf', TfidfTransformer()),
                     ('clf', SGDClassifier(loss='log', penalty='l2',
                                           alpha=1e-3, n_iter=10,
                                           random_state=42))])
_ = text_clf.fit(data_train, target_train)
predicted = text_clf.predict(data_test)
print(np.mean(predicted == target_test))
print(metrics.classification_report(target_test, predicted,
                                    target_names=all_texts.target_names))
