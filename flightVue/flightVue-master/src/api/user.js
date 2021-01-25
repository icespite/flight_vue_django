import request from '@/utils/request'

export function login(data) {
  return request({
    url: '/api/login',
    method: 'post',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    data
  })
}

export function getInfo() {
  return request({
    url: '/api/info/',
    method: 'get'
  })
}

export function getInform() {
  return request({
    url: '/user/getinform/',
    method: 'get'
  })
}

export function cofirmInform(id) {
  return request({
    url: '/user/confirmInform/',
    method: 'get',
    params: { id }
  })
}

export function logout() {
  return request({
    url: '/api/logout',
    method: 'post'
  })
}

// 得到所有地方
export function getAllLocation() {
  return request({
    url: '/user/getalllocation/',
    method: 'get'
  })
}

// 得到所有airline
export function getAllAirline() {
  return request({
    url: '/user/getallairline',
    method: 'get'
  })
}

// 根据flightnumber查询
export function searchByFlightNumber(flightNumber) {
  return request({
    url: '/user/searchbyflightnumber/',
    method: 'get',
    params: { flightNumber }
  })
}

export function buypost(id) {
  const param = new URLSearchParams()
  param.append('id', id)
  return request({
    url: '/user/buy',
    method: 'post',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    data: param
  })
}

export function buywaitpost(id) {
  const param = new URLSearchParams()
  param.append('id', id)
  return request({
    url: '/user/buywait',
    method: 'post',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    data: param
  })
}

export function getbuyinfo(id) {
  return request({
    url: '/user/getbuyinfo',
    method: 'get',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
  })
}

export function flightorder(list, order, column) {
  const param = new URLSearchParams()
  param.append('data', JSON.stringify(list))
  param.append('order', order)
  param.append('column', column)
  return request({
    url: '/user/flightorder',
    method: 'post',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    data: param
  })
}
export function cancelbuy(id, classify) {
  const param = new URLSearchParams()
  param.append('id', id)
  param.append('classify', classify)
  return request({
    url: '/user/cancelbuy',
    method: 'post',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    data: param
  })
}
export function searchflightless(time, classify, startid, endid) {
  const param = new URLSearchParams()
  param.append('time', time)
  param.append('classify', classify)
  param.append('startid', startid)
  param.append('endid', endid)
  return request({
    url: '/user/searchflightless',
    method: 'post',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    data: param
  })
}
