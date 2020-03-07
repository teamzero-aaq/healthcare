from tkinter import *

import numpy as np
import pandas as pd

# from gui_stuff import *

l1 = ['acidity', 'vomiting', 'indigestion', 'headache', 'nausea', 'blurred_and_distorted_vision', 'chest_pain',
      'dizziness', 'excessive_hunger', 'stiff_neck', 'spinning_movements', 'loss_of_balance', 'unsteadiness',
      'weakness_of_one_body_side', 'depression', 'irritability', 'altered_sensorium', 'lack_of_concentration',
      'visual_disturbances']

disease = ['Hypertension', 'Migraine', 'Paralysis (brain hemorrhage)', '(vertigo) Paroymsal  Positional Vertigo']

l2 = []
for x in range(0, len(l1)):
    l2.append(0)

# TESTING DATA df -------------------------------------------------------------------------------------
df = pd.read_csv("Training.csv")

df.replace({'prognosis': {'Hypertension ': 1, 'Migraine': 2, 'Paralysis (brain hemorrhage)': 3,
                          '(vertigo) Paroymsal  Positional Vertigo': 4}}, inplace=True)

# print(df.head())

X = df[l1]

y = df[["prognosis"]]
np.ravel(y)
# print(y)

# TRAINING DATA tr --------------------------------------------------------------------------------
tr = pd.read_csv("Testing.csv")
tr.replace({'prognosis': {'Hypertension ': 1, 'Migraine': 2, 'Paralysis (brain hemorrhage)': 3,
                          '(vertigo) Paroymsal  Positional Vertigo': 4}}, inplace=True)

X_test = tr[l1]
y_test = tr[["prognosis"]]
np.ravel(y_test)


# ------------------------------------------------------------------------------------------------------

def DecisionTree():
    from sklearn import tree

    clf3 = tree.DecisionTreeClassifier()  # empty model of the decision tree
    clf3 = clf3.fit(X, y)

    # calculating accuracy-------------------------------------------------------------------
    from sklearn.metrics import accuracy_score
    y_pred = clf3.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred, normalize=False))
    # -----------------------------------------------------

    psymptoms = [Symptom1.get(), Symptom2.get(), Symptom3.get(), Symptom4.get(), Symptom5.get()]

    for k in range(0, len(l1)):
        # print (k,)
        for z in psymptoms:
            if (z == l1[k]):
                l2[k] = 1

    inputtest = [l2]
    predict = clf3.predict(inputtest)
    predicted = predict[0]

    h = 'no'
    for a in range(0, len(disease)):
        if (predicted == a):
            h = 'yes'
            break

    if (h == 'yes'):
        t1.delete("1.0", END)
        t1.insert(END, disease[a])
    else:
        t1.delete("1.0", END)
        t1.insert(END, "Not Found")


def randomforest():
    from sklearn.ensemble import RandomForestClassifier
    clf4 = RandomForestClassifier()
    clf4 = clf4.fit(X, np.ravel(y))

    # calculating accuracy-------------------------------------------------------------------
    from sklearn.metrics import accuracy_score
    y_pred = clf4.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred, normalize=False))
    # -----------------------------------------------------

    psymptoms = [Symptom1.get(), Symptom2.get(), Symptom3.get(), Symptom4.get(), Symptom5.get()]

    for k in range(0, len(l1)):
        for z in psymptoms:
            if (z == l1[k]):
                l2[k] = 1

    inputtest = [l2]
    predict = clf4.predict(inputtest)
    predicted = predict[0]

    h = 'no'
    for a in range(0, len(disease)):
        if (predicted == a):
            h = 'yes'
            break

    if (h == 'yes'):
        t2.delete("1.0", END)
        t2.insert(END, disease[a])
    else:
        t2.delete("1.0", END)
        t2.insert(END, "Not Found")


