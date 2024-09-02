from langchain_ollama import OllamaLLM
from pdf_text import extracted_text
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the question below.

Here is the conversation history: {context}
Question: {question}

Answer:
"""

# Using the Dexter model
model = OllamaLLM(model="Dexter")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model


def handle_conversation():
    context = ""
    print("Ask your queries... Type 'exit' to quit")
    while True:
        # If extracted_text is a list, join its elements into a single string
        user_input = (
            " ".join(extracted_text)
            if isinstance(extracted_text, list)
            else extracted_text
        )

        # Check if user wants to exit the loop
        if user_input.lower() == "exit":
            break

        response = ""

        # Stream the conversation response from the model
        for result in chain.stream({"context": context, "question": user_input}):
            print(result, end="", flush=True)
            response += result

        print()
        # Update the context for the conversation
        context += f"\nUser: {user_input}\nAI: {response}"


if __name__ == "__main__":
    handle_conversation()
