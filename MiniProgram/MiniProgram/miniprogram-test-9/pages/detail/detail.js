import { ClassicModel } from '../../models/classic.js'
let classicModel = new ClassicModel()
Page({

  /**
   * 页面的初始数据
   */
  data: {
    book: null,
    comments: [],
    noComment: true,
    posting: false,
    like: false,
    count: 0,
    likeNum:false,
    num5:null
  },

  onLoad:function(options){
    console.log(options)
    classicModel.getPrevious('fanhui5',(res)=>{
      this.setData({
        book:res.data[options.bid - 1]
      })
      console.log(this.data.book)
    })
  },
  onLike: function (event) {
    this.setData({
      likeNum: !this.data.likeNum
    })
    if (this.data.likeNum) {
      console.log(this.data.classic)
      let likes = wx.getStorageSync('likes')
      console.log(this.data.book)
      likes.push({'id':this.data.book.id, "type": '图书', 'image': this.data.book.image, 'content': this.data.book.summary})
      wx.setStorageSync('likes', likes)
    }
    if (!this.data.likeNum) {
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