import fetch from 'isomorphic-fetch'


export const TODOS_REQUEST = 'TODOS_REQUEST'
export const TODOS_SUCCESS = 'TODOS_SUCCESS'
export const TODOS_FAILURE = 'TODOS_FAILURE'

export function loadTodos() {
  console.log("获取数据");
  return (dispatch, getState) => {
    dispatch(requestTodos());
    return fetch('/todo/api/v1.0/todos')
      .then(response =>
        response.json().then(json => ({ json, response }))
      ).then(({ json, response }) => {
          if (!response.ok) {
              dispatch(requestTodosFailure())
          }
          dispatch(requestTodosSuccess(json))
      })
  }

}

export function requestTodoList() {
  dispatch(requestTodos());
  return fetch('/todo/api/v1.0/todos')
    .then(response =>
      response.json().then(json => ({ json, response }))
    ).then(({ json, response }) => {
        console.log(json);
        if (!response.ok) {
            dispatch(requestTodosFailure())
        }
        console.log(json);
        dispatch(requestTodosSuccess(json))
    })
}

function requestTodos() {
  return {
    type: TODOS_REQUEST,
  }
}

function requestTodosFailure() {
  return {
    type: TODOS_FAILURE,
  }
}

function requestTodosSuccess(json) {
  console.log(json);
  return {
    type: TODOS_SUCCESS,
    data: json,
    receivedAt: Date.now()
  }
}
