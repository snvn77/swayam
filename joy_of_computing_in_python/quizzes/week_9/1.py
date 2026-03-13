# Stylometric and Sentiment Analysis of the Federalist Papers

# Background

# A political science research team is examining the Federalist Papers, a historically significant collection of essays written to support 
# the ratification of the U.S. Constitution. While many essays are clearly attributed to Hamilton, Madison, or Jay, a subset of essays has 
# disputed or shared authorship.

# Instead of relying on historical arguments alone, the team decides to use computational text analysis to study writing patterns across different author groups.

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
  
# Problem Statement

# The team wants to understand whether quantitative textual characteristics , such as word usage patterns and sentiment , can help differentiate 
# between authors and provide insights into disputed essays.

# The task is not to assign authorship directly, but to compare:
# Writing style indicators
# Distributional properties of words
# Emotional tone across author groups 

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Dataset Description

# The dataset is organized by author category:
# Hamilton
# Madison
# Jay
# Disputed
# Shared

# Each category contains a block of text representing essays attributed to that group. These texts are treated as independent corpora. 

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Analytical Approach

# The analysis follows four major stages:

# 1. Text Preprocessing

# Each author’s text is processed to extract meaningful words by:
# Tokenizing text into individual words
# Removing punctuation and non-alphabetic tokens
# Eliminating common English stopwords

# This ensures that comparisons focus on content-bearing words rather than grammatical fillers. 

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 2. Stylometric Analysis Using Word Length

# For every author group:
# The length of each word is computed
# A frequency distribution of word lengths is constructed

# Word length is treated as a stylistic signature, allowing comparison of writing habits without relying on vocabulary meaning.

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 3. Sentiment Analysis

# Each author’s entire text is analyzed using a sentiment model to compute:
# A polarity score ranging from negative to positive

# This helps identify whether different authors (or disputed texts) consistently express different emotional tones, even within formal political writing. 

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 4. Visual Comparison

# Word-length frequency distributions are plotted for all authors on the same figure.
# This visual representation allows analysts to:
# Observe overlaps between authors
# Identify stylistic similarities
# Spot anomalies in disputed or shared texts

import nltk
# nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from textblob import TextBlob
import matplotlib.pyplot as plt

federalist_papers = {
    "Hamilton": "Text data for Hamilton....",
    "Madison": "Text data for Madison....",
    "Jay": "Text data for Jay....",
    "Disputed": "Text data for disputed....",
    "Shared": "Text data for shared...."
}

authors = list(federalist_papers.keys())

tokens = {}
for author, text_data in federalist_papers.items():
    token = [word for word in word_tokenize(text_data) if word.isalpha() and word.lower() not in stopwords.words("english")]

    tokens[author] = token

sentiments = {}
for author, text_data in federalist_papers.items():
    blob = TextBlob(text_data)
    sentiment = blob.sentiment.polarity

    sentiments[author] = sentiment

word_lengths = {}
for author, token in tokens.items():
    length = [len(t) for t in token]
    word_lengths[author] = length

plt.figure(figsize=(12,8))
for author in authors:
    fdist = FreqDist(word_lengths[author])
    fdist.plot(15, cumulative=False)
plt.legend(authors)
plt.show


for author,sentiment in sentiments.items():
    print(f"Sentiment Score for {author}: {sentiment}")
    







# Assume the text for Hamilton contains only the words:
# "Liberty liberty the Constitution"
# After preprocessing, what will be stored in author_tokens["Hamilton"]?
#  ["Liberty", "liberty", "Constitution"]        (Right Answer)
#  ["Liberty", "liberty", "the", "Constitution"]
#  ["liberty", "liberty", "constitution"]
#  ["Liberty", "Constitution"]


# If an author's text contains only stopwords, what happens when plotting their word-length distribution?
#  The program raises a runtime error
#  An empty plot is generated without bars
#  All word lengths are plotted as zero
#  The author is skipped automatically        (Right Answer)


# Which author property is directly visualized in the plotted graphs?
#  Sentiment polarity
#  Token frequency
#  Word-length frequency        (Right Answer)
#  Vocabulary richness


# If the Disputed corpus contains significantly longer average words than others, how would this most likely appear in the plot?
#  Higher bars at smaller word lengths
#  A wider spread with peaks at larger word lengths
#  A flat distribution across all lengths
#  No visible difference from other authors        (Right Answer)


# Suppose TextBlob returns a sentiment polarity of 0.0 for Jay. What does this imply?
#  Jay’s text is emotionally neutral overall        (Right Answer)
#  Jay uses no adjectives
#  Jay’s text contains no positive words
#  Jay’s text failed sentiment analysis


# If the stopword filter were removed from preprocessing, which change would MOST likely occur?
#  Sentiment scores become negative
#  Word-length distributions shift toward shorter lengths
#  Vocabulary size decreases        (Right Answer)
#  Alphabetic filtering stops working


# Why is sentiment analysis performed on the entire text rather than token-level sentiment?
#  TextBlob does not support token sentiment
#  Corpus-level sentiment smooths local noise        (Right Answer)
#  Token sentiment would always be zero
#  Tokens are removed before sentiment analysis


# If the Shared corpus was written by multiple authors, what pattern would MOST likely appear?
#  A sharply peaked word-length distribution
#  Identical sentiment to all authors
#  A broader, less consistent distribution        (Right Answer)
#  No visible plot