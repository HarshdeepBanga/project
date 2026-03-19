# pip install langchain_core transformers

from langchain.prompts import PromptTemplate
from langchain.llms import HuggingFacePipeline
from transformers import pipeline

# Create a prompt template
template = "Explain the topic '{topic}' in simple words."
prompt = PromptTemplate(input_variables=["topic"], template=template)

# User input
user_topic = input("Enter a topic: ")
final_prompt = prompt.format(topic=user_topic)

# Load a small local model (CPU-friendly)
pipe = pipeline("text-generation", model="google/flan-t5-small")  # ~80MB model
llm = HuggingFacePipeline(pipeline=pipe)

# Generate text
response = llm(final_prompt)
print("\nGenerated Explanation:\n", response)