import spacy
from bs4 import BeautifulSoup as bs
import requests
import spacy.tokens

# Load the spaCy English model
nlp = spacy.load('en_core_web_md')

# Input Website Link from user 
while True:
    input_link = input('Enter BBC News Link: ')
    # Check if the link is a valid BBC News article
    if input_link.startswith('https://www.bbc.com/news/articles/'):
        break
    else:
        print("Please enter a valid BBC News article link.")
        continue

# Get Data from BBC News
response = requests.get(input_link)
soup = bs(response.content, 'html.parser')

# Find all article content divs
txt = soup.find_all('div', {'class' : 'sc-3b6b161a-0 dEGcKf'})

# Extract and join all paragraph texts from the article, with fallbacks when the specific BBC class is not found
if txt:
    text = " ".join(" ".join(p.get_text(strip=True) for p in element.find_all('p')) for element in txt)
else:
    # try article tag
    article = soup.find('article')
    if article:
        text = " ".join(p.get_text(strip=True) for p in article.find_all('p'))
    else:
        # fallback to all paragraphs on the page
        p_tags = soup.find_all('p')
        text = " ".join(p.get_text(strip=True) for p in p_tags)

# Process text with spaCy
doc = nlp(text)

# Create a list of sentences with non-empty text
Sentences = [sent.text.strip() for sent in doc.sents if sent.text.strip()]

# If no sentences extracted, notify and exit
if not Sentences:
    print("No article text could be extracted from the URL; try another BBC article link.")
    raise SystemExit(1)

# Ask the user how many sentences they want to see
while True:
    try:
        lenght = int(input('Enter Number of Sentences to show (Must be Between 5-10): '))
        if lenght < 5  or lenght > 10:
            print('Enter a Valid Number')
            continue
        else: break
    except ValueError:
        print('Enter a Number')

# Ranks Sentences based on word frequency
def sentence_ranks(sentences_list):
    word_freq = {}
    for token in doc:
        if not token.is_stop and not token.is_punct:
            word = token.lemma_.lower()
            word_freq[word] = word_freq.get(word, 0) + 1

    sentence_scores = {}
    for sentence in sentences_list:
        sent_doc = nlp(sentence)
        score = 0
        for token in sent_doc:
            if not token.is_stop and not token.is_punct:
                word = token.lemma_.lower()
                score += word_freq.get(word, 0)
        sentence_scores[sentence] = score

    return sentence_scores

# Get ranked sentences
ordered = sentence_ranks(Sentences)
# Sort sentences by their score in descending order
ordered = sorted(ordered.items(), key=lambda x: x[1], reverse=True)

# Print the top N sentences as requested by the user
print(f'\n\n\n Top {lenght} Sentences: \n')

for i, (sentence, score) in enumerate(ordered[:lenght]):
    print(f'{i+1} || {sentence}\n')