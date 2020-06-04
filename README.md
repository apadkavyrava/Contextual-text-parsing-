# Contextual-text-parsing-
Advanced named entity recognition for cases not covered by libraries

The project consists of four files:
1. Work sheet with data collection (datasets, web scraping, used the generators)
2. Work sheet with modeling case 
3. File with trained NN.
4. Python file 

Let's consider the case when libraries can't recognise the meaning of words.

Made tokenization and used the Word2Vec. If the item consists of two words, creating a single vector for them with 300 features.

The first model was Random Forest which achieved 92% accuracy score. The Logistic Regression was used to choose Hyper parameters and RFE to choose the best features.

Next tried a neural network with 3 layers. It has achieved 97% accuracy. Then checked for overfitting, added dropout and ran k-fold cross-validation to ensure good fit. The resulting final score is 94%.

Pyhon file predicts the meaning of the printed word.
