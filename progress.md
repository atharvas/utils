## Lit Review
 > Glove
	* https://blog.acolyer.org/2016/04/22/glove-global-vectors-for-word-representation/
 > word2vec
	* https://blog.acolyer.org/2016/06/01/distributed-representations-of-sentences-and-documents/
	* A general idea about word vectors:
	* https://blog.acolyer.org/2016/04/21/the-amazing-power-of-word-vectors/
 > tweestar
	* Best model for task B
	* approach: different models capture different sentiments. trained multiple classifiers on data (data was cleaned and was processed as word embeddings)
	* late fusion ?
 > semeval 2016
 > nlp notes
 > jurafsky
 > sent140
	* assumption
 > ?
 
 ## Experiments tried
 > prepros with spacy
	* batch.
 > naive Bayes
	*  Multinomial Naive bayes with counting
	*  Multinomial Naive bayes with tf-idf (best so far)
	*  Multinomial Naive bayes with word2vec
	*  Multinomial Naive bayes with glove (100 dim)
 > MaxEnt (best so far?)
	*  MaxEnt  with counting
	*  MaxEnt with tf-idf (best so far)
	*  MaxEnt with word2vec
	*  MaxEnt with glove (100 dim)

 
