import * as types from '../constants/actionTypes'


const initialState = null

export default function counter(state = initialState, action) {
  switch (action.type) {
    case types.RECEIVE_USER:
      return action.user
    case types.CHANGE_USER_NAME:
      return Object.assign({}, state, {
        name: action.name
      })
    default:
      return state
  }
}
