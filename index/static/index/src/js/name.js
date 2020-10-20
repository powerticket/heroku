const nameDisplay = document.querySelector('#js-name')
const nameForm = nameDisplay.querySelector('form')

const NAME_LS = 'name'

function saveName (name) {
  localStorage.setItem(NAME_LS, name)
}

function loadName (name) {
  nameDisplay.innerText = `${name}님, 환영합니다!`
}

function init () {
  const name = localStorage.getItem(NAME_LS)
  if (name) {
    loadName(name)
  } else {
    nameForm.addEventListener('submit', event => {
      event.preventDefault()
      const input = nameForm.querySelector('input')
      const name = input.value
      saveName(name)
      loadName(name)
    })
  }
}

init()
