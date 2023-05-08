import os
from openai import Completion as Comp
from openai import api_key

# Load your API key from an environment variable or secret management service
api_key = os.getenv("OPENAI_API_KEY")

# query = "Tell me a story of the Panda Express founders within 200 words"
# query = "Generate a summary of the Panda Express chain within 100 words."

# # Copied from https://www.thekrogerco.com/about-kroger/our-business/
query = """Extract keywords from this text:
Headquartered in Cincinnati, Ohio, The Kroger Co. is one of the largest retailers in the United States based on annual sales. The information below is current as of November 30, 2020.

We operate 2,750 grocery retail stores under a variety of banner names. Our formats include supermarkets, seamless digital shopping options, price-impact warehouse stores, and multi-department stores, which are similar to supercenters, but offer an expanded variety of national brand apparel and general merchandise. State-specific facts can be seen here.
170 fine jewelry stores under names like Fred Meyer Jewelers and Littman Jewelers. This is a high-margin business with good cash flow.
Kroger is the only major U.S. supermarket company to operate an economical three-tier distribution system.
Kroger also operates 35 food production or manufacturing facilities producing high quality private-label products that provide value for customers and enhanced margins for Kroger.
Kroger operates 1,585 supermarket fuel centers, which are a natural addition to our one-stop-shopping strategy.
Kroger’s 2,256 pharmacies, located in our combination food and drug stores, provide high quality services at everyday low prices.
"""

response = Comp.create(model="text-davinci-003",
                       prompt=query,
                       max_tokens=200,
                       top_p=1.0,
                       frequency_penalty=0.0,
                       presence_penalty=0.0
                       )

print(response)
print(response['choices'][0]["text"])
