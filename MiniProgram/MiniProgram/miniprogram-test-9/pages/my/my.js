
Page({

  /**
   * 页面的初始数据
   */
  data: {
    hasUserInfo: false,
    userInfo: null,
    classics: [],
    myBooksCount: 0,
    likeData:null
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    
  },
  onShow: function (options) {
    let likeData = wx.getStorageSync('likes')
    this.setData({
      likeData: likeData
    })
  },

  // onShow:function(options){

  // },

  getMyBookCount() {
    bookModel.getMyBookCount(data => {
      this.setData({
        myBooksCount: data.count
      })
    })
  },

  hasGottenUserInfo: function () {
    wx.getSetting({
      success: (data) => {
        if (data.authSetting['scope.userInfo']) {
          wx.getUserInfo({
            success: (data) => {
              this.setData({
                hasUserInfo: true,
                userInfo: data.userInfo
              })
            }
          })
        } else {
          this.setData({
            hasUserInfo: false
          })
        }
      }
    })
  },

  // 获取用户信息
  onGetUserInfo: function (event) {
    let userInfo = event.detail.userInfo
    if (userInfo) {
      this.setData({
        hasUserInfo: true,
        userInfo: userInfo
      })
    }
  },

  getMyFavor: function () {
    classicModel.getMyFavor((data) => {
      this.setData({
        classics: data
      })
    })
  },

  onPreviewTap: function (event) {
    wx.navigateTo({
      url: '/pages/classic-detail/index?cid=' + event.detail.cid + '&type=' + event.detail.type
    })
  },
  onJumpToAbout: function (event) {
    wx.navigateTo({
      url: '/pages/about/about',
    })
  },

  onStudy: function (event) {
    wx.navigateTo({
      url: '/pages/course/course',
    })
  },

  onShareAppMessage() {

  },

  // 通过点击喜欢的页面跳转到详情界面
  goDetail:function(event){
    let events = event.currentTarget.dataset
    if(events.inf.type=="图书"){
    console.log(event)
    wx.navigateTo({
      url: '/pages/detail/detail?bid='+events.inf.id
    })
    }
    else if (events.inf.type == "电影") {
      console.log(event)
      wx.switchTab({
        url: '/pages/classic/classic'
      })
    }
    
  }
})