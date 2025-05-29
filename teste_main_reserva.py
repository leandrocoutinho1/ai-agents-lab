import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

def generate_career_plan():
    """Gera plano de carreira usando Groq diretamente"""
    
    # Carregar dados
    try:
        with open("data/conhecimento_base.txt", "r", encoding="utf-8") as file:
            conhecimento_base = file.read()
        print(f"✅ Base de conhecimento carregada: {len(conhecimento_base)} caracteres")
    except FileNotFoundError:
        conhecimento_base = "Base de conhecimento não encontrada."
        print("❌ Arquivo conhecimento_base.txt não encontrado")

    try:
        with open("data/resposta_joao.txt", "r", encoding="utf-8") as file:
            resposta_jovem = file.read()
        print(f"✅ Resposta do jovem carregada: {len(resposta_jovem)} caracteres")
    except FileNotFoundError:
        resposta_jovem = "Resposta não encontrada."
        print("❌ Arquivo resposta_joao.txt não encontrado")

    # Configurar LLM
    llm = ChatGroq(
        api_key=os.getenv("GROQ_API_KEY"),
        model="llama3-8b-8192",
        temperature=0.3,
        max_tokens=2000
    )

    # Prompt estruturado
    prompt = f"""
Você é um mentor de carreira especializado com 10 anos de experiência ajudando jovens a entrarem na área de tecnologia.

PERFIL DO JOVEM:
{resposta_jovem}

BASE DE CONHECIMENTO PARA ORIENTAÇÃO:
{conhecimento_base}

TAREFA:
Crie um plano de desenvolvimento profissional personalizado para João Silva, usando as diretrizes da base de conhecimento e adaptando ao perfil específico dele.

INSTRUÇÕES OBRIGATÓRIAS:
- Use as informações da base de conhecimento como referência
- Adapte as sugestões ao perfil específico do João
- Responda APENAS em português
- Seja prático e específico
- Inclua recursos mencionados na base de conhecimento quando relevantes

FORMATO EXATO DA RESPOSTA:

# Plano de Desenvolvimento Profissional - João Silva

## Análise do Perfil
[Breve análise baseada nas informações do João]

## Etapa 1: Fundamentos (Meses 1-2)
[Baseado na base de conhecimento sobre lógica de programação e linguagens]

## Etapa 2: Desenvolvimento Prático (Meses 3-4)
[Incluir projetos sugeridos na base de conhecimento]

## Etapa 3: Preparação para o Mercado (Meses 5-6)
[Usar dicas da base sobre primeiro emprego e networking]

## Cronograma Semanal Detalhado
[Baseado nas dicas de estudo da base de conhecimento]

## Recursos Recomendados
[Incluir plataformas mencionadas na base: YouTube, Alura, Coursera, etc.]

## Desenvolvimento de Soft Skills
[Baseado nas orientações sobre comunicação da base]

## Próximos Passos para o Primeiro Emprego
[Usar as dicas sobre estágios e portfólio da base]

RESPOSTA:
"""

    return llm, prompt

def main():
    """Função principal"""
    print("🚀 Iniciando geração do plano de carreira...")
    
    # Criar diretório de output
    os.makedirs("output", exist_ok=True)
    
    try:
        # Gerar plano
        llm, prompt = generate_career_plan()
        
        print("\n📝 Gerando plano personalizado...")
        response = llm.invoke(prompt)
        
        print("\n✅ Plano gerado com sucesso!")
        print("="*80)
        print(response.content)
        print("="*80)
        
        # Salvar no arquivo
        output_file = "output/plano_desenvolvimento.txt"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(response.content)
        
        print(f"\n📄 Plano salvo em: {output_file}")
        print(f"📊 Tamanho do plano: {len(response.content)} caracteres")
        
    except Exception as e:
        print(f"❌ Erro detalhado: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
