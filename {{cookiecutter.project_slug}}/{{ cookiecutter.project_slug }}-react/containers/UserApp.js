import React, {Component, PropTypes} from 'react'
import {connect} from 'react-redux'
import {bindActionCreators} from 'redux'

import {fetchUser, changeUserName, saveUser} from '../actions/userActions'
import {cookies} from '../util.js'

class UserApp extends Component {

  componentDidMount(){
    const {dispatch} = this.props
    dispatch(fetchUser())
  }

  render() {
    const {user}  = this.props
    return (
      <div className="row">
        <div className="col-sm-3 col-md-2 sidebar">
          <ul className="nav nav-sidebar">
            <li className="active"><a href="#">Overview <span className="sr-only">(current)</span></a></li>
            <li><a href="#">Item 1</a></li>
            <li><a href="#">Item 2</a></li>
          </ul>
        </div>
        <div className="col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2 main">
        <ol className="breadcrumb">
          <li className="active">
            <strong>Hi from react!</strong>
          </li>
        </ol>
        <div className="box">
          {user &&
            <div>
            <p>This part was loaded by react/redux using djangorestframework with session authentication.</p>

            <h3>Change Name</h3>
            <div className="form-inline">
              <div className="form-group">
                <label className="sr-only" htmlFor="name">Name</label>
                <input onChange={(event) => this.props.changeUserName(event.target.value)}
                       type="text" className="form-control" id="name"
                       placeholder="Name" value={user.name}/>
              </div>

              <button onClick={() => this.props.saveUser(user)}
                      className="btn btn-default">
                      Save
              </button>
              </div>
              <h3>JSON</h3>
              <pre>
                {JSON.stringify(user, null, 2) }
              </pre>
            </div>
          }
          </div>
        </div>
      </div>
    )
  }
}
function mapStateToProps(state) {
  return {
    user: state.user,
  }
}

function mapDispatchToProps(dispatch) {
  return {
    saveUser: (user) => dispatch(saveUser(user)),
    changeUserName: (name) => dispatch(changeUserName(name)),
    dispatch: dispatch
  }
}

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(UserApp)
