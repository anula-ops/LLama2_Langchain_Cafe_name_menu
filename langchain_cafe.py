from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain_community.llms import CTransformers
#Llama2

llm = CTransformers(
        model = "TheBloke/Llama-2-7B-Chat-GGML",
        model_type="llama",
        max_new_tokens = 1024,
        temperature = 0.5
    )

def generate_cafe_name_and_items(country):
    # Chain 1: Restaurant Name
    prompt_template_name = PromptTemplate(
        input_variables=['country'],
        template="I want to open a cafeteria in {country}. Suggest a fancy name for this."
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="cafe_name")

    # Chain 2: Menu Items
    prompt_template_items = PromptTemplate(
        input_variables=['cafe_name'],
        template="""Suggest some menu items for {cafe_name}. Return it as a comma separated string"""
    )

    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=['country'],
        output_variables=['cafe_name', "menu_items"]
    )

    response = chain({'country': country})

    return response

if __name__ == "__main__":
    print(generate_cafe_name_and_items("Italian"))