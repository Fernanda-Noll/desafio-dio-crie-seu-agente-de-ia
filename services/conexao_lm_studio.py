from openai import OpenAI

# -> CONEXÃO LM STUDIO
def conexao_com_llama(script, contexto, pergunta):
    prompt = f"""
    {script}

    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {pergunta}"""

    client = OpenAI(
        base_url="http://127.0.0.1:1234/v1",
        api_key="lm-studio"
    )

    response = client.chat.completions.create(
        model="meta-llama-3.1-8b-instruct",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content
