<template>
  <div class="myReviewBox">
    <div class="review-flex-container">
      <!-- 영화 포스터 -->
      <article class="myreviewItems">
        <div class="myreviewItem">
          <img
            class="myreviewPoster"
            :src="'https://image.tmdb.org/t/p/w500/'+movie.poster_path"
            alt=""
          >
          <!-- cap -->
          <div class="myreviewCaption">
            <!--상세내용을 담는 공간  -->
            <div class="myreview-cap-detail">
              <h4>{{ movie.title }}</h4>
              <p class='myreview-overview-limit myreview-cap-overview' v-if="movie.overview.length">
                {{ movie.overview }}
              </p>
              <p v-else>
                줄거리 미제공
              </p>
              <p>
                <i class="fas fa-heart fa-lg myreview-cap-like"></i>
                <span class="myreview-cap-like-count">
                  {{ this.likeCount }}명
                </span>
                이 좋아합니다!
              </p>
              <button class='myreview-detail-btn' @click="selectMovie"> 상세보기 </button>
            </div>
          </div>
          <!-- cap end -->
        </div>
      </article>

      <!-- 리뷰 -->
      <article class="myReview">
        <div class="my-star">
          <b-form-rating 
            inline 
            no-border 
            :value="myreview.star"
            size="lg"
            readonly
          ></b-form-rating>
        </div>
        <div class="oneline-flex">
          <span class="oneline-title">
            <i class="fas fa-hashtag"></i>
            한줄평:
          </span>
          <span class="oneline-comm oneline-comm-limit">{{ myreview.oneline_comment }}</span>
        </div>
        <p class="myreview-date">작성일: {{ myreview.created_at.substring(0, 10) }}</p>
      </article>

      <MovieDetailModal 
        :movie="movie"
        :popup="popup" 
        @hidemodal="popup=false"
        @review-delete="reviewDelete"
      />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieDetailModal from '@/components/movies/modals/MovieDetailModal'

export default {
  name: 'MyReviewreview',
  components: {
    MovieDetailModal,
  },
  props: {
    movie: {
      type: Object,
    },
    myreview: {
      type: Object,
    },
    like: {
      type: Boolean,
    },
    likeCount: {
      type: Number,
    }
  },
  data () {
    return {
      popup: false,
      isClick: false,
      reviews: [],
      reviewTitle: '필요없',
      star: '',
      onelineComment: '',
      hashTag: '',
      watched: false,
    }
  },
  methods: {
    selectMovie () {
      this.popup = !this.popup
      this.isClick = !this.isClick
      if (this.isClick) {
        this.loadReview()
        this.loadWatch()
      }
    },
    loadReview () {
      axios({
        method: 'GET',
        url: `http://127.0.0.1:8000/reviews/${this.movie.id}/movie/`,
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },
      })
        .then(res=>{
          this.reviews = res.data
        })
        .catch(err=>{
          console.log(err)
        })
    },
    loadWatch () {
      axios({
        method: 'GET',
        url: `http://127.0.0.1:8000/movies/${this.movie.id}/watch/`,
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },
      })
        .then(res=>{
          this.watched = res.data.watch
        })
        .catch(err=>{
          console.log(err)
        })
    },
    checkLike () {
      axios({
        method: 'POST',
        url: `http://127.0.0.1:8000/movies/${this.movie.id}/like/`,
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },
      })
        .then(res=>{
          this.like = res.data.like
          this.likeCount = res.data.count
        })
        .catch(err=>{
          console.log(err)
        })
    },
    checkWatch () {
      axios({
        method: 'POST',
        url: `http://127.0.0.1:8000/movies/${this.movie.id}/watch/`,
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },
      })
        .then(res=>{
          this.watched = res.data.watch
        })
        .catch(err=>{
          console.log(err)
        })
    },
    reviewCreate () {
      axios({
        method: 'POST',
        url: `http://127.0.0.1:8000/movies/${this.movie.id}/review/`,
        data: {
          title: this.reviewTitle,
          star: this.star,
          oneline_comment: this.onelineComment,
          hashtag: this.hashTag,
        },
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },
      })
        .then(()=>{
          this.loadReview()
        })
        .catch(err=>{
          console.log(err)
        })
    },
    reviewDelete() {
      this.$emit('review-delete')
    },
  },
}
</script>

<style >
.myReviewBox {
  border: 2px solid rgb(0, 0, 0, 0.6);
  margin: 10px;
  border-radius: 2rem;
}

.myreview-show-detail {
  color: #222;   
  text-decoration: none;
}
.myreviewItems {
  text-align: center;
  margin: 10px;
}

.myreviewItem {
  display: inline-block;
  position: relative;
}

.myreviewPoster,
.myreviewItem,
.myreviewCaption {
  width: 16rem; 
  height: 22rem;
  border-radius: 10%;
}

.myreviewCaption {
  background-color: #000;
  position: absolute;
  top: 0;
  left: 0;
  color: #fff;
  padding: 20px;
  box-sizing: border-box;
  padding-top: 25px;
  opacity: 0;
  transition: 0.4s;
}

.myreviewItem:hover .myreviewCaption {    
  opacity: 80%;
}

.myreview-cap-detail {
  padding-top: 25px;
}

.myreview-cap-detail > h4 {
  font-size: 22px;
  padding-bottom: 15px;
}

.myreview-cap-detail > .myreview-cap-overview {
  font-size: 16px;
  padding-bottom: 10px;
}

.myreview-cap-like {
  color: rgb(181, 25, 25);
}

.myreview-cap-like-count {
  color: rgb(181, 25, 25);
  font-size: 18px;
}

.myreview-detail-btn {
  font-size: 15px;
  color: #F4F4F4;
  background-color: rgb(0, 0, 0, 0.01);
  border: 1px solid #F4F4F4;
  height: 35px;
  padding: 0 6px;
  border-radius: 0.25rem;
}

.myreview-detail-btn:hover,
.myreview-detail-btn:active {
  border: 1px solid #F0A500;
  color: #F0A500;
}

.myreviewCaption .myreview-show-detail {
  color: #fff;
  font-size: 15px;
  background-color: #F0A500;
  padding: 5px;
  border-radius: 3px;
}

.myreviewCaption .myreview-show-detail:hover {
  background-color: #fff;
  color: #000;
}

.myreview-overview-limit {
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  line-height: 20px;
  max-height: 80px;
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical;
}

.review-flex-container {
  display: flex;
  flex-wrap: wrap;
  margin: 0 3vw 0 0;
}

.myReview {
  width: 16rem; 
  height: 22rem;
  margin-left: 15px;
  padding-top: 100px;
  text-align: left;
}

.my-star .form-control {
  color: #F0A500;
  background-color: rgba(0, 0, 0, 0.01);
  padding: 0;
}

.my-star .form-control:hover,
.my-star .form-control:active,
.my-star .form-control:focus {
  color: #F0A500;
  background-color: rgba(0, 0, 0, 0.01);
  padding: 0;
}

.oneline-flex {
  display: flex;
}

.oneline-title {
  font-size: 20px;
  width: 90px;
  min-width: 90px;
  color: #CF7500;
}

.oneline-comm {
  font-size: 25px;
  padding: 6px 0 0 7px;
}

.oneline-comm-limit {
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  line-height: 25px;
  max-height: 100px;
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical;
}

.myreview-date {
  margin: 12px 0 0 0;
  text-align: right;
}
</style>