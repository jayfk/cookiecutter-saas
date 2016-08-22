import React from 'react'
import {Route, IndexRoute, Redirect} from 'react-router'

import App from './components/App'
import UserApp from './containers/UserApp'


export default (
  <Route path="/app/" component={App}>
    <IndexRoute component={UserApp} />
    <Redirect from="/app/*" to="/app/" />
  </Route>
)
