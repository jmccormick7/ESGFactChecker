from sentimentCheck import SentimentAnalyzer
import json
#import summarize_pdf
# from src/DocScraper.py
from src import NewsScraper
from src import NewsSummarizer
import statistics

class ForetAPI():
    def __init__(self, company_name):
        self.company_name = company_name

    def getNewsJSON(self):
        self.newsJSON =  NewsScraper.get_news(self.company_name)
    
    def getNewsSummary(self):
        self.newsGPT = NewsSummarizer.get_gpt(self.company_name)

    def getESG(self, JSONList:list): 
        sentiment = SentimentAnalyzer(JSONList)
        # jsonSentiment = SentimentAnalyzer.sentimentScoring(self.company_name)
        # return json_result
        return sentiment.getESG()
    
    def parse_articles(self, json_data):
        return json_data.get("articles", [])
    
    @classmethod
    def getMeanandSD(cls, jsonSentiment:list):
        positive_scores = []
        negative_scores = []
        neutral_scores = []

        for jsonfile in jsonSentiment:
            scores = json.loads(jsonfile[0])["scores"]
            for score_item in scores:
                label = score_item["label"]
                score = score_item["score"]
            
                if label == "positive":
                    positive_scores.append(score)
                elif label == "negative":
                    negative_scores.append(score)
                elif label == "neutral":
                    neutral_scores.append(score)

        # Calculate mean and standard deviation for each label
        positive_mean = statistics.mean(positive_scores)
        if len(positive_scores) > 1:
            positive_sd = statistics.stdev(positive_scores)
        else:
            positive_sd = 0

        negative_mean = statistics.mean(negative_scores)
        if len(negative_scores) > 1:
            negative_sd = statistics.stdev(negative_scores)
        else:    
            negative_sd = 0

        neutral_mean = statistics.mean(neutral_scores)
        if len(neutral_scores) > 1:
            neutral_sd = statistics.stdev(neutral_scores)
        else:   
            neutral_sd = 0

        return {
            "positive": {"mean": positive_mean, "sd": positive_sd},
            "negative": {"mean": negative_mean, "sd": negative_sd},
            "neutral": {"mean": neutral_mean, "sd": neutral_sd}
        }
    
    # def main(self):
    #     self.newsScraper = AylienNews()
    #     self.newsScraper.get_news("Tesla")
    #     get_gpt("Tesla")
    #     sentiment = self.getESG()
    #     # return sentiment
    #     print(sentiment)


