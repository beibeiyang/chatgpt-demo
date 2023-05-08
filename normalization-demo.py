import os
from openai import Completion as Comp
from openai import api_key

# Load your API key from an environment variable or secret management service
api_key = os.getenv("OPENAI_API_KEY")

queries = ["Normalize the address for me in Chinese and add the postal code at the end: " +
           "上海市杨浦区邯郸路600号4楼小肥羊火锅餐厅（五角场万达广场第一食品四楼）",

           "Give me the restaurant name, floor level, street name and number, city, and postal code in " +
           "上海市杨浦区邯郸路600号4楼小肥羊火锅餐厅（五角场万达广场第一食品四楼）",

           "Guess the postal code for 上海市杨浦区邯郸路600号4楼小肥羊火锅餐厅（五角场万达广场第一食品四楼）",

           "Q: Extract the building name, street name and number, city, province, postal code, " +
           "and country from the address: " +
           "Novotel Antwerp North, Luithagen-Haven 6, 2030 Antwerpen, Belgium"]

for q in queries:
    print("*"*40, "\n", q)
    response = Comp.create(model="text-davinci-003",
                           prompt=q,
                           max_tokens=200,
                           top_p=1.0,
                           frequency_penalty=0.0,
                           presence_penalty=0.0
                           )
    # print(response)
    print(response['choices'][0]["text"])
