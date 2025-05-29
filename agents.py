import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

class CareerMentorAgents:
    """Classe para gerenciar o agente mentor usando Groq diretamente"""
    
    def __init__(self):
        load_dotenv()
        self.llm = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model="llama3-8b-8192",
            temperature=0.3,
            max_tokens=2000
        )
    
    def get_llm(self):
        """Retorna o LLM configurado"""
        return self.llm
    
    def get_system_prompt(self):
        """Retorna o prompt do sistema para o mentor"""
        return """Você é um mentor de carreira especializado com 10 anos de experiência 
        ajudando jovens a entrarem na área de tecnologia. Você sempre responde em português 
        e cria planos estruturados, práticos e motivadores."""