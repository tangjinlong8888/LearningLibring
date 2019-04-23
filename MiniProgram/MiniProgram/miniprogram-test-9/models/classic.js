
// 经常用到的请求类,引用了配置文件的一些配置信息

import {HTTP} from '../util/http.js'

class ClassicModel extends HTTP{
  getLatest(sCallback){
    this.request({
      url:'fanhui1/',
      success:(res)=>{
        sCallback(res)
      }
    })
  }
  getPrevious(index,sCallback){
    this.request({
      url:index,
      success: (res) => {
        sCallback(res)
      }
    })
  }

}

export {ClassicModel}