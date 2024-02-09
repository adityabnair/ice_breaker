import os
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from third_parties.linkedin import scrape_linkedin_profile
from output_parsers import person_intel_parser, PersonIntel
from typing import Tuple

# from third_parties.twitter import scrape_user_tweets

load_dotenv()  # take environment variables from .env.


def ice_break(
    name: str,
) -> Tuple[
    PersonIntel, str
]:  # returning the PersonIntel object created in the output_parser file
    linkedin_profile_url = linkedin_lookup_agent(name=name)

    summary_template = """
    given the LinkedIn information {information} about a person from I want you to create:
    1. a short summary
    2. two interesting facts about them 
    3. A topic that may interest them
    4. 2 creative Ice breakers to open a conversation with them
            \n{format_instructions}

    """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables={
            "format_instructions": person_intel_parser.get_format_instructions()  # schema extracted and plugged in to temmplate
        },
    )
    llm = ChatOpenAI(temperature=1, model_name="gpt-3.5-turbo")
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url)

    result = chain.run(information=linkedin_data)
    print(result)
    return person_intel_parser.parse(result), linkedin_data.get("profile_pic_url")
    # print(linkedin_data)
    # scrape_user_tweets(username = "@Shreemauli7" , num_tweets = 20)


if __name__ == "__main__":
    print("Hello LangChain!")
    ice_break(name="Harrison Chase")
