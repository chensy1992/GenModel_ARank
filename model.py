import numpy as np
import random
from sklearn import svm
from sklearn import metrics
from sklearn.cross_validation import train_test_split
import pickle
import time

def rankcount(rank, crop_size):
    crank = [0] * crop_size
    for i in rank:
        crank[int(i)] += 1
    crank.append(np.mean(rank))
    crank.append(np.std(rank))
    return crank

def model_SVM_RBF():
    X = []
    y = []
    trainf = open('ranks.txt')
    t1 = time.time()
    len_imglist = 2
    for line in trainf:
            linesplit = line.strip().split(' ')
            feature = []
            for i in range(0, len(linesplit) - 1, 9):
                l = linesplit[i: i + 9]
                ll = np.zeros(7)
                for ini in range(7):
                    ll[ini] = int(l[ini])
                crank = rankcount(ll, 20)
                crank.append(float(l[7]))
                crank.append(float(l[8]))
                feature.extend(crank)
            X.append(feature)
            y.append(int(linesplit[9 * len_imglist]))
    print(np.shape(X))
    print(np.shape(y))

    clf = svm.SVC(kernel='rbf',probability=True).fit(X, y)
    pro_matrixf = open('model_rbf_711_old', 'wb')
    pickle.dump(clf, pro_matrixf, protocol=2)


def model_SVM_linear():
    X = []
    y = []
    trainf = open('ranks.txt')
    t1 = time.time()
    len_imglist = 2
    for line in trainf:
            linesplit = line.strip().split(' ')
            feature = []
            for i in range(0, len(linesplit) - 1, 9):
                l = linesplit[i: i + 9]
                ll = np.zeros(7)
                for ini in range(7):
                    ll[ini] = int(l[ini])
                crank = rankcount(ll, 20)
                crank.append(float(l[7]))
                crank.append(float(l[8]))
                feature.extend(crank)
            X.append(feature)
            y.append(int(linesplit[9 * len_imglist]))
    print(np.shape(X))
    print(np.shape(y))
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    print(X_train[0])
    # svm classification
    '''
    clf = svm.SVC(kernel='linear',  gamma=0.7, C = 1).fit(X_train, y_train)
    y_predicted = clf.predict(X_test)
    t2 = time.time()
    print('cost time:', t2 - t1)

    print("Classification report for %s" % clf)
    print
    print(metrics.classification_report(y_test, y_predicted))
    print
    print("Confusion matrix")
    print(metrics.confusion_matrix(y_test, y_predicted))

    '''
    clf = svm.SVC(kernel='linear',  gamma=0.7, C = 1, probability=True).fit(X, y)
    pro_matrixf = open('model_svm_linear_711_old', 'wb')
    pickle.dump(clf, pro_matrixf, protocol=2)

def main():
    #model_SVM_RBF()
    model_SVM_linear()

if __name__ == '__main__':
    main()



