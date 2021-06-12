<template>
  <div>
    <h1 class="myPage">
      <span class="userName">{{user_name}}</span>'s page
    </h1>
    <div>
      <b-tabs class="my-tab" ontent-class="mt-3" align="center">
        <b-tab title="내가 본 영화" active @click="clickWatchList">
          <MyMovieWatchList 
            v-if="showWatchList"
            :watch_list="my_movie_watch_list"
            @checkwatch="getInfo"
          />
        </b-tab>
        <b-tab title="내가 좋아한 영화" @click="clickLikeList">
          <MyMovieLikeList 
            v-if="showLikeList"
            :like_list="my_movie_like_list"
            @checklike='getInfo'
          />
        </b-tab>
        <b-tab title="내가 쓴 리뷰" @click="clickReviewList">
          <MyReviewList 
            v-if="showReviewList"
            :review_list="my_review_list"
          />
        </b-tab>
        <b-tab title="내가 쓴 게시글" @click="clickPostList">
          <MyPostList 
            v-if="showPostList"
            :post_list="my_post"
          />
        </b-tab>
      </b-tabs>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MyMovieLikeList from '@/components/mypages/mymovies/MyMovieLikeList.vue'
import MyMovieWatchList from '@/components/mypages/mymovies/MyMovieWatchList.vue'
import MyReviewList from '@/components/mypages/myreviews/MyReviewList.vue'
import MyPostList from '@/components/mypages/myposts/MyPostList.vue'

export default {
  name: 'MyPage',
  components: {
    MyMovieLikeList,
    MyMovieWatchList,
    MyReviewList,
    MyPostList,
  },
  data() {
    return {
      user_name: '',
      my_movie_watch_list: [],
      my_movie_like_list: [],
      my_review_list: [],
      my_post: [],
      showWatchList: false,
      showLikeList: false,
      showReviewList: false,
      showPostList: false,
    }
  },
  methods: {
    getInfo() {
      axios({
        method: 'GET',
        url: `http://127.0.0.1:8000/accounts/mypage/`,
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },
      })
        .then((res)=>{
          this.user_name = res.data.user_name
          this.my_movie_like_list = res.data.my_movie_like_list
          this.my_movie_watch_list = res.data.my_movie_watch_list
          this.my_review_list = res.data.my_review_list.reverse()
          this.my_post = res.data.my_post.reverse()
        })
        .catch((err)=>{
          console.log(err)
        })
    },
    clickWatchList () {
      this.showWatchList = true
      this.showLikeList = false
      this.showReviewList = false
      this.showPostList = false
    },
    clickLikeList () {
      this.showWatchList = false
      this.showLikeList = true
      this.showReviewList = false
      this.showPostList = false
    },
    clickReviewList () {
      this.showWatchList = false
      this.showLikeList = false
      this.showReviewList = true
      this.showPostList = false
    },
    clickPostList () {
      this.showWatchList = false
      this.showLikeList = false
      this.showReviewList = false
      this.showPostList = true
    },
  },
  created() {
    this.getInfo()
    this.clickWatchList()
  }
}
</script>

<style>
.myPage {
  margin: 20px 0 50px 0
}
.userName {
  font-size: 50px;
  color: #F0A500;
}

.my-tab .nav-link {
  font-size: 22px;
  border: 1px solid rgba(0, 0, 0, 0.01);
  text-decoration: none;
  color: #F4F4F4;
  background-color: rgb(0, 0, 0, 0.01);
}

.my-tab .nav-link:hover,
.my-tab .nav-link.active {
  color: #F0A500;
  background-color: rgba(0, 0, 0, 0.01);
  border: 1px solid rgba(0, 0, 0, 0.01);
}
</style>