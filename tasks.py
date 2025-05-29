from crewai import Task


class CareerDevelopmentTask:
    """Classe para gerenciar a tarefa de desenvolvimento de carreira"""
    
    @staticmethod
    def create_prompt(resposta_jovem, conhecimento_base):
        """Cria o prompt para geração do plano"""
        return f"""
Você é um mentor de carreira especializado. Crie um plano de desenvolvimento profissional personalizado.

PERFIL DO JOVEM:
{resposta_jovem}

BASE DE CONHECIMENTO PARA ORIENTAÇÃO:
{conhecimento_base}

INSTRUÇÕES:
- Use as informações da base de conhecimento como referência
- Adapte ao perfil específico do João
- Responda APENAS em português
- Seja prático e específico
- Inclua recursos mencionados na base de conhecimento quando relevantes

FORMATO DA RESPOSTA:

# Plano de Desenvolvimento Profissional - João Silva

## Análise do Perfil
[Análise baseada no perfil do João]

## Etapa 1: Fundamentos (Meses 1-2)
[Baseado na base de conhecimento sobre programação]

## Etapa 2: Desenvolvimento Prático (Meses 3-4)
[Projetos práticos sugeridos]

## Etapa 3: Preparação para o Mercado (Meses 5-6)
[Preparação para primeiro emprego]

## Cronograma Semanal Detalhado
[Cronograma baseado no tempo disponível do João]

## Recursos Recomendados
[Recursos específicos da base de conhecimento]

## Desenvolvimento de Soft Skills
[Habilidades interpessoais importantes]

## Próximos Passos para o Primeiro Emprego
[Estratégias para conseguir o primeiro emprego]

RESPOSTA:
"""

    def generate_study_plan(self, agent, resposta_jovem, conhecimento_base):
        return Task(
            description=self.create_prompt(resposta_jovem, conhecimento_base),
            agent=agent,
            expected_output="Plano estruturado em português",
            output_file="output/plano_desenvolvimento.txt"
        )