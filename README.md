# Ice Breaker

Ice Breaker is a functioning fullstack application based on generative AI. It performs web crawling to get a person's linkedin profile and leverages the langchain library to generate interesting ice breakers based on the person's history. 
It incorporates the use of LangChain ReAct (Reasoning Action) agents to faciliate the effective return of the linkedin profile URL as well as cleaning of tokens in the resultant information in JSON format. Finally, the output of the LLM is parsed using LangChain's output praser to get the four essential components from the JSON file which is summary, two interesting facts, topics of interest and two generated ice breakers. The frontend is designed using static HTML/CSS while the backend is created through Flask.

## Screenshots

![image](https://github.com/adityabnair/ice_breaker/assets/64246274/e25c2b6f-4111-4e24-8407-82fceed6be34)
![image](https://github.com/adityabnair/ice_breaker/assets/64246274/5b7d0abf-3d99-42c4-9677-d0201adaeac2)
![image](https://github.com/adityabnair/ice_breaker/assets/64246274/84e37355-cff1-4b1f-aad0-b21955f0c131)



## Main Prerequisites

1. Python 3.10
2. Access to OpenAI's API credits for usage of gpt-3.5 
3. Access to Proxycurl's paid API for crawling to get the thhe correct LinkedIn profile
4. Access to SerpAPI's paid credits to facilitate the scraping of information from the LinkedIn profile page


### Running

1. Use pipenv to install python libraries from requirements.txt
2. Add environment variables in a .env file to hold the keys
3. Run app.py
4. Search for name (name can be entered with a tag like an organization's name to differentitate between similar names)


## Acknowledgments

Thanks to @emarco177 for the langchain development course
