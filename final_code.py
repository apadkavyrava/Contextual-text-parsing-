#!/usr/bin/env python

import argparse
import spacy
import pandas as pd
import keras
from keras.models import load_model
from sklearn.preprocessing import LabelBinarizer

#if below doesn't work install lg model:
#!python -m spacy download en_core_web_lg

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("text", help="String to label")
    parser.add_argument("-m", "--model", help="Keras model .h5 file", default="model.h5")
    args = parser.parse_args()

    label = classify(args.text, args.model)
    print(label)


def classify(text, model_file):
    nlp = spacy.load("en_core_web_lg")
    LB = LabelBinarizer()
    LB.fit(['DATE', 'LOC', 'ORG', 'OTH', 'PRODUCT', 'RAN'])
    model = load_model(model_file)
    tokenised = nlp(text)
    vectors = [tokenised.vector]
    vectors_df = pd.DataFrame(vectors)
    y_pred_cat = model.predict(vectors_df)
    y_pred = LB.inverse_transform(y_pred_cat)
    return y_pred

if __name__ == "__main__":
    main()
