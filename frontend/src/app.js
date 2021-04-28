import './app.css';
import Home from './pages/home';
import { Switch, Route } from 'react-router-dom';
import SearchPage from './pages/search_page';

export default function App() {
  return (
    <Switch>
      <Route exact path='/' component={Home} />
      <Route path='/search' component={SearchPage} />
    </Switch>
  );
}
