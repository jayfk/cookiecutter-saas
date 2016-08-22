import * as types from '../constants/actionTypes'
import {cookies} from '../util'

export function changeUserName(name){
  return {
    type: types.CHANGE_USER_NAME,
    name: name
  }
}

export function saveUser(user){
  fetch('http://localhost:8000/api/v1/user/', {
    method: 'PUT',
    credentials: 'same-origin',
    headers: {
      'X-CSRFToken': cookies.get("csrftoken"),
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(user)
  })
  return {
    type: types.SAVE_USER
  }
}

function requestUser() {
  return {
    type: types.REQUEST_USER
  }
}

function receiveUser(json) {
  return {
    type: types.RECEIVE_USER,
    user: json,
    receivedAt: Date.now()
  }
}

export function fetchUser() {
  return dispatch => {
    dispatch(requestUser())
    return fetch('http://localhost:8000/api/v1/user/', {credentials: 'same-origin'})
      .then(response => response.json())
      .then(json => dispatch(receiveUser(json)))
  }
}
