import os
from dotenv import load_dotenv

load_dotenv()

def create_career_plan():
    """Cria plano de carreira usando API Groq diretamente"""
    
    print("🚀 Iniciando geração do plano de carreira...")
    
    # Verificar API key
    groq_key = os.getenv("GROQ_API_KEY")
    if not groq_key:
        print("❌ GROQ_API_KEY não encontrada no arquivo .env")
        print("Crie um arquivo .env com: GROQ_API_KEY=sua_chave_aqui")
        return False

    print(f"✅ API Key encontrada: {groq_key[:10]}...")
    
    os.makedirs("output", exist_ok=True)

    # Ler arquivos de dados
    try:
        with open("data/conhecimento_base.txt", "r", encoding="utf-8") as file:
            conhecimento_base = file.read()
        print(f"✅ Base de conhecimento carregada: {len(conhecimento_base)} caracteres")
    except FileNotFoundError:
        print("❌ Arquivo data/conhecimento_base.txt não encontrado")
        return False

    try:
        with open("data/resposta_joao.txt", "r", encoding="utf-8") as file:
            resposta_jovem = file.read()
        print(f"✅ Perfil do jovem carregado: {len(resposta_jovem)} caracteres")
    except FileNotFoundError:
        print("❌ Arquivo data/resposta_joao.txt não encontrado")
        return False

    # Criar plano usando API Groq
    try:
        from groq import Groq
        client = Groq(api_key=groq_key)
        
        print("\n📝 Gerando plano personalizado...")
        
        prompt = f"""Você é um mentor de carreira experiente. Crie um plano de desenvolvimento profissional detalhado e personalizado para João Silva.

PERFIL DO JOVEM:
{resposta_jovem}

BASE DE CONHECIMENTO PARA ORIENTAÇÃO:
{conhecimento_base}

INSTRUÇÕES:
- Analise cuidadosamente o perfil do João
- Use as diretrizes da base de conhecimento
- Crie um plano prático e motivador
- Seja específico com recursos e cronogramas
- Responda em português brasileiro

ESTRUTURA OBRIGATÓRIA:

# Plano de Desenvolvimento Profissional - João Silva

## Análise do Perfil
[Análise detalhada baseada nas informações do João]

## Etapa 1: Fundamentos (Meses 1-2)
[Baseado na base de conhecimento sobre lógica e linguagens]

## Etapa 2: Desenvolvimento Prático (Meses 3-4)
[Projetos e práticas específicas]

## Etapa 3: Preparação para o Mercado (Meses 5-6)
[Estratégias para primeiro emprego]

## Cronograma Semanal Detalhado
[Distribuição específica de atividades]

## Recursos Recomendados
[Plataformas, cursos e materiais específicos]

## Desenvolvimento de Soft Skills
[Habilidades interpessoais importantes]

## Próximos Passos para o Primeiro Emprego
[Estratégias práticas de busca de emprego]

## Dicas Motivacionais
[Conselhos para manter a motivação]

Seja detalhado, específico e prático em cada seção."""

        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system", 
                    "content": "Você é um mentor de carreira experiente especializado em tecnologia. Crie planos detalhados, práticos e motivadores para jovens que querem entrar na área tech."
                },
                {
                    "role": "user", 
                    "content": prompt
                }
            ],
            model="llama3-8b-8192",
            max_tokens=4000,
            temperature=0.3
        )
        
        content = response.choices[0].message.content
        
        # Salvar arquivo
        output_file = "output/plano_desenvolvimento.txt"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content)
        
        print(f"\n✅ Plano criado com sucesso!")
        print(f"📄 Arquivo salvo: {output_file}")
        print(f"📏 Tamanho: {len(content)} caracteres")
        
        # Mostrar prévia do conteúdo
        print("\n" + "="*60)
        print("📋 PRÉVIA DO PLANO GERADO:")
        print("="*60)
        preview = content[:800] + "..." if len(content) > 800 else content
        print(preview)
        print("="*60)
        
        return True
        
    except Exception as e:
        print(f"❌ Erro ao gerar plano: {e}")
        return False

def main():
    """Função principal"""
    print("🎯 Gerador de Plano de Desenvolvimento Profissional")
    print("=" * 50)
    
    success = create_career_plan()
    
    if success:
        print("\n🎉 Processo concluído com sucesso!")
        print("📁 Verifique o arquivo em: output/plano_desenvolvimento.txt")
    else:
        print("\n❌ Falha na geração do plano. Verifique os erros acima.")

if __name__ == "__main__":
    main()
