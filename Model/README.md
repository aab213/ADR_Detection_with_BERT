# Model

## Data
 All training and evaluation data can be requested from Davy Weissenbacher after signing up for the [CodaLab competition](https://competitions.codalab.org/competitions/20798). The `twitter_data_prep.ipynb` notebook can be used to combine the three raw data files and create train/dev sets with an 80/20 split in the format expected by the model.

## Model Notebooks

We ran our models using cTPUs on Google Colab. Our model pipeline is loosely based on Dharmendra Choudhary's [Medium post] (https://medium.com/@drcjudelhi/bert-fine-tuning-on-quora-question-pairs-b48277787285), which pulls heavily from the released [BERT github repo](https://github.com/google-research/bert).

[BERT<sub>LARGE</sub> Colab Notebook](https://colab.research.google.com/drive/1Gludb-LKPxi9ETggjleVDQOBetqaDTDq)

[BioBERT Colab Notebook](https://colab.research.google.com/drive/1z6Xs5zpAWni3bTsyYibJ1xT5oyyf6fxT)

[Bio + Clinical BERT Colab Notebook](https://colab.research.google.com/drive/18vw72Ebm7SNuP_GdMJI690VJ9zOgoutR)
