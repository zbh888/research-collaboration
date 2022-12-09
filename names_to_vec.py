import pandas as pd
import gensim
from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
import numpy as np
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


df = pd.read_csv('../Downloads/world-universities.csv', header = None, usecols = [1], names = ['name'])
df['type'] = 0 
df2 = pd.read_csv('../Downloads/tech_fundings.csv', usecols = [1], names = ['name'])
df2['type'] = 1
df3 = pd.concat([df, df2], ignore_index=True, names = ['name', 'type'], sort = True)


data = []
for i in df3.index:
    temp = []
    for j in word_tokenize(df3['name'][i]):
        temp.append(j.lower())
    data.append(temp)

df3['tokenized'] = data
size = 5
word2vec = Word2Vec(data, min_count = 1, vector_size = size)


vecs = []
for i in df3.index:
    temp = []
    tokens = word_tokenize(df3['name'][i])
    v = np.array([0] * size)
    for j in range(0, len(tokens)):
        temp = np.array(word2vec.wv[tokens[j].lower()])
        v = np.add(temp, v)
    v /= len(tokens)
    vecs.append(v)


X_train, X_test, y_train, y_test = train_test_split(np.asarray(vecs), df3['type'], test_size=0.2, random_state=0)

pca = PCA() 
X_train = pca.fit_transform(X_train)
print(pca.explained_variance_ratio_)
X_test = pca.transform(X_test)

classifier = RandomForestClassifier(random_state=0)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)
industry = 0
for y in y_test:
    if y == 1:
        industry += 1

print('industry: ' + str(industry) + '/' + str(len(y_test)))
print('Accuracy: ' + str(accuracy_score(y_test, y_pred)))