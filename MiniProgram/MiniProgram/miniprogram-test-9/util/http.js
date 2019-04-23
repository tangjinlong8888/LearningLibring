// 发送http请求


import {config} from '../config.js'

const tips = {
  200:'',
  202:'',
  1:"抱歉,出现未知错误!"

}

class HTTP{
  
  request(params){
    if(!params.method){
      params.method="GET"
    }
    wx.request({
      url: config.api_base_url + params.url,
      success:(res)=>{
        let code=res.statusCode.toString()
        if(code.startsWith('2')){
          params.success(res)
        }
        else{
          let error_code = res.data.statusCode
          this._show_error(error_code)
        }
      },
      fail:(err)=>{
        this._show_error(1)
      }
    })
  }

  _show_error(error_code){
    wx.showToast({
      title: '错误',
      icon: 'none',
      duration: 2000
    })

  }
}
export {HTTP}