# ChatGPT Demo

# Use cases
This repo includes the following demo:
- ERC demo: Estimate count of store locations
- Summarization demo: Extract keywords from paragraphs of text
- Opening Hours demo: Extract store opening hours from English or Korean texts
- Normalization demo: Normalize addresses in English and Chinese
- Crawl-and-understand: Crawl a HTML webpage and extract information from it

## How to run
- Register a OpenAI developer account at https://platform.openai.com/signup.
- Create an API key in your account: https://platform.openai.com/account/api-keys
- Add your API key in your local profile, for example in Mac:
```shell
export OPENAI_API_KEY=<your-openai-api-key>
```
- Install Python 3
- Run each demo in your command line, for example:
```shell
python3 summarization-demo.py
```
