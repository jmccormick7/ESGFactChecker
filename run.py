#!/venv/bin/python
from flask import Flask, request
import ForetAPI

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello there' 

@app.route('/esg/<company>')
def esg(company):
    pdf = request.args.get('pdf_url')
    pdf_summary = ForetAPI.getPDFSummary(pdf)
    news_summary = ForetAPI.getNewsSummary(company)

    return  f'Here is a summary of key ESG considerations from {company}\'s annual report: \\n{pdf_summary} \
\\n Here is a summary of key ESG considerations from news about {company}: \\n{news_summary}'  



# Keep this at the bottom of run.py
app.run(debug=True)