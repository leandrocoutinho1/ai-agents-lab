from crewai import Task

class CareerDevelopmentTask:
    def generate_study_plan(self, agent, resposta_jovem, conhecimento_base):
        return Task(
            description=f"""
Crie um plano de desenvolvimento profissional para o jovem baseado nas informações:

PERFIL: {resposta_jovem[:500]}...

BASE DE CONHECIMENTO: {conhecimento_base[:500]}...

Crie um plano estruturado em português com:
- Análise do perfil
- 3 etapas de desenvolvimento
- Recursos recomendados
- Cronograma

Responda diretamente com o plano, sem incluir pensamentos ou processos.
            """,
            agent=agent,
            expected_output="Plano de desenvolvimento profissional estruturado em português"
        )