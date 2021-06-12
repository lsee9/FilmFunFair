<template>
  <div>
    <h1 class="Mytitle">Update Post</h1>
    <section class="update-form-flex">
      <form @submit.prevent="updatePost">
        <div class="post-update-ti">
          <label for="updateTitle" class="form-label update-label">제목</label>
          <input 
            type="text" 
            class="form-control" 
            id="updateTitle"
            v-model="title"
          >
        </div>
        <div class="post-update-con">
          <label for="content" class="form-label update-label">내용</label>
          <textarea 
            class="form-control" 
            id="content" 
            rows="3"
            v-model="content"
          >
          </textarea>
        </div>
        <!-- 제출 버튼 -->
        <div class="update-btn">
          <span class="update-post-btn-t">
            <button class="update-post-btn">수정</button>
          </span>
          <span>
            <button class="back-post-btn" @click="goCommuPost(postId)">back</button>
          </span>
        </div>
      </form>
    </section>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'CommunityUpdate',
  props: {
    postId: {
      type: String
    }
  },
  data () {
    return {
      title: '',
      content: '',
    }
  },
  methods: {
    getPost() {
      axios({
        url: `http://127.0.0.1:8000/communities/${this.postId}/`,
        method: 'GET',
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },             
      })
        .then((res)=>{
          this.title = res.data.title
          this.content = res.data.content
        })
        .catch((err)=>{
          console.log(err)
        })
    },
    updatePost () {
      axios({
        url: `http://127.0.0.1:8000/communities/${this.postId}/`,
        method: 'PUT',
        data: {
          title: this.title,
          content: this.content,
        },
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },        
      })
        .then(()=>{
          const strPostId = this.postId + ""
          this.$router.push({ name: 'CommunityDetail', params: {postId: strPostId}})
        })
        .catch((err)=>{
          console.log(err)
        })
    },
    goCommuPost (postId) {
      const strPostId = postId + ""
      this.$router.push({ name: 'CommunityDetail', params: {postId:strPostId} })
    },
  },
  created() {
    this.getPost()
  }

}
</script>

<style>
.Mytitle {
  margin: 50px 0 20px 0;
}

.update-form-flex {
  display: flex;
  flex-wrap: wrap;
  margin: 0 30vw;
  padding-top: 10px;
  flex-direction: column;
}
.update-form-flex label {
  font-size: 20px;
}

.update-label {
  display: flex;
}

.post-update-ti input,
.post-update-con textarea {
  font-size: 18px;
  background-color: rgb(0, 0, 0, 0.01);
  border: 1px solid #F4F4F4;
  color: #F4F4F4;
}

.post-update-con {
  padding-top: 10px;
}

.post-update-con textarea {
  height: 250px;
}

.post-update-ti input:focus,
.post-update-con textarea:focus {
  background-color: rgb(0, 0, 0, 0.01);
  color: #F4F4F4;
  box-shadow: none;
  border: 1px solid #F4F4F4;
}

.update-btn {
  display: flex;
  flex-direction: row-reverse;
  padding-top: 10px;
}

.back-post-btn {
  font-size: 16px;
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

.update-post-btn-t {
  padding-left: 10px;
}

.update-post-btn {
  font-size: 16px;
  color: #F4F4F4;
  background-color: rgb(0, 0, 0, 0.01);
  border: 1px solid #F4F4F4;
  height: 30px;
  padding: 0 6px;
  border-radius: 0.25rem;
}

.update-post-btn:hover,
.update-post-btn:active {
  border: 1px solid #F0A500;
  color: #F0A500;
}

</style>