<template>
  <div>
    <h1 class="Mytitle">New Post</h1>
    <section class="create-form-flex">
      <form @submit.prevent="post">
        <div class="post-create-ti">
          <label for="createTitle" class="form-label create-label">제목</label>
          <input 
            type="text" 
            class="form-control" 
            id="createTitle"
            v-model="title"
          >
        </div>
        <div class="post-create-con">
          <label for="content" class="form-label create-label">내용</label>
          <textarea 
            class="form-control" 
            id="content" 
            rows="3"
            v-model="content"
          >
          </textarea>
        </div>
        <div class="create-btn">
          <span class="create-post-btn-t">
            <button class="create-post-btn">작성</button>
          </span>
          <span>
            <button class="back-post-btn" @click="goCommuList">목록</button>
          </span>
        </div>
      </form>
    </section>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'CommunityCreate',
  data () {
    return {
      title: '',
      content: '',
    }
  },
  methods: {
    post () {
      axios({
        url: 'http://127.0.0.1:8000/communities/main/',
        method: 'POST',
        data: {
          title: this.title,
          content: this.content,
        },
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },        
      })
        .then((res)=>{
          const strPostId = res.data.id + ""
          this.$router.push({ name: 'CommunityDetail', params: {postId: strPostId}})
        })
        .catch((err)=>{
          console.log(err)
        })
    },
    goCommuList () {
      this.$router.push({ name: 'CommunityList'})
    },
  },

}
</script>

<style>
.Mytitle {
  margin: 50px 0 20px 0;
}

.create-form-flex {
  display: flex;
  flex-wrap: wrap;
  margin: 0 30vw;
  padding-top: 10px;
  flex-direction: column;
}
.create-form-flex label {
  font-size: 20px;
}

.create-label {
  display: flex;
}

.post-create-ti input,
.post-create-con textarea {
  font-size: 18px;
  background-color: rgb(0, 0, 0, 0.01);
  border: 1px solid #F4F4F4;
  color: #F4F4F4;
}

.post-create-con {
  padding-top: 10px;
}

.post-create-con textarea {
  white-space: pre-line;
  height: 250px;
}

.post-create-ti input:focus,
.post-create-con textarea:focus {
  background-color: rgb(0, 0, 0, 0.01);
  color: #F4F4F4;
  box-shadow: none;
  border: 1px solid #F4F4F4;
}

.create-btn {
  display: flex;
  flex-direction: row-reverse;
  padding-top: 10px;
}

.back-post-btn {
  font-size: 15px;
  color: #F4F4F4;
  background-color: rgb(0, 0, 0, 0.01);
  border: 1px solid #F4F4F4;
  height: 30px;
  padding: 0 6px;
  border-radius: 0.25rem;
}

.back-post-btn:hover,
.back-post-btn:active {
  border: 1px solid #F0A500;
  color: #F0A500;
}

.create-post-btn-t {
  padding-left: 10px;
}

.create-post-btn {
  font-size: 15px;
  color: #F4F4F4;
  background-color: rgb(0, 0, 0, 0.01);
  border: 1px solid #F4F4F4;
  height: 30px;
  padding: 0 6px;
  border-radius: 0.25rem;
}
.create-post-btn:hover,
.create-post-btn:active {
  border: 1px solid #F0A500;
  color: #F0A500;
}
</style>