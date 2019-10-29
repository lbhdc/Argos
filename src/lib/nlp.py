import numpy as np
import spacy
from scipy.spatial import distance


# load_model takes the name of a pre-trained spacy model. It returns the model,
# the ids (an integer key), and the vectors. The ids and vectors are used to
# transition between text and vectors. 
# 
# Pretrained models are documented: https://spacy.io/models
# to install models `$python -m spacy <model_name>`
# larger models improve accuracy.
def load_model(name):
    nlp = spacy.load(name)
    ids = [x for x in nlp.vocab.vectors.keys()]
    vectors = [nlp.vocab.vectors[x] for x in ids]
    return (nlp, ids, vectors)

# entities takes a spacy doc and returns a list of tuples of the entity text
# and its part of speech label.
def entities(doc):
    return [(e.text, e.label_) for e in doc.ents]

# noun_chunks takes a spacy doc and returns a list of tuples of the noun chunk
# text and its part of speech label.
def noun_chunks(doc):
    return [(c.text, c.label_) for c in doc.noun_chunks]

# part_of_speech takes a spacy dock and returns a list of tuples of the text
# and its part of speech.
def parts_of_speech(doc):
    return [(w.text, w.pos_) for w in doc]

# tokenizer takes the language model, and the corpus and returns a list of
# tokens.
def tokenize(nlp, corpus):
    tokenizer = nlp.Defaults.create_tokenizer(nlp)
    tokens = [word for word in list(tokenizer(str(corpus)))]
    return tokens

# topic_vector takes a language model, and returns the average vector for all
# all of the tokens. 
def topic_vector(nlp, tokens):
    token_vectors = [nlp.vocab[str(word)].vector for word in tokens]
    average_vector = np.mean(token_vectors, axis=0)
    return average_vector

# topic_string takes a language model, its keys, its vectors (full output of
# load_model), and the target vector. It returns the word closest to the 
# topic vector.
def topic_string(nlp, ids, vectors, topic_vec):
    closest_index = distance.cdist([topic_vec], vectors).argmin()
    word_id = ids[closest_index]
    output_word = nlp.vocab[word_id].text
    return output_word