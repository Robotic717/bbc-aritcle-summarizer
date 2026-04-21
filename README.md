
# Natural Language Processing

## Description
This Python script allows you to extract and summarize content from any valid **BBC News article link**.  
It uses **BeautifulSoup** to scrape the article content and **spaCy** for natural language processing to generate a ranked summary of the most important sentences **without stop words**.

---

## Features

- Takes a valid BBC News article URL as input.
- Scrapes and extracts the main text content.
- Uses spaCy’s NLP pipeline to remove stop words.
- Reconstructs sentences without stop words.
- Scores and ranks sentences based on word frequency.
- Allows you to display **5 to 10** top-ranked sentences as a quick summary.

---

## Requirements

Make sure you have the following Python libraries installed:

- [spaCy](https://spacy.io/)  
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)  
- [requests](https://docs.python-requests.org/)

Install them using:

```bash
pip install spacy beautifulsoup4 requests
```
---


## How it Works

1. **Input:**  
   This script asks the user to provide a BBC news article link. if the link does not start with `https://www.bbc.com/news/articles/`, it asks the user to enter a correct link.


2. **Preprocessing:**  
   - Loads the `en_core_web_md` spaCy language model.
   - Removes stop words from the extracted text.
   - Reconstructs the text into clean sentences without stop words.

3. **Ranking:**  
   Each sentence is scored based on the frequency of its words. Sentences containing frequently occurring words are ranked higher.

4. **Output:**  
   - Prompts the user to specify how many sentences (between 5 and 10) they want to see.
   - Prints the top-ranked sentences as a summary.

---

## Example Output

If BBC news link is `https://www.bbc.com/news/articles/c20nqdl5ydjo` and number of lines is 7, the output will look like this:
```bash
 Top 7 Sentences: 

1: Congress passed law forcing TikTok sale April year, lawmakers citing fears app parent company hand user data Chinese government, TikTok denied.
2: previous deal sell TikTok American buyer fell apart April, White House clashed China Trump tariffs.
3:   President Donald Trump said buyer TikTok, video- sharing app banned amid claims posed national security risk.
4: law supposed effect 19 January, Trump repeatedly delayed enforcement executive actions, moves drawn criticism overruling congressional lawmakers.
5: sale need approval Chinese government, Trump told Fox thought President Xi Jinping" probably".
6: month Trump delayed time enforcement law mandating TikTok sale.
7: Trump criticised app term, came factor 2024 election win supports continued use.
```
