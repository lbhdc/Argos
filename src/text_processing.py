import lib.nlp

(nlp, ids, vectors) = lib.nlp.load_model("en_core_web_md")

tokenize = lambda text: lib.nlp.tokenize(nlp, text)
topic_vector = lambda tokens: lib.nlp.topic_vector(nlp, tokens)
topic_string = lambda topic_vec: lib.nlp.topic_string(nlp, ids, vectors, topic_vec)
topic = lambda doc: topic_string(topic_vector(tokenize(doc)))

doc = nlp(u"""
    Explosions will continually shake the earth
    Radiated robot men will stalk each other
    The rich and the chosen will watch from space platforms
    Dante's Inferno will be made to look like a children's playground
    The sun will not be seen and it will always be night
    Trees will die
    """.strip())

print(nlp(topic(doc)).vector)