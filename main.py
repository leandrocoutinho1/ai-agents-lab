import os
from crewai import Crew
from dotenv import load_dotenv
from agents import CareerMentorAgents
from tasks import CareerDevelopmentTask

load_dotenv()

os.makedirs("output", exist_ok=True)

with open("data/conhecimento_base.txt", "r", encoding="utf-8") as file:
    conhecimento_base = file.read()

with open("data/resposta_joao.txt", "r", encoding="utf-8") as file:
    resposta_jovem = file.read()

agent = CareerMentorAgents().career_mentor_agent()
task = CareerDevelopmentTask().generate_study_plan(agent, resposta_jovem, conhecimento_base)

crew = Crew(
    agents=[agent],
    tasks=[task],
    max_rpm=30
)

results = crew.kickoff()

print("\n✅ Plano gerado com sucesso!\n")
print(results)
