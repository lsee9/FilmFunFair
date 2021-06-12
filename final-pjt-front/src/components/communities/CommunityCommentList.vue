<template>
  <div class="one-comm-flex-container">
    <div class="comm-user-flex">
      <span class="comm-user">
        {{ comment.user_name }}
        <i class="far fa-comment-dots fa-lg"></i>
      </span>
      <span class="comm-text">
        {{ comment.text }}
      </span>
    </div>
    <div class="comm-del-btn-o">
      <button v-if="comment.user_name===loginusername" class="comm-del-btn" @click="deleteComment">X</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  props: {
    comment: {
      type: Object
    },
    postId: {
      type: String
    },
    loginusername: {
      type: String
    }
  },
  methods: {
    deleteComment() {
      axios({
        url: `http://127.0.0.1:8000/communities/${this.postId}/comment/${this.comment.id}`,
        method: 'DELETE',
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },             
      })
        .then((res)=>{
          console.log(res)
          this.$emit('need-refresh')
        })
        .catch((err)=>{
          console.log(err)
        })
    }
  },
}
</script>

<style>
.one-comm-flex-container {
  display: flex;
  margin: 0 35vw;
  padding-top: 20px;
  justify-content: space-between;
}

.comm-user-flex {
  display: flex;
}

.comm-user {
  font-size: 18px;
  width: 80px;
  min-width: 80px;
}

.comm-text {
  font-size: 18px;
  margin: 0 10px 0 5px;
  text-align: left;
}

.comm-del-btn-o {
  margin-left: 2px;
  margin-right: 3px;
  width: 30px;
  min-width: 30px;
}

.comm-del-btn {
  font-size: 13px;
  color: #F4F4F4;
  background-color: rgb(0, 0, 0, 0.01);
  border: 1px solid #F4F4F4;
  width: 30px;
  min-width: 30px;
  height: 30px;
  min-height: 30px;
  padding: 0 6px;
  border-radius: 0.25rem;
}

.comm-del-btn:hover,
.comm-del-btn:active {
  border: 1px solid #ae0f0f;
  color: #ae0f0f;
}
</style>