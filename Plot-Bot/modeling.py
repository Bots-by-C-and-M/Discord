


# Import for Topic Modeling
import re

"""
Things that need to happen:
    Storing the information in a database
        What do we want to store: user, datetime, msg, channel, link to msg?
    Clean data of msg
    Figure out how many topics need to be determined
    How to display to the mods
"""

# Clean data msgs
def clean_data(msg):
    """
    Accepts a msg from discord and performs several regex substitutions in order to clean the document.

    Parameters
    ----------
    text: string or object

    Returns
    -------
    text: string or object
    """
     # order of operations - apply the expression from top to bottom
    email_regex = "From: \S*@\S*\s?"
    non_alpha = '[^a-zA-Z]'
    multi_white_spaces = "[ ]{2,}"

    msg = re.sub(email_regex, "", msg)
    msg = re.sub(non_alpha, ' ', msg)
    msg = re.sub(multi_white_spaces, " ", msg)

    # apply case normalization
    return msg.lower().lstrip().rstrip()

# Create tokens in the form of lemmas

# Create Term Document Frequency List

# Topic Modeling
def compute_coherence_values(dictionary, corpus, texts, limit, start=2, step=3):
    """
    Compute c_v coherence for various number of topics

    Parameters:
    ----------
    dictionary : Gensim dictionary
    corpus : Gensim corpus
    texts : List of input texts
    limit : Max num of topics

    Returns:
    -------
    model_list : List of LDA topic models
    coherence_values : Coherence values corresponding to the LDA model with respective number of topics
    """
    coherence_values = []
    model_list = []
    for num_topics in range(start, limit, step):
        model = gensim.models.ldamulticore.LdaMulticore(corpus=corpus,
                                                        id2word=id2word,
                                                        num_topics=num_topics,
                                                        chunksize=100,
                                                        passes=10,
                                                        random_state=1234,
                                                        per_word_topics=True,
                                                        workers=2)
        model_list.append(model)
        coherencemodel = CoherenceModel(model=model, texts=texts, dictionary=dictionary, coherence='c_v')
        coherence_values.append(coherencemodel.get_coherence())

    return model_list, coherence_values

# Import for Sentiment Analysis
from nltk.sentiment.vader import SentimentIntensityAnalyzer

