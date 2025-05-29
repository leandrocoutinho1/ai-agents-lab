import os
from dotenv import load_dotenv
from agents import CareerMentorAgents
from tasks import CareerDevelopmentTask

def main():
    """Versão modular usando as classes"""
    load_dotenv()
    
    # Carregar dados
    try:
        with open("data/conhecimento_base.txt", "r", encoding="utf-8") as file:
            conhecimento_base = file.read()
        print(f"✅ Base de conhecimento carregada")
    except FileNotFoundError:
        conhecimento_base = "Base não encontrada."
        print("❌ Base de conhecimento não encontrada")

    try:
        with open("data/resposta_joao.txt", "r", encoding="utf-8") as file:
            resposta_jovem = file.read()
        print(f"✅ Resposta do jovem carregada")
    except FileNotFoundError:
        resposta_jovem = "Resposta não encontrada."
        print("❌ Resposta do jovem não encontrada")

    # Criar agente e task
    agent = CareerMentorAgents()
    task = CareerDevelopmentTask()
    
    # Gerar prompt e executar
    llm = agent.get_llm()
    prompt = task.create_prompt(resposta_jovem, conhecimento_base)
    
    try:
        print("🚀 Gerando plano de carreira...")
        response = llm.invoke(prompt)
        
        print("✅ Plano gerado com sucesso!")
        print("="*60)
        print(response.content)
        print("="*60)
        
        # Salvar arquivo
        os.makedirs("output", exist_ok=True)
        with open("output/plano_desenvolvimento.txt", "w", encoding="utf-8") as f:
            f.write(response.content)
        print("\n📄 Plano salvo em: output/plano_desenvolvimento.txt")
        
    except Exception as e:
        print(f"❌ Erro: {e}")

if __name__ == "__main__":
    main()
