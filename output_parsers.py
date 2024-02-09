from langchain.output_parsers import (
    PydanticOutputParser,
)  # validation of inputs against schemas
from pydantic import BaseModel, Field
from typing import List


class PersonIntel(
    BaseModel
):  # objects of class represents the information of the person
    summary: str = Field(description="Summary of the person")
    facts: List[str] = Field(description="Interesting facts about the person")
    topics_of_interest: List[str] = Field(
        description="Topics that may interest the person"
    )
    ice_breakers: List[str] = Field(
        description="Create ice breakers to open a conversation with the person"
    )

    def to_dict(self):  # turn info to dictionary that will be turned to JSON
        return {
            "summary": self.summary,
            "facts": self.facts,
            "topics_of_interest": self.topics_of_interest,
            "ice_breakers": self.ice_breakers,
        }


person_intel_parser: PydanticOutputParser = PydanticOutputParser(
    pydantic_object=PersonIntel
)  # query langchain for json output schema
