import sys
print(sys.version)

from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

from langchain.llms import CTransformers

# Model ID on HF
model_id = "TheBloke/guanaco-7B-GGUF"

# Initialize ctransformers LLM
llm = CTransformers(
    model=model_id,
    model_file="Guanaco-7B.Q4_K_M.gguf",  
    verbose=True
)

# Memory
memory = ConversationBufferMemory()

# Conversation chain
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

# Chat loop
print("Chatbot ready! Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = conversation.run(user_input)
    print("Bot:", response)

