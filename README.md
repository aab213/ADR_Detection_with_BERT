# ADR Detection with BERT
Amy Breden & Lee Moore
<br>UC Berkeley Master of Information and Data Science (MIDS)
<br> W266 - Natural Language Processing & Deep Learning - Final Project

## Abstract
The automation of adverse drug reaction (ADR) detection in social media would revolutionize the practice of pharmacovigilance, supporting drug regulators, the pharmaceutical industry and the general public in ensuring the safety of the drugs prescribed in daily practice. Following from the published proceedings of the Social Media Mining for Health (SMM4H) Applications Workshop & Shared Task in August 2019, we aimed to develop a deep learning model to classify ADRs within Twitter tweets that contain drug mentions. Our approach involved fine-tuning $BERT_{LARGE}$ and two domain-specific BERT implementations, BioBERT and Bio + clinicalBERT, applying a domain-specific preprocessor, and developing a max-prediction ensembling approach. Our final model resulted in state-of-the-art performance on both $F_1$-score (0.6681) and recall (0.7700) outperforming all models submitted in SMM4H 2019 and during post-evaluation.  

## Data
All training and evaluation data can be requested from Davy Weissenbacher after signing up for the [CodaLab competition](https://competitions.codalab.org/competitions/20798). The `twitter_data_prep.ipynb` notebook can be used to combine the three raw data files and create train/dev sets with an 80/20 split in the format expected by the model.
 
The pre-trained checkpoints required for BioBERT and ClinicalBERT can be downloaded from their respective GitHub repos ([BioBERT](https://github.com/naver/biobert-pretrained), [ClinicalBERT](https://github.com/EmilyAlsentzer/clinicalBERT))

## Preprocessor
See [/Preprocesser/README.md](https://github.com/aab213/ADR_Detection_with_BERT/tree/master/Preprocesser) for more information on the preprocessing pipeling.

## Running the Model

We ran our models using cTPUs on Google Colab. Our model pipeline is loosely based on Dharmendra Choudhary's [Medium post](https://medium.com/@drcjudelhi/bert-fine-tuning-on-quora-question-pairs-b48277787285), which pulls heavily from the released [BERT github repo](https://github.com/google-research/bert).

Our Colab notebook with our model pipeline is [here](https://colab.research.google.com/drive/1MH3Kl2BU7M7N9oV96IuxFJW01IuEq1pE).

## Ensembling the Results and Submitting

A key component of our approach is our unique ensembling method which combines the output of three models (BERT, BioBERT, and ClinicalBERT) using a max positive predicted probability approach. `model_ensembling.ipynb` is used to create an average prediction for each model type (across 5 runs), as well as create a max ensemble across three different model types. To use, create a subfolder with the prediction probabilities from each model.

To upload results to the [competition platform](https://competitions.codalab.org/competitions/20798#participate-submit_results), the output must be in the format specified in `model_ensembling.ipynb`, saved in a file named `answer.txt`, and zipped up (the zip file can be named anything).
