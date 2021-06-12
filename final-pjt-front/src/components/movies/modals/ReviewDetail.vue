<template>
  <li class="modal-liTag">
    <div v-if="!isUpdate">
      <!-- 평점 -->
      <div class="modal-user-star">
        <b-form-rating 
          inline 
          no-border 
          :value="review.star"
          size="lg"
          readonly
        ></b-form-rating>
        <span class="modal-user-star-val">{{ review.star }}</span>
      </div>
      <!-- 유저 리뷰 -->
      <div class="modal-user-review-flex">
        <div class="modal-review-flex">
          <!-- 유저이름 -->
          <span class="modal-user">
            {{ review.user_name }}
          </span>
          <!-- 한줄 평 -->
          <span class="modal-review">
            <i class="fas fa-hashtag fa-xs"></i>
            {{ review.oneline_comment }}
          </span>
        </div>
        <!-- 수정, 삭제 버튼 -->
        <div class="modal-review-btn-out" v-if="review.user===loginuser">
          <span @click="updateRequest" class="model-update-btn">수정</span>
          <span @click="reviewDelete" class="modal-del-btn">삭제</span>
        </div>
      </div>
    </div>
    <!-- update버튼 누르는 경우 -->
    <div v-else>
      <form @submit.prevent="reveiwUpdate">
        <div class="modal-upform-star">
          <b-form-rating 
            inline 
            no-border 
            v-model="star"
            size="lg"
          ></b-form-rating>
          <span class="modal-upform-star-val">{{ star }}</span>
        </div>
        <!-- form -->
        <div class="modal-user-review-flex">
          <div class="modal-review-flex">
            <!-- 유저이름 -->
            <label for="upreview" class="modal-user">
              {{ review.user_name }}
            </label>
            <!-- 한줄 평 -->
            <span class="modal-review-update">
              <i class="fas fa-hashtag fa-xs"></i>
              <input type="text" id="upreview" v-model="onelineComment">
            </span>
          </div>
          <!-- 수정, 삭제 버튼 -->
          <div class="modal-review-btn-out" v-if="review.user===loginuser">
            <button class="modal-upfrom-btn">작성</button>
          </div>
        </div>


      </form>
    </div>
  </li>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ReviewDetail',
  props: {
    review: {
      type: Object,
    },
    movieId: {
      type: Number,
    },
    loginuser: {
      type: Number
    },
  },
  data () {
    return {
      isUpdate: false,
      star: 0,
      onelineComment: '',
    }
  },
  methods: {
    reviewDelete () {
      axios({
        method: 'DELETE',
        url: `http://127.0.0.1:8000/reviews/${this.review.id}/movie/${this.movieId}/`,
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },
      })
        .then(()=>{
          this.$emit('review-delete')
        })
        .catch(err=>{
          console.log(err)
        })
    },
    reviewGet () {
      axios({
        method: 'GET',
        url: `http://127.0.0.1:8000/reviews/${this.review.id}/movie/${this.movieId}/`,
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },
      })
        .then(res=>{
          this.star = res.data.star
          this.onelineComment = res.data.oneline_comment
        })
        .catch(err=>{
          console.log(err)
        })
    },
    updateRequest () {
      this.isUpdate = true
      this.reviewGet()
    },
    reveiwUpdate() {
      axios({
        method: 'PUT',
        url: `http://127.0.0.1:8000/reviews/${this.review.id}/movie/${this.movieId}/`,
        data: {
          star: this.star,
          oneline_comment: this.onelineComment,
        },
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },
      })
        .then(()=>{
          this.isUpdate = false
          this.$emit('review-update')
        })
        .catch(err=>{
          console.log(err)
        })
    }
  },

}
</script>

<style>
.modal-liTag {
  margin-top: 20px;
}

.modal-user-star {
  display: flex;
  justify-items: center;
}

.modal-user-star .form-control {
  color: #CF7500;
  background-color: rgba(0, 0, 0, 0.01);
  padding: 0;
  height: 20px;
  min-height: 20px;
}

.modal-user-star .form-control:hover,
.modal-user-star .form-control:active,
.modal-user-star .form-control:focus {
  color: #CF7500;
  background-color: rgba(0, 0, 0, 0.01);
  padding: 0;
  /* outline: none; */
}

.modal-user-star-val {
  font-size: 16px;
  margin-left: 10px;
}

.modal-user-review-flex {
  display: flex;
  margin: 0 40px 0 0;
  justify-content: space-between;
}

.modal-review-flex {
  display: flex;
}

.modal-user {
  width: 65px;
  min-width: 65px;
  font-size: 23px;
}

.modal-review {
  font-size: 21px;
  margin: 5px 20px 0 10px;
  text-align: left;
}

.modal-review-btn-out {
  width: 85px;
  min-width: 85px;
  margin-top: 9px;
}

.model-update-btn,
.modal-del-btn {
  font-size: 16px;
  color: #F4F4F4;
  background-color: rgb(0, 0, 0, 0.01);
  border: 1px solid #F4F4F4;
  width: 40px;
  min-width: 40px;
  height: 45px;
  min-height: 45px;
  padding: 4px 4px;
  border-radius: 0.25rem;
}

.modal-del-btn {
  margin-left: 8px;
}

.model-update-btn:hover,
.model-update-btn:active {
  border: 1px solid #F0A500;
  color: #F0A500;
}

.modal-del-btn:hover,
.modal-del-btn:active {
  border: 1px solid #ae0f0f;
  color: #ae0f0f;
}

.modal-review-update {
  font-size: 21px;
  margin: 5px 20px 0 10px;
  text-align: left;
}

.modal-review-update input {
  margin-left: 10px;
  width: 480px;
}

.modal-upform-star {
  display: flex;
  justify-items: center;
}

.modal-upform-star .form-control {
  color: #CF7500;
  background-color: rgba(0, 0, 0, 0.01);
  padding: 0;
  height: 20px;
  min-height: 20px;
}

.modal-upform-star .form-control:hover,
.modal-upform-star .form-control:active,
.modal-upform-star .form-control:focus {
  color: #CF7500;
  background-color: rgba(0, 0, 0, 0.01);
  padding: 0;
}

.modal-upform-star-val {
  font-size: 16px;
  margin-left: 10px;
}

.modal-upform-review {
  display: flex;
  font-size: 20px;
  margin: 5px 20px 0 10px;
  text-align: left;
}

.modal-upform-review label{
  font-size: 18px;
}

.modal-upform-ti {
  width: 300px;
  margin-left: 10px;
}

.modal-upform-ti input,
.modal-upform-ti input:hover,
.modal-upform-ti input:active,
.modal-upform-ti input:visited {
  font-size: 19px;
  background-color: rgb(0, 0, 0, 0.01);
  width: 84%;
  display: inline;
  border: 1px solid #716f6f;
  color: #F4F4F4;
}

.modal-upfrom-ti input:focus {
  background-color: rgb(0, 0, 0, 0.01);
  color: #F4F4F4;
  outline: none;
}

.modal-upfrom-btn-t {
  padding-left: 3px;
}

.modal-upfrom-btn {
  font-size: 15px;
  color: #F4F4F4;
  background-color: rgb(0, 0, 0, 0.01);
  border: 1px solid #716f6f;
  width: 36px;
  min-width: 36px;
  height: 35px;
  min-height: 35px;
  padding: 4px 4px;
  margin-bottom: 2px;
  border-radius: 0.25rem;
}

.modal-upfrom-btn:hover,
.modal-upfrom-btn:active {
  border: 1px solid #F0A500;
  color: #F0A500;
}
</style>