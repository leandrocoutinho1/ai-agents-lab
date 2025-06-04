import os
from crewai import Agent
from langchain_groq import ChatGroq


class CareerMentorAgents:
    def __init__(self):
        self.llm = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model=os.getenv("MODEL")
        )

    def career_mentor_agent(self):
        return Agent(
            role="Mentor de Carreira",
            goal="Auxiliar o jovem a se desenvolver profissionalmente com base em suas respostas.",
            backstory="Você é um mentor de carreira que ajuda os usuários a alcançarem seus objetivos profissionais.",
            verbose=True,
            llm=self.llm,
            max_iter=2,
        )