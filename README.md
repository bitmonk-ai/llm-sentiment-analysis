# LLM Sentiment Analysis

This project performs sentiment analysis on customer reviews using Python, pandas and a Large Language Model (LLM).

Each review is classified as:
- Positive
- Negative
- Neutral


## Technologies

- Python
- pandas
- OpenAI API (LLM)
- CSV


## How it works

The script reads a CSV file containing reviews, sends each review to the LLM and receives a sentiment classification.

The result is added as a new column in the DataFrame.


## How to run

1. Install dependencies:

pip install -r requirements.txt

2. Create a .env file with your API key:

OPENAI_API_KEY=your_api_key_here

3. Run the script:

python Desafio_Aula_5.py


## Notes

- The output CSV is generated automatically
- The .env file is not included for security reasons

## Context

This project was developed as part of a challenge from the Alura course "Python: Inteligência Artificial Aplicada", applying the concepts to real data using LLM-based sentiment classification.


## Author

Eduardo Rabelo (bitmonk-ai)  
https://github.com/bitmonk-ai
