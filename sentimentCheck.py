import requests
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import json
import torch.nn.functional as F
import statistics

class SentimentAnalyzer():
   
    def __init__(self, newsArticle:list):
        self.newsArticle = newsArticle
        pass

    def getESG(self): 
        jsonSentiment = list()
        
        for jsonfile in self.newsArticle:
            stringInp = jsonfile["title"] + jsonfile["summary"]
            jsonSentiment.append((SentimentAnalyzer.sentimentScoring(stringInp), jsonfile["date"]))
        
        # return json_result
        return jsonSentiment

    @classmethod
    def sentimentScoring(cls, newsArticle:str):
        # Load model directly
        API_TOKEN = "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"

        tokenizer = AutoTokenizer.from_pretrained("mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis")
        model = AutoModelForSequenceClassification.from_pretrained("mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis")

        inputs = tokenizer(newsArticle, return_tensors="pt")
        outputs = model(**inputs)

        # Extract logits and apply softmax to get the probabilities
        logits = outputs.logits
        probabilities = F.softmax(logits, dim=1)[0].tolist()

        # Assuming three classes: 'negative', 'neutral', and 'positive'
        labels = ["negative", "neutral", "positive"]
        predicted_label = labels[probabilities.index(max(probabilities))]

        # Create a list of dictionaries with label and score
        scores = [{"label": label, "score": score} for label, score in zip(labels, probabilities)]

        # Convert results to JSON format
        result = {
            "predicted_label": predicted_label,
            "scores": scores,
        }

        # Convert to JSON string
        json_result = json.dumps(result, indent=4)
        return(json_result)
    
    
    




