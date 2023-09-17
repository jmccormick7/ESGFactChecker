from pathlib import Path as p

from langchain import OpenAI
from langchain import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader

import urllib


data_folder = p.cwd() / "data"
p(data_folder).mkdir(parents=True, exist_ok=True)

pdf_url = "https://www.chevron.com/-/media/shared-media/documents/chevron-sustainability-report-2022.pdf"
pdf_file = str(p(data_folder, pdf_url.split("/")[-1]))

urllib.request.urlretrieve(pdf_url, pdf_file)


pdf_loader = PyPDFLoader(pdf_file)
print(pdf_loader)
pages = pdf_loader.load_and_split()
text = "\n".join([(page if isinstance(page, str) else page.page_content) for page in pages])

OPENAI_API_KEY = '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'
llm = OpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)

text_splitter = RecursiveCharacterTextSplitter(separators=["\n\n", "\n"], 
 chunk_size=3000, chunk_overlap=100)

docs = text_splitter.create_documents([text])

map_prompt_template = """
                      Write a two sentence summary of the following text delimited by triple backquotes that includes the main points and any important details. Please consider the following information if it is present in the passage:
              Key risks in investing in the company, Environmental positives and negatives, Social positives and negatives, Governance positives and negatives, Overall sentiment, Adherance to government regulations, Change over time. Also, focus on sentences with these keywords: ESG, Sustainability, Environment, Diversity, Climate, Equality, Carbon, Conscious, Responsibility, CSR, Environment, Social, and Governance, Green, Renewable, Recycle, Discrimination, Racism, Sexism.
                      ```{text}```
                      """

map_prompt = PromptTemplate(template=map_prompt_template, input_variables=["text"])

combine_prompt_template = """
                      Write a one to three page summary of the following text delimited by triple backquotes.
                      Return your response in bullet points which covers the key points of the text. Please consider the following information if it is present in the passage:
              Key risks in investing in the company, Environmental positives and negatives, Social positives and negatives, Governance positives and negatives, Overall sentiment, Adherance to government regulations, Change over time. Also, focus on sentences with these keywords: ESG, Sustainability, Environment, Diversity, Climate, Equality, Carbon, Conscious, Responsibility, CSR, Environment, Social, and Governance, Green, Renewable, Recycle, Discrimination, Racism, Sexism. 
                      ```{text}```
                      BULLET POINT SUMMARY:
                      """

combine_prompt = PromptTemplate(
    template=combine_prompt_template, input_variables=["text"]
)

summary_chain = load_summarize_chain(llm=llm,
 chain_type='map_reduce',
 map_prompt=map_prompt,
 combine_prompt=combine_prompt,
)

summary_chain = load_summarize_chain(llm=llm, chain_type='map_reduce')
output = summary_chain.run(docs)
print(output)

