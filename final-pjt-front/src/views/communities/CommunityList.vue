<template>
  <div>
    <h1 class="Mytitle">Our PlayGround</h1>
    
    <!-- 글 작성 버튼 -->
    <div class="table-btn">   
      <button @click="postCreate"><span class="btn-space">글 작성</span></button>
    </div>

    <!-- 게시글 -->
    <div class="commu-total-flex-container">
      <div 
        v-for="post in posts"
        :key="post.id"
        @click="clickPost(post.id)"
      >
        <div class="commu-post-box">
          <article class="commu-one-post">
            <!-- 번호, 제목 -->
            <p class="commu-post-num-user">
              <span class="commu-post-num">No. {{ post.id }}</span>
              <span class="commu-post-user">
                <i class="far fa-user commu-user-icon"></i>
                {{ post.user_name }}
              </span>
            </p>
            <p class="commu-post-title commu-post-title-limit">
              {{ post.title }}
            </p>
            <!-- 등록일 -->
            <div class="commu-post-date">
              <p>등록일: {{ post.created_at.substring(0, 10) }}</p>
              <p>수정일: {{ post.updated_at.substring(0, 10) }}</p>
            </div>
          </article>
        </div>
      </div>
    </div>

    <!-- 로딩 스피너 -->
    <div v-if="!pageEnd" class="text-center my-3 commu-loading">
      <b-spinner
        variant="warning"
        style="width: 3rem; height: 3rem;"
      ></b-spinner>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'CommunityList',
  data() {
    return {
      posts: [],
      post: '',
      page: 1,
      pageEnd: false,
    }
  },
  methods: {
    postCreate() {
      this.$router.push({ name: 'CommunityCreate' })
    },
    getPosts() {
      axios({
        method: 'GET',
        url: 'http://127.0.0.1:8000/communities/main/',
        params: {
          p: this.page,
        },
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },        
      })
        .then((res)=>{
          this.posts.push(...res.data)
        })
        .catch((err)=>{
          console.log(err)
        })      
    },
    clickPost(postId) {
      const strPostId = postId + ""
      this.$router.push({ name: 'CommunityDetail', params: {postId:strPostId} })
    },
    linkGen(pageNum) {
      console.log(pageNum)
    }
  },
  created() {
    this.getPosts()
    document.addEventListener('scroll', ()=>{
      const {scrollTop, clientHeight, scrollHeight} = document.documentElement
      if (scrollHeight - scrollTop === clientHeight) {
        if (this.posts[this.posts.length-1].id === 1) {
          console.log('endpage')
          this.pageEnd = true
        } else {
          this.page += 1
          this.getPosts()
        }
      }
    })    
  }
}
</script>

<style>
.Mytitle {
  margin: 50px 0 20px 0;
}

.commu-total-flex-container {
  display: flex;
  flex-wrap: wrap;
  margin: 0 17vw 0 15vw;
  padding-top: 20px;
}

.commu-post-box {
  border: 2px solid rgb(0, 0, 0, 0.6);
  margin: 15px;
  width: 18rem;
  height: 17rem;
  border-radius: 1.5rem;
}

.commu-post-box:hover,
.commu-post-box:active,
.commu-post-box:focus {
  color: #CF7500;
  border-color: #CF7500;
}

.commu-one-post {
  margin: 40px 30px 33px 30px;
  width: 14rem;
}

.commu-post-num-user {
  display: flex;
  justify-content: space-between;
}

.commu-post-num {
  font-size: 18px;
  margin: 0;
}

.commu-post-user {
  font-size: 20px;
}

.commu-user-icon {
  margin-right: 2px;
}

.commu-post-title {
  font-size: 24px;
  margin-top: 30px;
}

.commu-post-title-limit {
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  line-height: 25px;
  max-height: 60px;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
}

.commu-post-date {
  margin-top: 30px;
}

.commu-post-date p {
  margin: 0;
  font-size: 16px;
}

.table-btn {
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  margin: 0 18.5vw;
}

.table-btn > button,
.table-btn button:visited {
  font-size: 16px;
  color: #F4F4F4;
  background-color: rgb(0, 0, 0, 0.01);
  border: 1px solid #F4F4F4;
  border-radius: 0.25rem;
  height: 35px;
  padding: 0 6px;
}

.table-btn button:hover,
.table-btn button:active {
  background-color: rgb(0, 0, 0, 0.01);
  border: 1px solid #F0A500;
  color: #F0A500;
}

</style>