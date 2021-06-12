<template>
  <div>
    <!-- 게시글 제목 -->
    <div class="commu-detail-flex-container">
      <h4 class="Detailtitle" @click="mainBack">
        <i class="fas fa-angle-left fa-sm"></i>
        <span class="detail-back-btn">Back</span>
        <span>Our PlayGround</span> 
      </h4>
    </div>

    <!-- 게시글 내용 -->
    <div class="post-title-flex-container">
      <p class="post-ti-no">No. {{ post.id }} <span class="post-title-sm">제목:</span></p>
      <h3 class="post-title">{{ post.title }}</h3>
    </div>
    <hr class="my-hr">

    <!-- 유저 이름과 날짜 -->
    <div class="post-user-flex-container">
      <div class="user">
        <i class="fas fa-user-circle fa-2x"></i>
        <span>{{ post.user_name }}</span>
      </div>
      <div>
        <p class="post-date">등록일: {{ post.created_at.substring(0, 10) }}</p>
        <p class="post-update">수정일: {{ post.updated_at.substring(0, 10) }}</p>
      </div>
    </div>

    <!-- 게시글 내용 -->
    <div class="post-cont-flex-container cont-box">
      <p class="post-cont">
        {{ post.content }}
      </p>
    </div>

    <!-- 좋아요, 취소 업데이트버튼 -->
    <div class="post-user-flex-container">
      <div class="cont-like">
        <i v-if="!isLike" @click="like" class="far fa-heart fa-lg empty-heart"></i>
        <i v-if="isLike" @click="like" class="fas fa-heart fa-lg cont-heart"></i>
        <span>{{likeCount}} 명이 좋아합니다.</span>
      </div>
      <div class="post-btn">
        <span v-if="post.user_name===loginusername">
          <button class="up-btn" @click="updatePost">수정</button>
        </span>
        <span v-if="post.user_name===loginusername" class="del-btn-o">
          <button class="del-btn" @click="deletePost">삭제</button>
        </span>
      </div>
    </div>
    <hr class="my-hr-section">

    <!-- 댓글 폼 -->
    <section class="comm-form-flex">
      <form @submit.prevent="createComment">
        <div class="post-comm-ti">
          <label for="createcomm" class="form-label comm-label">댓글</label>
          <div class="comm-input">
            <input 
              type="text" 
              class="form-control" 
              id="createcomm"
              v-model="commentInput"
            >
            <span class="comm-btn-t">
              <button class="comm-btn">작성</button>
            </span>
          </div>
        </div>
      </form>
    </section>

    <!-- 댓글 -->
    <CommunityCommentList
      v-for="comment in comments"
      :key=comment.id
      :comment=comment
      :postId="postId"
      @need-refresh="getPost"
      :loginusername="loginusername"
    />
  </div>
</template>

<script>
import axios from 'axios'
import CommunityCommentList from '@/components/communities/CommunityCommentList.vue'

export default {
  name: 'CommunityDetail',
  props: {
    postId: {
      type: String
    }
  },
  components: {
    CommunityCommentList
  },
  data() {
    return {
      post: {},
      commentInput: '',
      comments: [],
      isLike: false,
      likeCount: 0,
      loginusername: '',
    }
  },
  methods: {
    getLoginUser(token) {
      const base64Url = token.split('.')[1];
      const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
      const jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c) {
          return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
      }).join(''));

      return JSON.parse(jsonPayload).username;
    },
    getPost() {
      axios({
        url: `http://127.0.0.1:8000/communities/${this.postId}/`,
        method: 'GET',
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },             
      })
        .then((res)=>{
          this.post = res.data
          this.comments = res.data.post_comment.reverse()
          this.loginusername = this.getLoginUser(`JWT ${localStorage.getItem('jwt')}`)
        })
        .catch((err)=>{
          console.log(err)
        })
    },
    mainBack () {
      this.$router.push({ name: 'CommunityList' })
    },
    updatePost() {
      const strPostId = this.postId + ""
      this.$router.push({ name: 'CommunityUpdate', params: {postId:strPostId} })
    },
    deletePost() {
      axios({
        url: `http://127.0.0.1:8000/communities/${this.postId}/`,
        method: 'DELETE',
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },             
      })
        .then(()=>{
          this.$router.push({ name: 'CommunityList' })
        })
        .catch((err)=>{
          console.log(err)
        })
    },
    createComment() {
      axios({
        url: `http://127.0.0.1:8000/communities/${this.postId}/comment/`,
        method: 'POST',
        data: {
          text: this.commentInput
        },
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },        
      })
        .then(()=>{
          this.getPost()
          this.commentInput = ''
        })
        .catch((err)=>{
          console.log(err)
        })
    },
    getLike() {
      axios({
        url: `http://127.0.0.1:8000/communities/${this.postId}/like/`,
        method: 'GET',
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },   
      })
        .then((res)=>{
          this.isLike = res.data.like
          this.likeCount = res.data.count
        })
        .catch((err)=>{
          console.log(err)
        })
    },
    like() {
      axios({
        url: `http://127.0.0.1:8000/communities/${this.postId}/like/`,
        method: 'POST',
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },   
      })
        .then((res)=>{
          this.isLike = res.data.like
          this.likeCount = res.data.count
          this.getPost()
        })
        .catch((err)=>{
          console.log(err)
        })
    }
  },
  created() {
    this.getLike()
    this.getPost()
  },
}
</script>

