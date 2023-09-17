import React from "react";

import "./styles.css";

export default class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      company: "",
      company_info: "",
    };
  }

  handleCompanyChange = (event) => {
    this.setState({ company: event.target.value });
  };

  handleSubmit = () => {
    fetch("/api/add", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        author: this.state.author,
        tweet: this.state.tweet,
      }),
    })
      .then((res) => {
        return res.json();
      })
      .then((data) => {
        var tweetId = data.id;
        this.setState((prevState) => ({
          tweets: [
            ...prevState.tweets,
            {
              id: tweetId,
              author: prevState.author,
              tweet: prevState.tweet,
            },
          ],
          tweet: "",
        }));
      });
    this.setState({ company_info: this.state.company });
  };

  render() {
    const company = this.state.company;

    return (
      <div>
        <div className="app">
          <div className="title">Foret API</div>
          <div className="body">Try our api below</div>
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
          <div>{this.state.company_info}</div>
        </div>
      </div>
    );
  }
}
