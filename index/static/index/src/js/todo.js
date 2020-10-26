const TODOS_LS = 'todos'
const TODOSHOW_LS = 'todoShow'

const todoDisplay = document.querySelector('#js-todo')
const todoForm = todoDisplay.querySelector('form')
const todoCount = document.querySelector('#js-todoCount')
let todoCollapseDiv = document.querySelector('#collapseTodo')
let todoCollapseButton = document.querySelector('button[data-target="#collapseTodo"]')
let todoCollapse = localStorage.getItem(TODOSHOW_LS)

function showTodo (content, status) {
  const li = document.createElement('li')
  const checkButton = document.createElement('button')
  const todoSpan = document.createElement('span')
  const deleteButton = document.createElement('button')

  checkButton.innerText = '⬜'
  todoSpan.innerText = content
  deleteButton.innerText = '❌'

  if (status === '✅') {
    checkButton.innerText = '✅'
    todoSpan.classList.toggle('todo-done')
  }

  checkButton.addEventListener('click', handleChangeStatus)
  deleteButton.addEventListener('click', handleDeleteTodo)
  checkButton.classList.add('btn')
  deleteButton.classList.add('btn')
  todoSpan.classList.add('align-self-center')

  li.append(checkButton, todoSpan, deleteButton)

  li.classList.add('d-flex')
  li.classList.add('justify-content-between')
  li.classList.add('list-group-item')

  todoDisplay.appendChild(li)
}

function handleChangeStatus (event) {
  const parentLi = event.target.parentElement
  const adjSpan = parentLi.querySelector("span")
  const button = event.target
  const status = button.innerText

  if (status === '⬜') {
    button.innerText = '✅'
  } else {
    button.innerText = '⬜'
  }

  adjSpan.classList.toggle('todo-done')
  adjSpan.classList.toggle('text-secondary')
  saveTodos()
}

function handleDeleteTodo (event) {
  const parentLi = event.target.parentElement

  parentLi.remove()
  saveTodos()

}

function saveTodos () {
  const todoLis = todoDisplay.querySelectorAll('li')
  const todoArr = []
  let count = 0

  todoLis.forEach(todoLi => {
    const status = todoLi.querySelector('button').innerText
    const content = todoLi.querySelector('span').innerText

    todoArr.push({
      status,
      content
    })

    if (status === '⬜') {
      count++
    }
  })
  countTodos(count)
  const todoJSON = JSON.stringify(todoArr)

  localStorage.setItem(TODOS_LS, todoJSON)
}

function countTodos (count) {
  todoCount.innerText = count
}

function init () {
  const todoJSON = localStorage.getItem(TODOS_LS)
  if (todoCollapse === '0') {
    todoCollapseDiv.classList.remove('show')
  }

  if (todoJSON) {
    const todoArr = JSON.parse(todoJSON)

    todoArr.forEach(todo => {
      const { content, status } = todo

      showTodo(content, status)

    })
  }

  saveTodos()

  todoForm.addEventListener('submit', event => {
    event.preventDefault()
    const input = todoForm.querySelector('input')
    const content = input.value

    input.value = ''
    showTodo(content)
    saveTodos()

  })
  todoCollapseButton.addEventListener('click', event => {
    todoCollapse = todoCollapse !== '0' ? '0' : '1'
    localStorage.setItem(TODOSHOW_LS, todoCollapse)
  })
}

init()
