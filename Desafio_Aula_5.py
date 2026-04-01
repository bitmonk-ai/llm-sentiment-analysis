# Desafio
# 1. Carregar um arquivo .csv com feedback de clientes (review.csv)
# 2. Usar uma LLM para classificar o sentimento de cada feedback. (Positivo, Negativo, Neutro)
# 3. Adicionar uma nova coluna com a classificação ao DataFrame.
import os
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv

df = pd.read_csv("C:/Estudos_phython_AI/reviews.csv")

review_text = df["reviewText"]

def verificandoreviews(listareviews):
    sentimento = []
    load_dotenv()
    client = OpenAI()

    for reviewtext in listareviews:

        resposta = client.responses.create(
            model="gpt-5.4-nano-2026-03-17",
            input=f"""No arquivo texto, indique somente a sentimento se Positive, Negative ou Neutral,
            sem a necessidade de explicar ou enfeitar a resposta.
            
            Reviews
            {reviewtext}"""
        )
        sentimento.append(resposta.output_text)
    return sentimento

df["Sentiment"] = verificandoreviews(review_text)
df.to_csv("review_+_sentiment_column.csv", index=False)
print(df.head())
