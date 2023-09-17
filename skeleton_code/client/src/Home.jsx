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
    file = this.state.company + ".txt";
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
          <div>{this.state.company_info}</div>
        </div>
      </div>
    );
  }
}
