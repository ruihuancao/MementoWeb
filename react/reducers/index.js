import { combineReducers } from 'redux'
import * as ActionTypes from '../actions'


const selectedTodos = (
    state = {
    isFetching: false},
        action
) => {
  switch (action.type) {
    case ActionTypes.TODOS_REQUEST:
      return Object.assign({}, state, {
            isFetching: true
          })
    case ActionTypes.TODOS_SUCCESS:
          return  Object.assign({}, state, {
            isFetching: false,
            todos : action.data,
            lastUpdated: action.receivedAt
          })
    case ActionTypes.TODOS_FAILURE:
           return  Object.assign({}, state, {
            isFetching: false
          })
    default:
      return state
  }
}

const selectedTodoList = (
    state = {
        isFetching: false
    },
        action) =>
{
  switch (action.type) {
    case ActionTypes.TODOS_REQUEST:
      return Object.assign({}, state, {
            isFetching: true
          })
    case ActionTypes.TODOS_SUCCESS:
          return  Object.assign({}, state, {
            isFetching: false,
            todos : action.data,
            lastUpdated: action.receivedAt
          })
    case ActionTypes.TODOS_FAILURE:
           return  Object.assign({}, state, {
            isFetching: false
          })
    default:
      return state
  }
}


const rootReducer = combineReducers({
  selectedTodoList,
  selectedTodos
})

export default rootReducer
