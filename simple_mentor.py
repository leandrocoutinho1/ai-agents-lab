import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

# Carregar dados
with open("data/conhecimento_base.txt", "r", encoding="utf-8") as file:
    conhecimento_base = file.read()

with open("data/resposta_joao.txt", "r", encoding="utf-8") as file:
    resposta_jovem = file.read()

# Configurar LLM diretamente
llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama3-8b-8192",
    temperature=0.3
)

# Prompt direto
prompt = f"""
Você é um mentor de carreira especializado. Crie um plano de desenvolvimento profissional personalizado.

PERFIL DO JOVEM:
{resposta_jovem}

BASE DE CONHECIMENTO:
{conhecimento_base}

INSTRUÇÕES:
- Use as informações da base de conhecimento como referência
- Adapte ao perfil específico do João
- Responda em português
- Seja prático e específico

Crie um plano estruturado com:
1. Análise do perfil
2. Etapas de desenvolvimento (6 meses)
3. Cronograma semanal
4. Recursos recomendados
5. Dicas para primeiro emprego

RESPOSTA:
"""

try:
    print("🚀 Gerando plano com Groq diretamente...")
    response = llm.invoke(prompt)
    
    print("✅ Plano gerado com sucesso!")
    print("="*60)
    print(response.content)
    print("="*60)
    
    # Salvar no arquivo
    os.makedirs("output", exist_ok=True)
    with open("output/plano_desenvolvimento.txt", "w", encoding="utf-8") as f:
        f.write(response.content)
    print("\n📄 Plano salvo em: output/plano_desenvolvimento.txt")
    
except Exception as e:
    print(f"❌ Erro: {e}") 