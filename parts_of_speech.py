# #!/usr/bin/env python
# # coding: utf-8

import spacy, textacy, re
from textacy import extract

print('POS: done with imports')

# # In[5]:


# get_ipython().system('python -m spacy download en_core_web_sm')


# In[21]:


# TURNS FILE INTO NLP ANALYZABLE OBJECT
def text_to_nlp(file_name):
    with open (file_name, 'r') as file:
        text = file.read()
    #nlp = spacy.load('en_core_web_sm')
    nlp = textacy.make_spacy_doc(text, lang="en_core_web_sm")
    #nlp_text = nlp(text)
    return nlp #_text

print('POS: converted text file to nlp obj')


def tokenize_by_word(nlp_text):
    return list(nlp_text)

# In[20]:


def get_nouns(word_list):
    nouns = filter(lambda token: token.pos_ == 'NOUN', word_list)
    return list(nouns)


# In[19]:


def get_article_noun_phrases(nlp_text):
    noun_phrases = list(nlp_text.noun_chunks)
    article_noun_phrases = []
    for phrase in noun_phrases:
        articles = r"\ba\b|\bA\b|\ban\b|\bAn\b|\bthe\b|\bThe\b"
        if (len(phrase) >= 3) and (re.search(articles, str(phrase))):
            article_noun_phrases.append(phrase)
    return list(article_noun_phrases)


# In[18]:


def get_verb_phrases(nlp_text):
    patterns = [
                [{"POS":"ADV"},{"POS":"ADV"},{"POS":"VERB"}],
                [{"POS":"ADV"},{"POS":"VERB"},{"POS":"ADV"}],
                [{"POS":"ADV"},{"POS":"VERB"},{"POS":"AUX"}],
                [{"POS":"ADV"},{"POS":"VERB"},{"POS":"ADP"}],
                [{"POS":"ADV"},{"POS":"VERB"},{"POS":"NOUN"}],
                [{"POS":"ADV"},{"POS":"VERB"},{"POS":"PROPN"}],
                [{"POS":"ADV"},{"POS":"VERB"},{"POS":"NUM"}],
                [{"POS":"ADV"},{"POS":"VERB"},{"POS":"ADV"}],
                [{"POS":"AUX"},{"POS":"AUX"},{"POS":"VERB"}],
                [{"POS":"AUX"},{"POS":"VERB"},{"POS":"AUX"}],
                [{"POS":"AUX"},{"POS":"ADV"},{"POS":"VERB"}],
                [{"POS":"AUX"},{"POS":"VERB"},{"POS":"ADV"}],
                [{"POS":"AUX"},{"POS":"VERB"},{"POS":"ADP"}],
                [{"POS":"AUX"},{"POS":"VERB"},{"POS":"NOUN"}],
                [{"POS":"AUX"},{"POS":"VERB"},{"POS":"PROPN"}],
                [{"POS":"AUX"},{"POS":"VERB"},{"POS":"NUM"}],
                [{"POS":"VERB"},{"POS":"AUX"},{"POS":"ADV"}],
                [{"POS":"VERB"},{"POS":"ADV"},{"POS":"ADV"}],
                [{"POS":"VERB"},{"POS":"ADV"},{"POS":"ADP"}],
                [{"POS":"VERB"},{"POS":"ADV"},{"POS":"NOUN"}],
                [{"POS":"VERB"},{"POS":"ADV"},{"POS":"PROPN"}],
                [{"POS":"VERB"},{"POS":"ADV"},{"POS":"NUM"}]
               ]
    verb_phrases = extract.matches.token_matches(nlp_text, patterns=patterns)
    return list(verb_phrases)
    

print('POS: ran function defs')

# In[16]:


#loglines = text_to_nlp('loglines.txt')


# In[17]:


#print(get_article_noun_phrases(loglines))
#print (get_verb_phrases(loglines))

