# imports
import os
os.system("pip install bertopic")

from bertopic import BERTopic
from sklearn.datasets import fetch_20newsgroups
from sentence_transformers import SentenceTransformer
from sklearn.datasets import fetch_20newsgroups

# get data
docs = fetch_20newsgroups(subset='all',  remove=('headers', 'footers', 'quotes'))['data']

# add sentence-transformer
sentence_model = SentenceTransformer("all-MiniLM-L6-v2")

# train model
topic_model = BERTopic(embedding_model=sentence_model)
topics, probs = topic_model.fit_transform(docs)

# get infos
topic_model.get_topic_info()