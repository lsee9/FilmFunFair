<template>
  <div class="movie-modal">
    <b-modal size="lg" ref="my-modal" hide-footer title="영화 상세 정보">
      <div>
        <div>
          <h2>{{ movie.title }}</h2>
          <!-- 포스터 및 유튜브영상 -->
          <div class="modal-movieInfo-flex">
            <img 
              :src="'https://image.tmdb.org/t/p/w500/'+movie.poster_path" 
              alt="movieposter"
              class="movie-modal-poster"
            >
            <div class="modal-movieInfo-left-flex">
              <MovieDetailPreview :movieTitle="movie.title" />
              <!-- 줄거리 -->
              <div class="modal-overview-part">
                <p class="modal-overview-title">&lt;줄거리&gt;</p>
                <p v-if="movie.overview.length" class="modal-overview">
                  {{ movie.overview }}
                </p>
                <p v-else class="modal-overview">
                  줄거리 미제공
                </p>
              </div>
            </div>
          </div>

          <!-- 좋아요, 봤어요 -->
          <div class="modal-movie-btn">
            <span class="modal-like">
              <i v-if="!like" @click="checkLike" class="far fa-heart fa-lg modal-empty-heart"></i>
              <i v-if="like" @click="checkLike" class="fas fa-heart fa-lg modal-cont-heart"></i>
              <span>{{ likeCount }}명</span>이 좋아합니다
            </span>
            <span>
              <button v-if="watched" @click="checkWatch" class="modalWatchedBtnAfter">봤어요!</button>
              <button v-if="!watched" @click="checkWatch" class="modalWatchedBtn">안봤어요</button>
            </span>
          </div>
          
          <!-- 평점 -->
          <div class="modal-movie-star">
            <span class="modal-star-rating">평점: </span>
            <b-form-rating 
              inline 
              no-border 
              :value="avg_star"
              readonly
            ></b-form-rating>
            <span class="modal-star-avg">{{ avg_star }}</span>
          </div>

          <hr>

          <section>
            <h4>
              <i class="fas fa-hashtag"></i>
              Oneline Comment
            </h4>

            <!-- 리뷰 등록 -->
            <form @submit.prevent="reviewCreate">
              <div class="modal-form-star">
                <b-form-rating 
                  inline 
                  no-border 
                  v-model="star"
                  size="lg"
                ></b-form-rating>
                <span class="modal-form-star-val">{{ star }}</span>
              </div>
              <div class="modal-form-review">
                <label for="Comment">리뷰: </label>
                <div class="modal-from-ti">
                  <input type="text" id="Comment" v-model="onelineComment">
                  <span class="modal-from-btn-t">
                    <button class="modal-from-btn">작성</button>
                  </span>
                </div>
              </div>
            </form>
            <ul v-if="reviews.length">
              <ReviewDetail 
                v-for="review in reviews" 
                :key="review.id"
                :review="review"
                :movieId="movie.id"
                :loginuser="loginuser"
                @review-delete="reviewDelete"
                @review-update="reviewUpdate"
              />
            </ul>
            <ul v-else>
              <li class="modal-empty-li">아직 등록된 리뷰가 없습니다:(</li>
            </ul>
          </section>
        </div>
      </div>

      <!-- 모달창 닫는 버튼 -->
      <b-button class="mt-2" button-size="sm" variant="warning" block @click="hideModal">Close</b-button>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios'
import ReviewDetail from './ReviewDetail'
import MovieDetailPreview from './MovieDetailPreview'

  export default {
    name: 'MovieDetailModal',
    components: {
      ReviewDetail,
      MovieDetailPreview,
    },
    data() {
      return {
        reviews: [],
        star: 0,
        avg_star: 0,
        onelineComment: '',
        like: false,
        likeCount: 0,
        watched: false,      
      }
    },
    props: {
      popup: Boolean,
      movie: Object,
      loginuser: Number,
    },
    methods: {
      showModal() {
        this.$refs['my-modal'].show()
      },
      hideModal() {
        this.$refs['my-modal'].hide()
        this.$emit('hidemodal')
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
            this.reviews = res.data.reviews.reverse()
            this.avg_star = res.data.avg_star
          })
          .catch(err=>{
            console.log(err)
          })
      },
      loadLike () {
        axios({
          method: 'GET',
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
            this.$emit('checklike')
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
            this.$emit('checkwatch')
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
            star: this.star,
            oneline_comment: this.onelineComment,
          },
          headers: {
            Authorization: `JWT ${localStorage.getItem('jwt')}`
          },
        })
          .then(()=>{
            this.star= ''
            this.onelineComment= ''
            this.loadReview()
          })
          .catch(err=>{
            console.log(err)
          })
      },
      reviewUpdate() {
        this.loadReview()
      },
      reviewDelete() {
        this.loadReview()
        this.$emit('review-delete')
      },
    },
    watch: {
      popup() {
        if (this.popup === true) {
          this.showModal()
          this.loadReview()
          this.loadLike()
          this.loadWatch()
        } else {
          this.hideModal()
        }
      }
    },
  }
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Fredoka+One&family=Jua&display=swap');

