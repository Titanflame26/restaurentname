from langchain_cohere.llms import Cohere
from langchain_core.prompts import PromptTemplate
from key import COHERE_API_KEY

api_key = COHERE_API_KEY
llm = Cohere(cohere_api_key = api_key )
#name = llm.invoke("I want to open a restaurant for Indian food. Suggest a fency name for this.")
#print(name)

prompt_template_name = PromptTemplate(
    input_variables =['cuisine'],
    template = "I want to open a restaurant for {cuisine} food. Suggest a fency name for this."
)
p = prompt_template_name.format(cuisine="Indian")
print(llm.invoke(prompt_template_name.format(cuisine="Russian")))
#print(llm.invoke(p))
#chain = prompt_template_name | llm