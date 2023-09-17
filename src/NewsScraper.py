import aylien_news_api
from aylien_news_api.rest import ApiException
from pprint import pprint as pp
import json
import ast
import os

## Configure connection to the API
configuration = aylien_news_api.Configuration()
configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = 'befd2292'
configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = 'bdd192061113c19d38f04118b1b3fe56'
configuration.host = "https://api.aylien.com/news"
api_instance = aylien_news_api.DefaultApi(aylien_news_api.ApiClient(configuration))

# given a story in sentence list form, clean out newlines and extraneous information (author names, links, etc)
def clean_story(story):
    cleaned_output = []
    for sentence in story:
        sentence.replace("\n", "") # remove newlines
        sentence.replace ("\\n", "")
        if (".com" not in sentence
            and "Read more" not in sentence
            and "non-commercial" not in sentence
            and "min read" not in sentence): #remove extraneous text
            cleaned_output.append(sentence)
    return cleaned_output



## retrieve ESG information about a company
def get_headlines(company_name):

    ## List parameters as a search operator struct
    opts= {
        'title': '\"' + company_name + '\" AND ("ESG" OR "Sustainability" OR "Environment" OR "Diversity" OR "Climate" OR "Equality" OR "Carbon" OR "Conscious" OR "Responsibility" OR "CSR" OR "Environment, social, and governance" OR "Green" OR "Renewable" OR "Recycle" OR "Discrimination" OR "Racism" OR "Sexism")',
        'language': ['en'],
        'published_at_start': 'NOW-1YEAR',
        'published_at_end': 'NOW',
        'per_page': 25,
        'sort_by': 'relevance'
    }

    #setup list of articles. each artcle is a dict with keys "title" and "summary"
    articles = []

    try:
        ## Make a call to the Stories endpoint for stories that meet the criteria of the search operators
        api_response = api_instance.list_stories(**opts)
        ## Print the list of returned stories
        for story in api_response.stories:
            title = "{}".format(story.title)

            source_name = "{}".format(story.source.name)
            source_link = "{}".format(story.links.permalink)

            story = ast.literal_eval("{}".format(story.summary.sentences))
            story = clean_story(story)
            story = " ".join(story).strip() # separate sentences with space, remove author line
        

            articles.append({"title": title, "summary": story, "source_name": source_name, "url": source_link})
    except ApiException as e:
        print('Exception when calling DefaultApi->list_stories: %s\n' % e)
    
    #convert list to json
    articles_json = {"articles": articles}
    return articles_json

## takes in `article_list` of (title, summary) tuples and outputs it into a file called <output_name>.txt
def format_headlines(article_json, output_name):
    outdirectory_path = "./news_outputs"
    if not os.path.exists(outdirectory_path):
        os.makedirs(outdirectory_path)
    outfile = output_name.lower() + ".txt" #squash names to lowercase for lookup
    outfile_path = os.path.join(outdirectory_path, outfile)

    json_str = json.dumps(article_json, indent = 4)

    #memoize output for later
    with open(outfile_path, "w") as out:
            out.write(json_str)
    
    return json_str
    
# returns a json
def get_news(company_name):
    directory_path = "./news_outputs"

    for filename in os.listdir(directory_path):
        if os.path.isfile(os.path.join(directory_path, filename)):
            if company_name.lower() in filename:
                print("cached")
                with open(os.path.join(directory_path, filename), "r") as file:
                    jsonData = json.load(file)
                    return jsonData

    print("fetched")       
    return json.loads(format_headlines(get_headlines(company_name), company_name))


get_news("Microsoft")