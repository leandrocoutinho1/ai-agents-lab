from crewai import Task


class CareerDevelopmentTask:
    def generate_study_plan(self, agent, resposta_jovem, conhecimento_base):
        return Task(
            description=f"""
                Com base nas respostas do jovem e no conteúdo de referência, gere um plano de desenvolvimento profissional personalizado.

                Resposta do jovem:
                ------------------
                {resposta_jovem}

                Base de conhecimento:
                ---------------------
                {conhecimento_base}

                Instruções:
                - Analise as dificuldades, interesses e metas do jovem.
                - A partir da base de conhecimento, sugira uma rota de estudo personalizada.
                - Destaque as principais soft e hard skills a desenvolver.
                - Seja claro, objetivo e encorajador na resposta.
            """,
            agent=agent,
            expected_output="Plano de desenvolvimento profissional personalizado.",
            output_file="output/plano_desenvolvimento.txt",
        )