if __name__ == "__main__":
    foret = ForetAPI("Tesla")
    teslaJSON = {
        "articles": [
            {
                "title": "\"Tesla Hotbed For Racism\": Lawsuit Claims 6,000 Workers Faced Discrimination",
                "summary": "If a judge in agrees to broaden the case, it would raise the stakes for Elon Musk's company. Tesla has been hit with a number of high-profile suits - including one filed by the state of California in February of last year - over its treatment of Black employees and contract workers at the Fremont plant.\n\n Lawyers for Vaughn said as many as 6,000 Black workers would be eligible to join the the case, though not all may seek monetary damages.\n\n A Black former assembly line staffer at Tesla Inc. is moving to add hundreds of other workers to his 2017 lawsuit in which he called the electric-car maker's production floor a \"hotbed for racist behavior. If a state court judge in Oakland agrees to let Vaughn broaden the case, it would raise the stakes for Elon Musk's company.",
                "source_name": "NDTV",
                "url": "https://www.ndtv.com/world-news/tesla-hotbed-for-racism-lawsuit-claims-6-000-workers-faced-discrimination-4097497",
                "date": "2023-06-06 02:36:18+00:00"
            },
            {
                "title": "Tesla Discrimination Verdict",
                "summary": "FILE - Vehicles are parked outside the Tesla plant, in Fremont, Calif., on May 12, 2020.\n (AP Photo/Ben Margot, File) FILE PHOTO\n  BM DD\n  \uc774 \uae30\uc0ac\ub294 \uc5b8\ub860\uc0ac\uc5d0\uc11c \uc138\uacc4 \uc139\uc158\uc73c\ub85c \ubd84\ub958\ud588\uc2b5\ub2c8\ub2e4.\n  2023 \uc2a4\ud0c0 \ucc44\ub110\uc744 \ucc3e\uc544\ub77c! A federal jury on Monday, April 3, 2023, has awarded nearly $3.2 million in damages to a former Black worker at a Tesla factory California that has been at the epicenter of racial discrimination allegations hanging over the automaker run by billionaire Elon Musk.",
                "source_name": "Naver",
                "url": "https://n.news.naver.com/mnews/article/077/0005906216",
                "date": "2023-04-04 20:51:29+00:00"
            },
            {
                "title": "Elon Musk says 'ESG is the devil' with tobacco firms trouncing Tesla in social-responsibility ratings",
                "summary": "Elon Musk slammed the framework that evaluates companies' environmental, social and governance standards, flagging that tobacco firms tend to receive higher ESG ratings than electric-vehicle maker Tesla\n \"Why ESG is the devil,\" the Tesla and SpaceX chief said on Twitter , in response to an article by Washington Free Beacon reporter Aaron Sibarium.\n   \"From S&P Global to the London Stock Exchange, tobacco companies are crushing Tesla in the ESG ratings,\" Sibarium had tweeted Tuesday\n  \"How could cigarettes, which kill over 8 million a year, be deemed a more ethical investment than electric cars?\" he added.\n  Sibarium's article pointed out that S&P Global's latest ESG rankings gave EV maker Tesla a score of 37 \u2013 and tobacco giant Philip Morris an 84.\n   The London Stock Exchange gave British American Tobacco an ESG rating of 94, and Tesla a more middling 65.\n   They often use a 1-to-100 ratings scale, determined by research firms like S&P Global and Morningstar.",
                "source_name": "Yahoo",
                "url": "https://news.yahoo.com/elon-musk-says-esg-devil-132731052.html",
                "date": "2023-06-14 16:29:03+00:00"
            },
            {
                "title": "Elon Musk says 'ESG is the devil' with tobacco firms trouncing Tesla in social-responsibility ratings",
                "summary": "Elon Musk called the framework that evaluates companies' social and sustainability standards \"the devil\" on Wednesday.\n\n download the app Email address By clicking \u2018Sign up\u2019, you agree to receive marketing emails from Insider as well as other partner offers and accept our Terms of Service and Privacy Policy\n\nElon Musk slammed the framework that evaluates companies' environmental, social and governance standards, flagging that tobacco firms tend to receive higher ESG ratings than electric-vehicle maker Tesla.\n\n \"From S&P Global to the London Stock Exchange, tobacco companies are crushing Tesla in the ESG ratings,\" Sibarium had tweeted Tuesday.\n\n Sibarium's article pointed out that S&P Global's latest ESG rankings gave EV maker Tesla a score of 37 \u2013 and tobacco giant Philip Morris an 84.",
                "source_name": "Business Insider",
                "url": "https://markets.businessinsider.com/news/stocks/elon-musk-tesla-stock-price-esg-tobacco-green-investing-twitter-2023-6",
                "date": "2023-06-14 13:32:30+00:00"
            },
            {
                "title": "Tesla Racial Discrimination Lawsuit",
                "summary": "Tesla Cars  FILE - Tesla cars are loaded onto carriers at the Tesla electric car plant on May 13, 2020, in Fremont, Calif.\nLawyers seeking to bring a class-action lawsuit against Tesla submitted declarations Monday, June 5, 2023, in Alameda County Superior Court from 240 Black workers who testified to rampant racism and discrimination at the electric car maker's Fremont factory in Northern California, including frequent use of the N-word and references to the manufacturing site as a plantation or slave ship. (AP Photo/Ben Margot, File) FILE PHOTO",
                "source_name": "Naver",
                "url": "https://n.news.naver.com/mnews/article/077/0005961262",
                "date": "2023-06-07 20:30:25+00:00"
            },
            {
                "title": "Elon Musk blasts ESG as \u2018the devil' after tobacco stocks beat Tesla in sustainability indexes",
                "summary": "\u201cESG is the devil,\u201d wrote Musk on Wednesday in response to a report published in the Washington Free Beacon\n  The article cited Tesla's poor score upon re-entering the S&P 500 sustainability index, receiving only 37 out of a maximum 100 points, versus the 84 achieved by cigarette merchant Philip Morris International\n  Companies like PMI and Altria , which split up the rights to sell Marlboro when the company broke up, are responsible for an estimated 8 million cancer-related deaths worldwide every year and would not seem obvious candidates for ESG investing.\n   In this article:  PM\n When it comes to ethical investing, tobacco companies selling a lifestyle product proven to cause cancer are leaving Elon Musk's Tesla behind in a cloud of smoke and it has left the entrepreneur steaming.\n   Yet the right-leaning publication reported the two companies have bumped up their score in various sustainability indexes including by emphasizing diversity in their boards, the funding of minority businesses and other inclusive measures in an attempt to win back deep-pocket asset managers.\n   Reportedly thanks to a clever embrace of diversity, equity and inclusion policies\u2014which Musk calls \u201cwoke\u201d\u2014it has earned a higher score when it comes to environmental, social and governance (ESG) criteria in recent sustainability indexes.",
                "source_name": "Yahoo! Finance News",
                "url": "https://finance.yahoo.com/news/elon-musk-blasts-esg-devil-154219376.html",
                "date": "2023-06-15 19:05:24+00:00"
            },
            {
                "title": "Tesla countersues California agency that filed racial discrimination suit against it",
                "summary": "Tesla Inc. has countersued the California agency that filed a racial discrimination lawsuit against the company, alleging that the government organization violated state law in bringing about the suit. The Tesla TSLA, lawsuit says its aim is to stop the agency, also referred to as CRD, from breaking rules collectively known as the California Administrative Procedure Act.   The electric-vehicle maker, in the suit filed Thursday in Alameda County Superior Court, said the California Civil Rights Department \u2014 previously known as the California Department of Fair Employment and Housing \u2014 violated state rules by filing the lawsuit without seeking public comment or holding a public hearing.   \u201cCRD abused its discretion, acted in excess of its statutory power and authority, and failed to proceed in the manner required by law by promulgating and generally applying the rules,\u201d Tesla says in its countersuit.",
                "source_name": "MarketWatch",
                "url": "https://www.marketwatch.com/story/tesla-countersues-california-agency-that-filed-racial-discrimination-suit-against-it-11663892619",
                "date": "2022-09-23 00:28:35+00:00"
            },
            {
                "title": "\u2018ESG is the devil': Oil and tobacco companies score better ESG rankings than Tesla",
                "summary": "Sky News host Chris Kenny says tobacco and oil companies have scored better ESG rankings than Tesla, the maker of zero-emissions cars.\n\n \u201cWell, the point here is that the tobacco companies and the oil companies actively campaign to demonstrate their virtue in ESG terms.\n\n \u201cIt\u2019s little wonder that this has gotten Elon Musk, the Tesla founder and CEO, tweeting that \u2018ESG is the devil\u2019 \u2013 Yep, he just might be right on that,\u201d Mr Kenny said.",
                "source_name": "News.com.au",
                "url": "https://www.news.com.au/national/esg-is-the-devil-oil-and-tobacco-companies-score-better-esg-rankings-than-tesla/video/44ece6caea6aa65f2ffe8cb390307334",
                "date": "2023-06-15 12:09:31+00:00"
            },
            {
                "title": "Tesla Countersues California Agency That Filed Racial Discrimination Lawsuit",
                "summary": "Tesla has countersued the California agency that filed a racial discrimination lawsuit against the company, alleging that the government organization violated state law in bringing about the suit.\n\n The electric-vehicle maker, in the suit filed Thursday in Alameda County Superior Court, said the California Civil Rights Department\u2014previously known as the California Department of Fair Employment and Housing\u2014violated state rules by filing the lawsuit without seeking public comment or holding a public hearing.",
                "source_name": "Wall Street Journal",
                "url": "https://www.wsj.com/articles/tesla-countersues-california-agency-that-filed-racial-discrimination-lawsuit-11663891682",
                "date": "2022-09-23 00:12:30+00:00"
            },
            {
                "title": "How Tesla 'won' a $3 million fine for race discrimination",
                "summary": "(Reuters) - Orrick, who didn't specifically call out Tesla for its maneuver on retrial, had previously reprimanded Tesla in a 2022 ruling for making the same accusation although \u201cit can point to no evidence\u201d and \u201cdid not impeach Diaz's credibility.\u201d\n  Allegations of a plantation-style workplace in Tesla's Fremont facility are not unique to Diaz's case, despite the company's forceful denials.\n   A recent trial and $3.2 million verdict against Tesla Inc for race discrimination against an ex-employee was arguably a win for the electronic car maker, which was accused of creating a \"plantation-mentality workplace\" in Fremont, California.\n   Diaz's attorneys described Tesla's arguments in court as stereotypes and \u201crace-baiting\u201d that sought to undermine the previous jury's findings by reframing the case as a minor \u201cconflict between Latinos and African Americans.\" Orrick even commented that the company's inquiries were somewhat like asking a defendant \u201cwhen did you stop beating your wife?\u201d\n  Perhaps most worrisome, Tesla's attorneys accused Diaz himself of making sexual and racially harassing comments to a Latino co-worker \u2013 without any meaningful evidence.",
                "source_name": "Reuters",
                "url": "https://www.reuters.com/legal/litigation/how-tesla-won-3-million-fine-race-discrimination-2023-04-18/",
                "date": "2023-04-18 22:00:24+00:00"
            },
            {
                "title": "Tesla stock bull: The company is a sustainability 'behemoth'",
                "summary": "\u00b7  Anchor, Editor-at-Large  En este art\u00edculo:  TSLA  GM  F\n Amid the carnage that is Tesla's stock price headed into 2023, a Wall Street bull has emerged with a reminder to all that the company remains a longer-term sustainability play.\n   \"Need a leader at this time for Tesla, not Ted Striker,\" former Tesla bull Ives said in a new note on Friday , referring to the pilot in the comedy film \"Airplane.\"\n  \"At the same time that Tesla is cutting prices and inventory is starting to build globally in face of a likely global recession, Musk is viewed as 'asleep at the wheel' from a leadership perspective for Tesla at the time investors need a CEO to navigate this Category 5 storm,\" Ives added. Others, such as Wedbush analyst Dan Ives, continue to trim price targets on Tesla amid the stock's precipitous fall.\n   The analyst sees fair value for Tesla's stock at $275, up sizably from its current price of $123 in midday Friday trading.\n   This week brought news Tesla will offer $7,500 discounts on Model 3 and Model Y vehicles delivered in the U.S. in December \u2014 an unexpected development that further pressured the stock price.",
                "source_name": "Yahoo! Finanzas Espana (Spanish)",
                "url": "https://es.finance.yahoo.com/news/tesla-stock-bull-price-sustainability-behemoth-171323053.html",
                "date": "2022-12-23 17:57:51+00:00"
            },
            {
                "title": "2 Green Flags for Tesla's Future",
                "summary": "Tesla (TSLA 7.67%) has delivered astounding returns for investors in recent years. not only has a major upcoming growth catalyst in Cybertruck, but investors should also take comfort in the fact that Tesla is a rare electric vehicle maker that is profitable.\u00a0 The F-150 is Ford's highest-volume vehicle,\u00a0but Tesla could take some share away from the industry leader. Regardless, it seems Tesla will try to price the vehicle to compete with the Ford\u00a0F-150 -- the top-selling vehicle in the U.S. last year.\u00a0\n\n\n Americans love their trucks, so it wouldn't be surprising for Cybertruck to become Tesla's best-selling vehicle.",
                "source_name": "The Motley Fool",
                "url": "https://www.fool.com/investing/2022/12/01/2-green-flags-for-teslas-future/?source=iedfolrf0000001",
                "date": "2022-12-01 14:02:35+00:00"
            },
            {
                "title": "Tesla stock bull: The company is a sustainability 'behemoth'",
                "summary": "The analyst sees fair value for Tesla's stock at $275, up sizably from its current price of $123 in midday Friday trading.\n   Others, such as Wedbush analyst Dan Ives, continue to trim price targets on Tesla amid the stock's precipitous fall. This week brought news Tesla will offer $7,500 discounts on Model 3 and Model Y vehicles delivered in the U.S. in December \u2014 an unexpected development that further pressured the stock price.\n   Gianarikas acknowledged, however, that the near-term is uncertain on Tesla.",
                "source_name": "Yahoo! Finance News",
                "url": "https://finance.yahoo.com/news/tesla-stock-bull-price-sustainability-behemoth-171323053.html",
                "date": "2022-12-23 17:18:58+00:00"
            },
            {
                "title": "Tesla stock bull: The company is a sustainability 'behemoth'",
                "summary": "In this article:  TSLA  GM  F  Amid the carnage that is Tesla's stock price headed into 2023, a Wall Street bull has\nemerged with a reminder to all that the company remains a longer-term sustainability play.\n   \"Need a leader at this time for Tesla, not Ted Striker,\" former Tesla bull Ives said in a new note on Friday , referring to the pilot in the comedy film \"Airplane.\"\n  \"At the same time that Tesla is cutting prices and inventory is starting to build globally in face of a likely global recession, Musk is viewed as 'asleep at the wheel' from a leadership perspective for Tesla at the time investors need a CEO to navigate this Category 5 storm,\" Ives added. Others, such as Wedbush analyst Dan Ives, continue to trim price targets on Tesla amid the stock's precipitous fall.\n   The analyst sees fair value for Tesla's stock at $275, up sizably from its current price of $123 in midday Friday trading.\n   In a new note to clients, Gianarikas called Tesla ( TSLA ) a sustainability \"behemoth\" \u2014 pointing to leadership positions in EVs and in solar with SolarCity.",
                "source_name": "Yahoo! Finance France (French)",
                "url": "https://ca.finance.yahoo.com/news/tesla-stock-bull-price-sustainability-behemoth-171323053.html",
                "date": "2022-12-23 17:36:46+00:00"
            },
            {
                "title": "Tesla stock bull: The company is a sustainability 'behemoth'",
                "summary": "Amid the carnage that is Tesla's stock price headed into 2023, a Wall Street bull has emerged with a reminder to all that the company remains a longer-term sustainability play.\n\n The analyst sees fair value for Tesla's stock at $275, up sizably from its current price of $123 in midday Friday trading.\n\n Others, such as Wedbush analyst Dan Ives, continue to trim price targets on Tesla amid the stock's precipitous fall.\n\n \"At the same time that Tesla is cutting prices and inventory is starting to build globally in face of a likely global recession, Musk is viewed as 'asleep at the wheel' from a leadership perspective for Tesla at the time investors need a CEO to navigate this Category 5 storm,\" Ives added. This week brought news Tesla will offer $7,500 discounts on Model 3 and Model Y vehicles delivered in the U.S. in December \u2014 an unexpected development that further pressured the stock price.",
                "source_name": "Yahoo",
                "url": "https://news.yahoo.com/tesla-stock-bull-price-sustainability-behemoth-171323053.html",
                "date": "2022-12-23 17:27:52+00:00"
            },
            {
                "title": "Tesla stock bull: The company is a sustainability 'behemoth'",
                "summary": "Canaccord Genuity Managing Director George Gianarikas joins Yahoo Finance Live to discuss the market's reaction to Tesla stock, how investors are\ndealing with the stock following uncertainty, uncertainty around EV delivery, a recession, growth, and the outlook for sustained leadership within the EV space.\n   Brian Sozzi\n  \u00b7\n  3 \u5206\u9418\u6587\u7ae0\n  \u5728\u9019\u7bc7\u6587\u7ae0\u4e2d:\n  F\n  Amid the carnage that is Tesla's stock price headed into 2023, a Wall Street bull has emerged with a reminder to all that the company remains a longer-term sustainability play.\n   The analyst sees fair value for Tesla's stock at $275, up sizably from its current price of $123 in midday Friday trading.\n   Others, such as Wedbush analyst Dan Ives, continue to trim price targets on Tesla amid the stock's precipitous fall. And on the other side, they are destined to increase their leadership in EVs, which we think are on the cusp of really penetrating penetrating the overall auto market,\" Canaccord Genuity analyst George Gianarikas told Yahoo Finance Live (video above).",
                "source_name": "Hk Finance Yahoo",
                "url": "https://hk.finance.yahoo.com/news/tesla-stock-bull-price-sustainability-behemoth-171323053.html",
                "date": "2022-12-23 22:33:25+00:00"
            },
            {
                "title": "California agency asks court to order Tesla to cooperate in discrimination investigation",
                "summary": "Amy Kaufman: No, Emily Ratajkowski Won't Just Shut Up And Look Pretty\n\nEmily Ratajkowski knows that everyone is looking at her.",
                "source_name": "Scribd",
                "url": "https://www.scribd.com/article/638138139/California-Agency-Asks-Court-To-Order-Tesla-To-Cooperate-In-Discrimination-Investigation",
                "date": "2023-04-14 23:12:22+00:00"
            },
            {
                "title": "Ex-Tesla Factory Worker Takes the Stand in Racial Discrimination Trial",
                "summary": "Tesla is being sued for racial discrimination at the Fremont, California factory\n\nAn ex-Tesla factory worker took the stand following a lawsuit he filed against the company for racial discrimination from mid-2015 through 2016. Diaz\u2019s trial gets underway as Tesla faces a separate class-action lawsuit in California from former employees who similarly claim they were racially discriminated against at the Fremont factory. The company\u2019s lawyer, Alex Spiro, told the jury on Monday, that while racial discrimination conducted at the Fremont factory was indefensible, he said the claims were exaggerated and questioned whether Diaz had suffered psychological damage, Reuters reported. The trial began in San Francisco federal court on Monday and Diaz\u2019s lawyer told the jury Black workers were treated as second-class citizens at the Tesla factory. Owen Diaz, a Black former escalator worker at the Tesla factory in Fremont, California claims he was subjected to racially discriminatory comments and actions from his coworkers over the nine months he worked at the company\u2019s factory.",
                "source_name": "Yahoo",
                "url": "https://news.yahoo.com/ex-tesla-factory-worker-takes-220500562.html",
                "date": "2023-03-29 22:57:49+00:00"
            },
            {
                "title": "Tesla racial-discrimination trial begins after record judgment was reduced",
                "summary": "A Black elevator operator at Tesla Inc. Tesla had urged the judge to reduce the jury award to $600,000, with the company\u2019s lawyers acknowledging in a filing that the use of racial slurs in a workplace was \u201cdeeply offensive\u201d and \u201cutterly unacceptable.\u201d TSLA, +0.40% who in 2021 was awarded $137 million by a jury that agreed he was subjected to racial harassment at the automaker\u2019s Fremont, Calif. factory, then saw a judge reduce the award to $15 million last year, is back in San Francisco federal court Monday for a new trial. Diaz\u2019s lawyers are hoping to increase the payout to their client as they re-argue the case before the same U.S. District Court judge, William Orrick, in a trial that is reportedly expected to last five days. During the original trial, Owen Diaz testified that he was regularly called the N-word and other racial slurs, including by a supervisor, at work.",
                "source_name": "Market Watch",
                "url": "https://www.marketwatch.com/story/tesla-racial-discrimination-trial-begins-after-record-judgment-was-reduced-5227e43c",
                "date": "2023-03-27 16:53:06+00:00"
            },
            {
                "title": "Shareholders launch campaign to tie Elon Musk\u2019s salary to Tesla\u2019s ESG",
                "summary": "\u00a9 Provided by City AM Shareholders have launched a campaign to tie Elon Musk\u2019s salary to Tesla\u2019s ESG performance.\n\n Shareholders, spearheaded by activist investor Tulipshare, have launched a campaign to tie Elon Musk\u2019s salary to Tesla\u2019s environmental, social and governance (ESG) performance.\n\n The post Shareholders launch campaign to tie Elon Musk\u2019s salary to Tesla\u2019s \u201cFacing multiple lawsuits because of its lack of ESG focus, it is time that investors \u2013 including retail investors \u2013 hold Tesla\u2019s CEO accountable,\u201d said Antoine Argouges, chief executive of London-based Tulipshare.\n\n Currently, Musk\u2019s pay is tied to Tesla\u2019s performance and that has led to an increase in investors\u2019 returns.",
                "source_name": "MSN UK",
                "url": "https://www.msn.com/en-gb/money/other/shareholders-launch-campaign-to-tie-elon-musk-s-salary-to-tesla-s-esg/ar-AA13aovy?ocid=finance-verthp-feeds",
                "date": "2022-10-20 08:34:17+00:00"
            },
            {
                "title": "Shareholder Group Calls for Tesla to Link Executive Pay to ESG Metrics",
                "summary": "By Michael Elkins  Shares of Tesla, Inc. (NASDAQ: TSLA ) are down 4.69% in pre-market trading on Thursday after Retail activist shareholder\nplatform Tulipshare called on the electric vehicle company to tie its executive pay to environmental, social and governance (ESG) factors. Tulipshare believes that the decision by S&P Dow Jones Indices last spring to remove Tesla from a widely followed ESG index showed the company faces reputational and legal risks that investors will not tolerate.   Tesla CEO Elon Musk pushed hard against S&P's decision, tweeting in May that \"ESG is a scam\". The activist group said it expects to file a shareholder resolution on the matter for the electric car maker's annual meeting next year.   However, the company has embraced some ESG trends such as reporting its production and energy consumption and providing workforce demographic data.",
                "source_name": "Investing.com Uk",
                "url": "https://uk.investing.com/news/stock-market-news/shareholder-group-calls-for-tesla-to-link-executive-pay-to-esg-metrics-432SI-2789392",
                "date": "2022-10-20 12:45:15+00:00"
            },
            {
                "title": "Shareholder group wants Tesla to link Musk's pay to ESG metrics",
                "summary": "By Ross Kerber  (Reuters) - Retail activist shareholder platform Tulipshare called on Tesla Inc to tie its executive pay to environmental, social\nand governance (ESG) factors and said it expects to file a shareholder resolution on the matter for the electric carmaker's annual meeting next year.   Antoine Argouges, chief executive of Britain-based Tulipshare, said a decision by S&P Dow Jones Indices last spring to oust Tesla from a widely followed ESG index showed the company faces reputational and legal risks that investors will not tolerate.   While Tesla CEO Elon Musk pushed hard against S&P's decision, tweeting in May that \"ESG is a scam,\" the company has embraced some ESG trends such as reporting its production and energy consumption and providing workforce demographic data.   Shareholder resolutions at Tesla's 2023 annual meeting are due by early next year. At its latest annual meeting, held in August, investors mostly sided with the recommendations of directors, helped by Musk's 15.6% stake in the company.",
                "source_name": "MSN News Canada",
                "url": "https://www.msn.com/en-ca/money/topstories/shareholder-group-wants-tesla-to-link-musk-s-pay-to-esg-metrics/ar-AA13aC1O",
                "date": "2022-10-20 05:42:03+00:00"
            },
            {
                "title": "Shareholder Group Calls for Tesla to Link Executive Pay to ESG Metrics",
                "summary": "Stock Markets  8 minutes ago (Oct 20, 2022 07:40)   TSLA   US500   DJI   By Michael Elkins\n Shares of Tesla, Inc. (NASDAQ: ) are down 4.69% in pre-market trading on Thursday after Retail activist shareholder platform Tulipshare called on the electric vehicle company to tie its executive pay to environmental, social and governance (ESG) factors. Alcoa Drops 10% After a Big Q3 Miss and Guide Down, Goldman Sees Attractive Entry Point  By Senad Karaahmetovic Shares of Alcoa (NYSE:AA) are trading 10% lower in pre-market Thursday after the aluminum business reported weak Q3 results. Tulipshare believes that the decision by Indices last spring to remove Tesla from a widely followed ESG index showed the company faces reputational and legal risks that investors will not tolerate.   Related Articles  Amazon Reiterated as Top Pick at Morgan Stanley, Credit Suisse  By Senad Karaahmetovic Amazon (NASDAQ:AMZN) is due to report on its Q3 performance next week.",
                "source_name": "Investing.com South Africa",
                "url": "https://za.investing.com/news/shareholder-group-calls-for-tesla-to-link-executive-pay-to-esg-metrics-432SI-2635154",
                "date": "2022-10-20 12:48:06+00:00"
            },
            {
                "title": "Shareholder Group Wants Tesla to Link Musk's Pay to ESG Metrics",
                "summary": "By Reuters| Oct. 20, 2022, at 1:07 a.m.",
                "source_name": "U.S. News & World Report Online",
                "url": "https://money.usnews.com/investing/news/articles/2022-10-20/shareholder-group-wants-tesla-to-link-musks-pay-to-esg-metrics",
                "date": "2022-10-20 05:42:35+00:00"
            },
            {
                "title": "Elon Musk: Tesla \u2018Not Immune' to Global Economic Environment",
                "summary": "Reuters\n\nA Pakistani court in the eastern city of Lahore on Monday granted bail until May 23 to former Prime Minister Imran Khan's wife in a graft case, a lawyer in their legal team said. Khan was arrested by the country's anti-graft agency last week in the same case, prompting violent protests across the country, which is already reeling from a crippling economic crisis. -accused along with Khan in the case, which pertained to the alleged receiving of financial help from a land developer in the setting-up of Al Qadir University of which the former premier and his spouse are trustees. Khan's wife, Bushra Bibi, was co",
                "source_name": "Yahoo! Finance France (French)",
                "url": "https://ca.finance.yahoo.com/video/elon-musk-tesla-not-immune-011600423.html",
                "date": "2023-05-17 05:18:31+00:00"
            }
        ]
    }
    articles = foret.parse_articles(teslaJSON)
    scores = foret.getESG(articles)
    data = ForetAPI.getMeanandSD(scores)
    print(data)


