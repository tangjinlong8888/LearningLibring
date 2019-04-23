// 导入自定义网络请求类
import { ClassicModel } from '../../models/classic.js'
let classicModel = new ClassicModel()
Page({

  /**
   * 页面的初始数据
   */
  data: {
    count: null,
    numm:null,
    likeNum:false
  },

  // 点击查看上一期
  onNext:function(){
    console.log(124567)
    let num1 = wx.getStorageSync('num1') - 1
    if (num1 < 1) {
      num1 = Number(this.data.numm)
    }
    wx.num1 = wx.setStorageSync('num1', num1)
    let num2 = `fanhui${num1}`
    console.log(num2)
    classicModel.getPrevious(num2, (res) => {
      this.setData({
        classic: res
      })
      console.log(res)
    })
  },
  
  // 点击查看下一期,加了一个循环
  onPrevious:function(){
    let num1 = wx.getStorageSync('num1') + 1
    if(num1>Number(this.data.numm)){
      num1 = 1
    }
    wx.num1 = wx.setStorageSync('num1', num1)
    let num2 = 'fanhui'+ num1
    console.log(num2)
    classicModel.getPrevious(num2,(res)=>{
      this.setData({
        classic:res
      })
    })
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    // 使用箭头函数,这样就可以在回调函数中使用this
    classicModel.getLatest((data)=>{
      this.setData({
        classic:data,
        numm:data.data.index,
      })
      wx.setStorageSync('likes',[])
      wx.setStorageSync('ni', [])
      wx.setStorageSync('num1', 1)
      console.log(this.data)
    })
    // console.log(this.data.test)
    // wx.request({
    //   url: 'http://127.0.0.1:8001/fanhui1/',
    //   success:function(event){

    //   }
    // })
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  },

  // 如果点击了喜欢按钮,就把喜欢的内容写入到缓存区中
  onLike: function (event) {
    this.setData({
      likeNum:!this.data.likeNum
    })
    if(this.data.likeNum){
      console.log(this.data.classic)
      let likes = wx.getStorageSync('likes')
      console.log(likes)
      likes.push({ "type": '电影', 'image': this.data.classic.data.url, 'content': this.data.classic.data.content })
      wx.setStorageSync('likes', likes)
    }
    if (!this.data.likeNum){
      console.log(this.data.classic)
      let likes = wx.getStorageSync('likes')
      console.log(likes)
      likes.pop()
      wx.setStorageSync('likes', likes)
    }
    // let ni = wx.getStorageSync('ni')
    // console.log(ni)
    // ni.push({'wo':123})
    // wx.setStorageSync('ni', ni)
    }

})