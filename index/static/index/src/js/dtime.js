const dateDisplay = document.querySelector('#js-date')
const timeDisplay = document.querySelector('#js-time')

function loadDate () {
  const now = new Date()
  const year = now.getFullYear()
  const month = now.getMonth() + 1
  const date = now.getDate()
  let day
  switch (now.getDay()) {
    case 1:
      day = '월'
      break
    case 2:
      day = '화'
      break
    case 3:
      day = '수'
      break
    case 4:
      day = '목'
      break
    case 5:
      day = '금'
      break
    case 6:
      day = '토'
      break
    default:
      day = '일'
      break
  }
  dateDisplay.innerText = `${year}년 ${month < 10 ? `0${month}` : month}월 ${date < 10 ? `0${date}` : date}일 (${day})`
}

function loadTime () {
  const now = new Date()
  const hours = now.getHours()
  const minutes = now.getMinutes()
  const seconds = now.getSeconds()
  timeDisplay.innerText = `${hours < 10 ? `0${hours}` : hours}:${minutes < 10 ? `0${minutes}` : minutes}:${seconds < 10 ? `0${seconds}` : seconds}`
}

function init () {
  loadDate()
  loadTime()
  setInterval(loadTime, 1000)
}

init()
