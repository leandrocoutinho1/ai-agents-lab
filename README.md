# 🤖 Laboratório Agentes de IA

## Visão Geral
**ai-agents-lab** é um experimento educacional e prático voltado para o desenvolvimento de conhecimento em agentes de inteligência artificial, utilizando a biblioteca `CrewAI` e o provedor de linguagem de alto desempenho `Groq`. O objetivo é explorar como agentes autônomos podem colaborar entre si para realizar tarefas complexas com base em conhecimento prévio e entradas personalizadas, com resposta extremamente rápida e eficiente graças ao uso do Groq como backend de inferência.


## 📚 Objetivo

Este projeto simula um mentor de carreira baseado em IA, capaz de analisar uma resposta de um jovem sobre seus interesses profissionais e, com base em uma base de conhecimento, gerar um plano de desenvolvimento personalizado.

## 🚀 Tecnologias Utilizadas

- Python 3.11+
- CrewAI
- Groq

## 🗂️ Estrutura do Projeto

```bash
ai-agents-lab/  
├── agents.py # Definição dos agentes IA  
├── tasks.py # Definição das tarefas que os agentes irão executar  
├── main.py # Script principal que executa o experimento  
├── data/  
│   ├── conhecimento_base.txt # Base de conhecimento usada pelos agentes  
│   └── resposta_joao.txt # Entrada personalizada com resposta do jovem  
├── output/ # Pasta onde os resultados podem ser salvos  
├── .env.example # Variáveis de ambiente
├── requirements.txt
└── README.md
```


## ⚙️ Instalação
1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/ai-agents-lab.git
   ```
2. Acesse o diretório do projeto:
   ```bash
   cd ai-agents-lab
   ```
3. Crie e ative um ambiente virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   .venv\Scripts\activate     # Windows
   ```
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Configuração das Credenciais
Edite o arquivo .env.example, renomeando para .env e preenchendo com sua chave da API da Groq e o modelo LLM a ser usado:

   ```bash
   GROQ_API_KEY=sua-chave-aqui
   MODEL=model-aqui
   ```

## Como Usar
1. Adicione os arquivos de entrada na pasta data/:
    - `conhecimento_base.txt`: conteúdo com base de conhecimento.
    - `resposta_joao.txt`: resposta de um jovem com seus interesses.

2. Execute o projeto:

```sh
python main.py
```

## 💡 Exemplos de uso
Você pode adaptar os arquivos da pasta data/ para testar com diferentes respostas e bases de conhecimento. A saída será exibida no terminal e pode ser facilmente direcionada para um arquivo, se desejar.