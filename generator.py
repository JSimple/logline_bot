#!/usr/bin/env python
# coding: utf-8
# In[3]:
import spacy, re, random, torch
from textacy import extract
from parts_of_speech import text_to_nlp, get_article_noun_phrases, get_verb_phrases
from transformers import pipeline

# In[7]:

# for prompt gen
def get_genre():
    genres = [
            "Action",
            "Adventure",
            "Animation",
            "Biography",
            "Comedy",
            "Crime",
            "Documentary",
            "Drama",
            "Family",
            "Fantasy",
            "History",
            "Horror",
            "Musical",
            "Mystery",
            "Romance",
            "Sci-Fi",
            "Sports",
            "Thriller",
            "War",
            "Western"
    ]
    return '-'.join(random.choices(genres, k=2))

#prompt gen
def generate_prompt(source):
    nlp = text_to_nlp(source)
    genre = get_genre()
    noun_phrase1 = random.choice(get_article_noun_phrases(nlp))
    noun_phrase2 = random.choice(get_article_noun_phrases(nlp))
    verb_phrase = random.choice(get_verb_phrases(nlp))
    prompt = 'Logline for a/n {g} movie about {n1}: {n2}'.format(
    g=genre, n1=noun_phrase1, n2=noun_phrase2)
    return str(prompt)

# logline gen
generator = pipeline('text-generation', model='KrishParikh/gpt2_imdb_movie_plots')

def generate_logline():
    prompt = generate_prompt('loglines.txt')
    colon_idx = prompt.index(':')
    generated = generator(prompt, max_length = 100, do_sample = True, temperature = 1.25)
    logline = generated[0]['generated_text'][colon_idx+2:]
    return logline.capitalize()

def generate_title(logline):
    prompt = 'This is a movie\'s plot:\n"{l}"\nThis is the movie\'s short and snappy title that uses 1 - 4 words from the plot:"'.format(
    l=logline)
    generated = generator(prompt, max_length = 100, do_sample = True, temperature = .6)
    title = generated[0]['generated_text'].replace(prompt,'').replace('\"','').replace('.','')
    return title

# In[104]:


#title = generate_title(logline)
# for i in range (20):
#     logline = generate_logline()
#     print(str(i) + "." + logline)
