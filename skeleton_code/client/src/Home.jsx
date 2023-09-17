import React from "react";

import "./styles.css";

export default class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      company: "",
      news_header: "",
      news_info: "",
      esg_header: "",
      esg_info: "",
      sentiment_header: "",
      sentiment_info: "",
    };
  }

  //   REPLACE THIS WITH DATABASE
  blackstone_data = {
    news: "- Blackstone has completed a $1 billion equity investment in renewable energy company Invenergy, bringing its total investment in the company to $4 billion.",
    esg: "We are saving the world in terms of sustainability",
    sentiment: "Slightly negative sentiment",
  };
  chevron_data = {
    news: "- Exxon and Chevron investors have rejected climate measures.",
    esg: "We love the earth and work hard for it",
    sentiment: "Mildly negative sentiment",
  };
  nike_data = {
    news: '- A long-running lawsuit against Nike has revealed allegations of sexism, bullying, and fear of retaliation within the company, with female employees describing it as a "giant men\'s sports team" where favoritism prevails.',
    esg: "Our top priority is sustainability",
    sentiment: "Neutral Sentiment",
  };
  tesla_data = {
    news: "- Tesla is facing multiple lawsuits alleging racial discrimination and racism in its Fremont plant, with thousands of Black employees potentially joining one of the cases.",
    esg: "We treat our workers well",
    sentiment: "Positive Sentiment",
  };

  manual_database = {
    blackstone: this.blackstone_data,
    chevron: this.chevron_data,
    nike: this.nike_data,
    tesla: this.tesla_data,
  };

  handleCompanyChange = (event) => {
    this.setState({ company: event.target.value });
  };

  handleSubmit = () => {
    this.setState({ esg_header: "ESG Summary" });
    this.setState({
      esg_info: this.manual_database[this.state.company]["esg"],
    });
    this.setState({ news_header: "Related News" });
    this.setState({
      news_info: this.manual_database[this.state.company]["news"],
    });
    this.setState({ sentiment_header: "Sentiment Analysis" });
    this.setState({
      sentiment_info: this.manual_database[this.state.company]["sentiment"],
    });
  };

  render() {
    const company = this.state.company;

    return (
      <div>
        <div className="app">
          <div className="title">Foret API</div>
          <div className="body">Try our API below</div>
          <div className="tweet-box">
            <input
              value={company}
              onChange={this.handleCompanyChange}
              className="tweet-box-author"
              placeholder="Company"
            />
            <div className="tweet-box-actions">
              <button onClick={this.handleSubmit} className="tweet-box-submit">
                Submit
              </button>
            </div>
          </div>

          <div className="header"> {this.state.esg_header} </div>
          <div className="text">{this.state.esg_info}</div>
          <div className="header"> {this.state.news_header} </div>
          <div className="text">{this.state.news_info}</div>
          <div className="header"> {this.state.sentiment_header} </div>
          <div className="text">{this.state.sentiment_info}</div>
        </div>
      </div>
    );
  }
}
