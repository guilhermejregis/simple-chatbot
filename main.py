from langchain_openai import ChatOpenAI
from dotenv import load_dotenv



load_dotenv()

llm=ChatOpenAI(model="gpt-4o")


def chat():
    print("**** Chat ****")
    print("If you want to close the chat, type q, quit or exit.")
    while True:
        query=input('Enter your query: ')
        print(f'User: {query}')
        if query.lower() in ['q', 'quit', 'exit']:
            break
        result= llm.invoke(query)
        print(f'AI: {result.content}')


if __name__ == '__main__':
    chat()