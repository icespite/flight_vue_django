import request from '@/utils/request'

export function modifyLocation(id, name) {
  const param = new URLSearchParams()
  param.append('id', id)
  param.append('name', name)
  return request({
    url: '/manage/modefylocation',
    method: 'post',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    data: param
  })
}

export function modifyAirline(id, name, identifier) {
  const param = new URLSearchParams()
  param.append('id', id)
  param.append('name', name)
  param.append('identifier', identifier)
  return request({
    url: '/manage/modefyairline',
    method: 'post',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    data: param
  })
}

export function addlocationpost(name) {
  const param = new URLSearchParams()
  param.append('name', name)
  return request({
    url: '/manage/addlocation',
    method: 'post',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    data: param
  })
}

export function deletelocationpost(id) {
  const param = new URLSearchParams()
  param.append('id', id)
  return request({
    url: '/manage/deletelocation',
    method: 'post',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    data: param
  })
}

export function deleteairlinepost(id) {
  const param = new URLSearchParams()
  param.append('id', id)
  return request({
    url: '/manage/deleteairline',
    method: 'post',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    data: param
  })
}
export function addairlinepost(name, identifier) {
  const param = new URLSearchParams()
  param.append('name', name)
  param.append('identifier', identifier)
  return request({
    url: '/manage/addairline',
    method: 'post',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    data: param
  })
}
export function modifyflightformpost(list) {
  const param = new URLSearchParams()
  param.append('list', JSON.stringify(list))
  return request({
    url: '/manage/modifyflight',
    method: 'post',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    data: param
  })
}

export function addflightformpost(list) {
  const param = new URLSearchParams()
  param.append('list', JSON.stringify(list))
  return request({
    url: '/manage/addflight',
    method: 'post',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    data: param
  })
}

export function cancelflight(id, classify) {
  const param = new URLSearchParams()
  param.append('id', JSON.stringify(id))
  param.append('classify', JSON.stringify(classify))
  return request({
    url: '/manage/cancelflight',
    method: 'post',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    data: param
  })
}
export function deleteflight(list) {
  const param = new URLSearchParams()
  param.append('list', JSON.stringify(list))
  return request({
    url: '/manage/deleteflight',
    method: 'post',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    data: param
  })
}
