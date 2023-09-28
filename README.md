# ESGFactChecker


Inspiration:

Social and Environmental Sustainability is becoming an increasingly important alpha for corporate and consumer  investors. 
By providing sustainability information to investors, we can  enable more informed decisions and reward socially-conscious companies.

Current ESG Data is opaque, complex, paywalled, and biased:

Typical self-reported ESG dataset can be over 70 pages
“Objective” quantitative ESG metrics have no explanations of their derivation
Aggregators like Morningstar and Bloomberg charge tens of thousands for access 
Companies are more likely to report ESG data in a positive light

Our Approach:

We aim to use generative AI to summarize both ESG reports and third-party news articles into quick, easy to read bullet points that highlight key investment risks and CSR facts.
While current solutions provide ratings and scores to quantify ESG information, we use novel generative AI technology to provide qualitative summaries that can be quickly understood by investors.

Solution: Short, layman summaries of verified ESG data:

Inspired by Robinhood purchase briefs
Provide qualitative summaries of both self-reported ESG data and recent news articles regarding the company’s ESG efforts
Provide quantitative breakdown of sentiment regarding a company’s ESG efforts

News Scraping:

Aylien API to scrape recent news articles that contain (COMPANY_NAME AND {ESG word set})
Positive words such as “carbon,” “diversity,” and “impact”
Negative words such as “discrimination,” “racism”
After retrieving (~25-50) articles, we scrape their summaries and pass into OpenAI GPT-3.5 for aggregation
Typical aggregation prompt:
"Summarize key ESG metrics and statistics from the following articles in five bullet points:\n\n”
Typical response:

INSERT IMAGE

Sentiment Analysis using NLP Models & Hugging Face:

A sentiment NLP model, trained on financial data, from Hugging Face was used: https://huggingface.co/mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis
The model was installed using transformers from Hugging Face
We fed in the raw logits from this model into PyTorch softmax function to transform the scores into a range of 0 to 1. 
These softmax transformations gave us our percentages per label allowing us to quantify relative relationships between the 3 sentiment categories for each article.
Our Sentiment Analysis then takes the values for every article scraped and find the mean and standard deviation of these label categories to get the broad sentiment 

ESG Report Summaries:

In order to summarize the entire PDF, we first use langchain PDF loading and text splitting to split long documents into short segments of text.
GPT and other Generative AI tools have a maximum token length: 4000 tokens for the GPT model we currently use.
We use the map reduce technique to first summarize each individual section, then extract key facts and statistics from these summaries.
Emphasis on: Key risks for investing in the company, Environmental positives and negatives, Social positives and negatives, Governance positives and negatives, Adherence to government regulations.
The tech stack uses langchain as a LLM framework, as well as text-bison and GPT models for summary generation.

Future Plans:

In the future we want to create a website that would allow for direct access to our API.
We had been working on a website using a React Frontend and a Flask Backend but unfortunately we were unable to get past some server-client issues in time
We feel in the long term there is opportunity to develop and train our own models to more narrowly tailor our metrics, both on the generative AI side and the NLP side.
We also were looking at performing time series analysis into general sentiment scores, so we could observe changes over time in the companies public ESG sentiment. 
Finally, we would like to further develop this as a plugin for financial apps like Robinhood to continue to help consumer traders get more information about the trades they are making.
