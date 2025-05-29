import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

# Teste simples da API
try:
    llm = ChatGroq(
        api_key=os.getenv("GROQ_API_KEY"),
        model="llama3-8b-8192",
        temperature=0.1
    )
    
    response = llm.invoke("Olá, como você está?")
    print("✅ API funcionando!")
    print(f"Resposta: {response.content}")
    
except Exception as e:
    print(f"❌ Erro na API: {e}")
    print(f"API Key configurada: {bool(os.getenv('GROQ_API_KEY'))}") 