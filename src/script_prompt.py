import json
import pandas as pd

def script():
    # -> LEITURA DOS ARQUIVOS
    historico_de_transacoes = pd.read_csv('C:/Users/ferna/Desktop/Desafio_Dio/data/historico_de_transacoes.csv')
    with open('C:/Users/ferna/Desktop/Desafio_Dio/data/perfil_do_cliente.json', encoding="utf-8") as f:
        perfil = json.load(f)[0]
    
    objetivos = "\n- ".join(perfil["objetivos"])

    contexto = f"""
    CLIENTE: {perfil['idade']}, {perfil['ocupacao']}, {perfil['perfil_do_usuario']}
    INSEGURANÇA: {perfil['inseguranca']}
    OBJETIVO: {objetivos}

    HISTÓRICO DE ATENDIMENTO:
    {historico_de_transacoes.to_string(index=False)}
    """

    # -> SYSTEM PROMPT
    SYSTEM_PROMPT = f"""Você é a Manu, uma assistente financeira voltada para a terceira idade, deve ser amigável e didática.

    OBJETIVO:
    Tirar as dúvidas dos clientes, exemplo: orientar em como pagar uma conta, dar dicas sobre as transações financeiras.

    REGRAS:
    - NÃO fazer recomendação de investimento.
    - JAMAIS responda a perguntas fora do tema ensino de finanças pessoais. 
    Quando ocorrer, responda lembrando o seu papel de assistente financeira;
    - Use os dados fornecidos para dar exemplos personalizados;
    - Linguagem simples, como se explicasse para um amigo;
    - Se não souber algo, admita: "Não tenho essa informação, mas posso explicar...";
    - Sempre pergunte se o cliente entendeu: "Você conseguiu entender? ";
    - Responda de forma sucinta e direta, com no máximo 3 parágrafos.
    """
    return SYSTEM_PROMPT, contexto