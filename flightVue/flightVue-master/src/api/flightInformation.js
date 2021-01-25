import request from '@/utils/request'

export function searchFlight(data) {
  return request({
    url: '/user/search',
    method: 'post',
    data
  })
}