<style>
.commu-detail-flex-container {
  display: flex;
  flex-wrap: wrap;
  margin: 0 15vw 20px 17vw;
  padding-top: 10px;
}
.detail-back-btn {
  font-size: 18px;
  padding: 0 5px;
}
.Detailtitle {
  margin: 20px 0 20px 0;
  justify-content: end;
}
.Detailtitle:hover {
  color: #F0A500;
}

.post-title-flex-container {
  display: flex;
  flex-wrap: wrap;
  margin: 0 20vw;
  padding-top: 10px;
}
.post-ti-no {
  width: 93px;
  height: 24px;
}
.post-title-sm {
  padding-left: 4px;
}
.post-title {
  padding-left: 5px;
}
.my-hr {
  margin: 0 20vw;
  border: #F4F4F4;
}

.post-user-flex-container {
  display: flex;
  flex-wrap: wrap;
  margin: 0 20vw;
  padding-top: 10px;
  justify-content: space-between;
}
.user,
.cont-like {
  padding-left: 30px;
}
.user > span {
  font-size: 22px;
  margin: 0 5px 0 5px;
}
.user {
  padding-top: 7px;
}
.post-date {
  font-size: 13px;
  padding-top: 8px;
  padding-right: 35px;
  margin-bottom: 0;
}
.post-update {
  font-size: 13px;
  padding-right: 35px;
  margin-bottom: 6px;
}

.post-cont-flex-container {
  display: flex;
  flex-wrap: wrap;
  margin: 0 22vw;
  padding-top: 10px;
}
.cont-box {
  border: 2px solid #716f6f;
}
.post-cont {
  font-size: 18px;
  padding: 20px;
  margin-bottom: 10px;
}

.empty-heart:hover,
.empty-heart:active {
  color: rgb(181, 25, 25);
}

.cont-heart {
  color: rgb(181, 25, 25);
}

.cont-heart:active {
  color: #F4F4F4;
}

.cont-like > span {
  font-size: 16px;
  padding-left: 6px;
}

.post-btn {
  padding-right: 30px;
}

.del-btn-o {
  padding-left: 10px;
}

.del-btn {
  font-size: 15px;
  color: #F4F4F4;
  background-color: rgb(0, 0, 0, 0.01);
  border: 1px solid #F4F4F4;
  height: 30px;
  padding: 0 6px;
  border-radius: 0.25rem;
}

.del-btn:hover,
.del-btn:active {
  border: 1px solid #ae0f0f;
  color: #ae0f0f;
}

.up-btn {
  font-size: 15px;
  color: #F4F4F4;
  background-color: rgb(0, 0, 0, 0.01);
  border: 1px solid #F4F4F4;
  height: 30px;
  padding: 0 6px;
  border-radius: 0.25rem;
}
.up-btn:hover,
.up-btn:active {
  border: 1px solid #F0A500;
  color: #F0A500;
}

.my-hr-section {
  margin: 10px 20vw 0 20vw;
  border-top: 3px double #F4F4F4;
  background-color: rgb(0, 0, 0, 0.01);
}

.comm-form-flex {
  display: flex;
  margin: 0 35vw;
  padding-top: 10px;
  flex-direction: column;
}
.comm-form-flex label {
  font-size: 20px;
}

.comm-label {
  display: flex;
}

.post-comm-ti input {
  background-color: rgb(0, 0, 0, 0.01);
  width: 84%;
  display: inline;
  border: 1px solid #716f6f;
  color: #F4F4F4;
}

.post-comm-ti input:active,
.post-comm-ti input:focus {
  background-color: rgb(0, 0, 0, 0.01);
  color: #F4F4F4;
  border: 1px solid #716f6f;
  box-shadow: none;
}

.comm-btn-t {
  padding-left: 3px;
}

.comm-btn {
  font-size: 15px;
  color: #F4F4F4;
  background-color: rgb(0, 0, 0, 0.01);
  border: 1px solid #716f6f;
  width: 15%;
  min-width: 50px;
  height: 38px;
  padding: 0 6px;
  border-radius: 0.25rem;
}

.comm-btn:hover,
.comm-btn:active {
  border: 1px solid #F0A500;
  color: #F0A500;
}

.comment-flex-container {
  display: flex;
  flex-wrap: wrap;
  margin: 0 35vw;
  padding-top: 10px;
  flex-direction: column;
}
</style>