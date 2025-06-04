import os
from crewai import Agent, LLM


class CareerMentorAgents:
    def __init__(self):
        self.llm = LLM(
            model="compound-beta-mini",
            api_key=os.getenv("GROQ_API_KEY")
        )

    def career_mentor_agent(self):
        return Agent(
            role="Mentor de Carreira",
            goal="Criar planos de desenvolvimento profissional para jovens",
            backstory="Você é um mentor experiente que cria planos práticos de carreira em tecnologia.",
            llm=self.llm,
            verbose=True,
            allow_delegation=False
        )