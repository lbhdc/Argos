import unittest
import nlp


nlp_model, ids, vectors = nlp.load_model("en_core_web_md")
doc = nlp_model("""
    How about you give me that $20 you owe me?
""".strip())


class NlpTests(unittest.TestCase):
    
    def test_entities(self):
        self.assertEqual([("20", "MONEY")], nlp.entities(doc))

    def test_noun_chunks(self):
        # TODO: not testing much
        self.assertEqual(len(doc), len(nlp.parts_of_speech(doc)))

    def test_tokenize(self):
        # TODO: not testing much
        self.assertEqual(len(doc), len(nlp.tokenize(nlp_model, doc)))
        
    def test_topic(self):
        tokens = nlp.tokenize(nlp_model, doc)
        vector = nlp.topic_vector(nlp_model, tokens)
        topic = nlp.topic_string(nlp_model, ids, vectors, vector)
        self.assertEqual("you", topic)

if __name__ == '__main__':
    unittest.main()