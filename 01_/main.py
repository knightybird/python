from langchain_community.llms import KoboldApiLLM

llm = KoboldApiLLM(endpoint="http://localhost:5001", max_length=80)

response = llm("### Instruction:\nWhat is the first book of the bible?\n### Response:")


