import logo from './logo.svg';
import './App.css';
import {Component} from "react";

class App extends Component {
  state = {
    quests: []
  };

  async componentDidMount() {
    const response = await fetch('/quests');
    const body = await response.json();
    this.setState({quests: body});
  }

  render() {
    const {quests} = this.state;
    return (
        <div className="App">
          <header className="App-header">
            <img src={logo} className="App-logo" alt="logo" />
            <div className="App-intro">
              <h2>Clients</h2>
              {quests.map(quest =>
                  <div key={quest.id}>
                    {quest.name} ({quest.email})
                  </div>
              )}
            </div>
          </header>
        </div>
    );
  }
}
export default App;
