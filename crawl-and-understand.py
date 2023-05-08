from bs4 import BeautifulSoup
from bs4.element import Comment
from urllib.request import Request, urlopen
import os
from openai import Completion as Comp
from openai import api_key

# Getting input for webiste from user
url = "https://investor.costco.com/company-profile/default.aspx"
print(" This is the website link to crawl", url)


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    return u" ".join(t.strip() for t in visible_texts)


req = Request(url=url, headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(req).read()
text = text_from_html(html)
print(text)


# Load your API key from an environment variable or secret management service
api_key = os.getenv("OPENAI_API_KEY")

queries = ["""Based on the following text, tell me the number of total Costco warehouses out there: """ + text,
           """Based on the following text, tell me the number of Costco warehouses in GB are out there: """ + text]
for q in queries:
    print("*"*40, "\n", q)
    response = Comp.create(model="text-davinci-003",
                           prompt=q,
                           max_tokens=200,
                           top_p=1.0,
                           frequency_penalty=0.0,
                           presence_penalty=0.0
                           )
    #print(response)
    print(response['choices'][0]["text"])

