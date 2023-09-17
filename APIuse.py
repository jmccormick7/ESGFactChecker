import requests

API_URL = "https://api-inference.huggingface.co/models/mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "Exxon and Chevron investors shoot down climate proposals after a year a record profits",
})

print(output)