<template>
  <div>
    <h2 class="Mytitle">My Review</h2>
    <div class="index">
      <div class="reviews-flex-container review-outer">
        <MyReviewInfo 
          v-for="(movie, i) in myPostMovies"
          :key="movie.id"
          :movie="movie"
          :myreview="review_list[i]"
          :like="movie['like']"
          :likeCount="movie['count']"
          @review-delete="reviewDelete"
        />
      </div>
    </div>
    

  </div>
</template>

<script>
import axios from 'axios'
import MyReviewInfo from './MyReviewInfo'

export default {
  name: 'MyReviewList',
  props: {
    review_list: {
      type: Array,
    }
  },
  components: {
    MyReviewInfo,
  },
  data () {
    return {
      myPostMovies: [],
    }
  },
  methods: {
    loadMovie() {
      axios({
        method: 'GET',
        url: `http://127.0.0.1:8000/accounts/mypage/mypost/`,
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },
      })
        .then(res=>{
          console.log(res.data['my_movies'])
          this.myPostMovies = res.data['my_movies'].reverse()
        })
        .catch(err=>{
          console.log(err)
        })
    },
    reviewDelete () {
      this.loadMovie()
    },
  },
  created () {
    this.loadMovie()
  },
}
</script>

<style>
.Mytitle {
  margin: 50px 0 20px 0;
}

.reviews-flex-container {
  display: flex;
  flex-wrap: wrap;
  margin: 0 5vw 0 17vw;
}
</style>