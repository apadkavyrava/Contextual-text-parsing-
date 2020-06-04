# Contextual-text-parsing-
Advanced named entity recognition for cases not covert by libraries

The project consists four files:
1. Work sheet with collecting data (datasets, web scaping, used the generators)
2. Work sheet with moduling case 
3. File with traned NN.
4. Python file 

Let's considering the case when libraries can't recognise the meanning of words.

Made tokenization and used the Work2Vec. If the item consists of two words, was created a single vector for them with 300 features.

The first model was Random Forest which achieved 92% accuracy score. The Logistic Regression was used to chose Hyper parameters and RFE to choise the best features.

Next tried a neural network with 3 layers. It has achieved 97% accuracy. Then checked for overfitting, added dropout and ran k-fold cross-validation to ensure good fit. The resulting final score is 94%.

Pyhon file predict the meaning of the printed word.
