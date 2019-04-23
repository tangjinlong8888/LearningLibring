
// 导入并实例化请求类
import { ClassicModel } from '../../models/classic.js'
let classicModel = new ClassicModel()
Page({

  /**
   * 页面的初始数据
   */
  data: {
    searchPanel: false,
    books: Object,
    more: false
  },

  onReachBottom: function (event) {
    this.setData({
      more: random(16)
    })
  },
  onActivateSearch: function (event) {
    this.setData({
      searchPanel: true
    })
  },

  onCancel: function (event) {
    this.setData({
      searchPanel: false
    })
  },

  onShareAppMessage() {

  },
  /**
   * 生命周期函数--监听页面加载
   */

// 使用实例化的对象去请求数据
  onLoad: function (options) {
    classicModel.getPrevious('fanhui5', (res) => {
      this.setData({
        books: res.data
      })
      console.log(res)
    })
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

  }
})