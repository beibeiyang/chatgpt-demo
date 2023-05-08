import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(model="text-davinci-003",
                                    prompt="Q: How many Tesla Superchargers are there in Switzerland?",
                                    temperature=0,
                                    max_tokens=60,
                                    top_p=1.0,
                                    frequency_penalty=0.0,
                                    presence_penalty=0.0
                                    )

print(response)
