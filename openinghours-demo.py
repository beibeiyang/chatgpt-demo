import os
from openai import Completion as Comp
from openai import api_key

# Load your API key from an environment variable or secret management service
api_key = os.getenv("OPENAI_API_KEY")

query1 = """Q: Given the following opening hours for a store, what are the opening hours for Sunday?

Sunday
11:00 AM to 9:00 PM
Monday
10:30 AM to 9:30 PM
Tuesday
10:30 AM to 9:30 PM
Wednesday
10:30 AM to 9:30 PM
Thursday
10:30 AM to 9:30 PM
Friday
10:30 AM to 9:30 PM
Saturday
10:30 AM to 9:30 PM"""

query2 = """Q: Given the following opening hours for a store, what are the opening hours every day in the order from Monday to Sunday?
Sunday
11:00 AM to 9:00 PM
Monday
10:30 AM to 9:30 PM
Tuesday
10:30 AM to 9:30 PM
Wednesday
10:30 AM to 9:30 PM
Thursday
10:30 AM to 9:30 PM
Friday
10:30 AM to 9:30 PM
Saturday
10:30 AM to 9:30 PM"""

# Copied from Lotte websites. See:
# https://www.lwt.co.kr/info/businessHours/BusinessHoursList.do and
# https://www.lwt.co.kr/en/info/businessHours/BusinessHoursList.do
query3 = """Q: Given the following opening hours for a store in Seoul, what are the opening hours for Friday, Saturday and Sunday?
서울스카이
일~목 10:30 ~ 22:00 (매표 및 입장 마감 21:00)
금, 토, 공휴일전일 10:30 ~ 23:00
"""

for q in [query1, query2, query3]:
    print("*" * 10)
    print("Query:" + q)
    response = Comp.create(model="text-davinci-003",
                           prompt=q,
                           max_tokens=200,
                           top_p=1.0,
                           frequency_penalty=0.0,
                           presence_penalty=0.0
                           )
    print(response)
    print(response['choices'][0]["text"])
