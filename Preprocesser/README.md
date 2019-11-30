# Preprocessor

Our preprocessor is based off of Anne Dirkson's [LexNorm](https://github.com/AnneDirkson/LexNorm) and [DrugNorm](https://github.com/AnneDirkson/DrugNorm) pipelines. 

The pipeline takes raw tweets and performs the following functions:
* Replaces URLs with "-URL-", removes usernames from email addresses while retaining the email domain, and removes copyright and trademark logos 
* Replaces twitter handles with “-TH-” (original code removed handles)
* Removes hashtags (if word starts with “\#”, remove “\#” symbol but keep the word)
* Replaces Twitter handles with “-TH-” (original code removed handles)
* Tokenization with NLTK 
* Implements DrugNorm drug normalizer to convert brand names of drugs to generic names.

## Required files
Prior to running, you will need to download the tetragram.binary in the N-gram-language-models [file](https://data.mendeley.com/datasets/dwr4xn8kcv/3) and the HealthVec [model](https://github.com/dartrevan/ChemTextMining/tree/master/word2vec).

You will also need to follow the steps in Dirkson's DrugNorm [repo](https://github.com/AnneDirkson/DrugNorm) to get access to the UMLS RxNorm dataset and generate the DrugNorm dictionary.