def NaiveBayes():
    from sklearn.naive_bayes import GaussianNB
    gnb = GaussianNB()
    gnb = gnb.fit(X, np.ravel(y))

    # calculating accuracy-------------------------------------------------------------------
    from sklearn.metrics import accuracy_score
    y_pred = gnb.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred, normalize=False))
    # -----------------------------------------------------

    psymptoms = [Symptom1.get(), Symptom2.get(), Symptom3.get(), Symptom4.get(), Symptom5.get()]
    for k in range(0, len(l1)):
        for z in psymptoms:
            if (z == l1[k]):
                l2[k] = 1

    inputtest = [l2]
    predict = gnb.predict(inputtest)
    predicted = predict[0]

    h = 'no'
    for a in range(0, len(disease)):
        if (predicted == a):
            h = 'yes'
            break

    if (h == 'yes'):
        t3.delete("1.0", END)
        t3.insert(END, disease[a])
    else:
        t3.delete("1.0", END)
        t3.insert(END, "Not Found")


# gui_stuff------------------------------------------------------------------------------------

root = Tk()
root.configure(background='white')

# entry variables
Symptom1 = StringVar()
Symptom1.set(None)
Symptom2 = StringVar()
Symptom2.set(None)
Symptom3 = StringVar()
Symptom3.set(None)
Symptom4 = StringVar()
Symptom4.set(None)
Symptom5 = StringVar()
Symptom5.set(None)
Name = StringVar()

# labels
S1Lb = Label(root, text="Symptom 1", fg="yellow", bg="black")
S1Lb.grid(row=7, column=0, pady=10, sticky=W)

S2Lb = Label(root, text="Symptom 2", fg="yellow", bg="black")
S2Lb.grid(row=8, column=0, pady=10, sticky=W)

S3Lb = Label(root, text="Symptom 3", fg="yellow", bg="black")
S3Lb.grid(row=9, column=0, pady=10, sticky=W)

S4Lb = Label(root, text="Symptom 4", fg="yellow", bg="black")
S4Lb.grid(row=10, column=0, pady=10, sticky=W)

S5Lb = Label(root, text="Symptom 5", fg="yellow", bg="black")
S5Lb.grid(row=11, column=0, pady=10, sticky=W)

lrLb = Label(root, text="DecisionTree", fg="white", bg="red")
lrLb.grid(row=15, column=0, pady=10, sticky=W)

destreeLb = Label(root, text="RandomForest", fg="white", bg="red")
destreeLb.grid(row=17, column=0, pady=10, sticky=W)

ranfLb = Label(root, text="NaiveBayes", fg="white", bg="red")
ranfLb.grid(row=19, column=0, pady=10, sticky=W)

# entries
OPTIONS = sorted(l1)

S1En = OptionMenu(root, Symptom1, *OPTIONS)
S1En.grid(row=7, column=1, padx=10)

S2En = OptionMenu(root, Symptom2, *OPTIONS)
S2En.grid(row=8, column=1)

S3En = OptionMenu(root, Symptom3, *OPTIONS)
S3En.grid(row=9, column=1)

S4En = OptionMenu(root, Symptom4, *OPTIONS)
S4En.grid(row=10, column=1)

S5En = OptionMenu(root, Symptom5, *OPTIONS)
S5En.grid(row=11, column=1)

dst = Button(root, text="DecisionTree", command=DecisionTree, bg="green", fg="yellow")
dst.grid(row=8, column=3, padx=10)

rnf = Button(root, text="Randomforest", command=randomforest, bg="green", fg="yellow")
rnf.grid(row=9, column=3, padx=10)

lr = Button(root, text="NaiveBayes", command=NaiveBayes, bg="green", fg="yellow")
lr.grid(row=10, column=3, padx=10)

# textfileds
t1 = Text(root, height=1, width=40, bg="orange", fg="black")
t1.grid(row=15, column=1, padx=10)

t2 = Text(root, height=1, width=40, bg="orange", fg="black")
t2.grid(row=17, column=1, padx=10)

t3 = Text(root, height=1, width=40, bg="orange", fg="black")
t3.grid(row=19, column=1, padx=10)

root.mainloop()