.modal{
  font-family: 'Fredoka One', cursive;
  font-family: 'Jua', sans-serif;
}

.modal .modal-content{
  background-color: rgb(0, 0, 0, 0.95);
  color: #F4F4F4;
}

.modal-header button {
  color: #F4F4F4;
  background-color: rgb(0, 0, 0, 0.01);
  border: 1px solid #716f6f;
  width: 40px;
  height: 40px;
  margin: 0;
  border-radius: 0.25rem;
}

.modal-header button:hover,
.modal-header button:active {
  border: 1px solid #F0A500;
  color: #F0A500;
}

.modal-movieInfo-flex {
  display: flex;
}

.movie-modal-poster {
  width: 19rem;
  min-width: 19rem;
  height: 95%;
  border: 1px solid #1e1b1b;
}

.modal-movieInfo-left-flex {
  display: flex;
  flex-direction: column;
  margin-left: 20px;
}

.modal-overview-part {
  margin-top: 10px;
  width: 440px;
  max-width: 440px;
}
.modal-overview-title {
  margin-bottom: 3px;
  font-size: 20px;
}
.modal-overview {
  font-size: 17px;
  margin: 0;
}

.modal-movie-btn {
  margin: 10px 0;
  display: flex;
  justify-content: center;
}

.modal-like {
  margin-right: 10px;
  margin-left: 100px;
}

.modal-empty-heart:hover,
.modal-empty-heart:active {
  color: rgb(181, 25, 25);
}

.modal-cont-heart {
  color: rgb(181, 25, 25);
}

.modal-cont-heart:active {
  color: #F4F4F4;
}

.modal-like > span {
  font-size: 17px;
  padding-left: 6px;
}

.modalWatchedBtn {
  font-size: 15px;
  color: #F4F4F4;
  background-color: rgb(0, 0, 0, 0.01);
  border: 1px solid #F4F4F4;
  height: 30px;
  padding: 0 6px;
  border-radius: 0.25rem;
}

.modalWatchedBtnAfter {
  font-size: 15px;
  color: #F0A500;
  background-color: rgb(0, 0, 0, 0.01);
  border: 1px solid #F0A500;
  height: 30px;
  padding: 0 6px;
  border-radius: 0.25rem;
}

.modalWatchedBtn:hover,
.modalWatchedBtn:active {
  color: #F0A500;
  border: 1px solid #F0A500;
}

.modal-movie-star {
  display: flex;
  justify-items: center;
}

.modal-star-rating {
  font-size: 16px;
}

.modal-movie-star .form-control {
  color: #F0A500;
  background-color: rgba(0, 0, 0, 0.01);
  padding: 0;
  font-size: 30px;
  height: 30px;
}

.modal-movie-star .form-control:hover,
.modal-movie-star .form-control:active,
.modal-movie-star .form-control:focus {
  color: #F0A500;
  background-color: rgba(0, 0, 0, 0.01);
  padding: 0;
}

.modal-star-avg {
  font-size: 22px;
  margin-left: 10px;
}

.modal-form-star {
  display: flex;
  justify-items: center;
}

.modal-form-star .form-control {
  color: #CF7500;
  background-color: rgba(0, 0, 0, 0.01);
  padding: 0;
  height: 20px;
  min-height: 20px;
}

.modal-form-star .form-control:hover,
.modal-form-star .form-control:active,
.modal-form-star .form-control:focus {
  color: #CF7500;
  background-color: rgba(0, 0, 0, 0.01);
  padding: 0;
}

.modal-form-star-val {
  font-size: 16px;
  margin-left: 10px;
}

.modal-form-review {
  display: flex;
  margin-top: 10px;
}

.modal-form-review label{
  font-size: 18px;
}

.modal-from-ti {
  width: 300px;
  margin-left: 10px;
}

.modal-from-ti input {
  font-size: 21px;
  background-color: rgb(0, 0, 0, 0.01);
  width: 84%;
  display: inline;
  border: 1px solid #716f6f;
  color: #F4F4F4;
}

.modal-from-ti input:focus {
  background-color: rgb(0, 0, 0, 0.01);
  color: #F4F4F4;
  outline: none;
}

.modal-from-btn-t {
  padding-left: 3px;
}

.modal-from-btn {
  font-size: 17px;
  color: #F4F4F4;
  background-color: rgb(0, 0, 0, 0.01);
  border: 1px solid #716f6f;
  width: 40px;
  min-width: 40px;
  height: 35px;
  min-height: 35px;
  padding: 4px 4px;
  margin-bottom: 2px;
  border-radius: 0.25rem;
}

.modal-from-btn:hover,
.modal-from-btn:active {
  border: 1px solid #F0A500;
  color: #F0A500;
}

.modal-empty-li {
  font-size: 20px;
  margin: 5px 20px 0 10px;
  text-align: left;
}

</style>