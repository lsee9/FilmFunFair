<template>
  <div class="postBox" @click="clickPost(post.id)">
    <article class="myPost">
      <p class="postTitle postTitle-limit">{{ post.title }}</p>
      <div class="mypost-info-to">
        <div class="mypage-post-date">
            <p>작성일</p>
            <p>{{ post.created_at.substring(0, 10) }}</p>
        </div>
        <div class="postInfo">
          <span class="postLike"><i class="fas fa-heart fa-lg"></i> {{ like }}</span>
          <span class="postComm"><i class="far fa-comment-dots fa-lg"></i> {{ comment }}</span>
        </div>
      </div>
    </article>
  </div>
</template>

<script>
export default {
  name: 'MyPostInfo',
  props: {
    post: {
      type: Object,
    },
    like: {
      type: Number,
    },
    comment: {
      type: Number,
    },
  },
  methods: {
    clickPost(postId) {
      const strPostId = postId + ""
      this.$router.push({ name: 'CommunityDetail', params: {postId:strPostId} })
    },
  },
}
</script>

<style>
.postBox {
  border: 2px solid rgb(0, 0, 0, 0.6);
  margin: 20px;
  width: 18rem;
  height: 12rem;
  border-radius: 1rem;
}

.postBox:hover,
.postBox:active {
  border: 2px solid #CF7500;
  color: #CF7500;
}

.myPost {
  margin: 35px 30px 33px 30px;
  width: 14rem;
}

.postTitle {
  font-size: 25px;
}

.postTitle-limit {
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  line-height: 25px;
  max-height: 60px;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;
}

.mypost-info-to {
  display: flex;
  justify-content: space-between;
  margin-top: 50px;
}

.postInfo {
  font-size: 18px;
  margin-top: 20px;
}

.postLike {
  color: rgb(181, 25, 25);
  margin: 0 3px;
}

.postComm {
  color: rgb(32, 114, 142);
  margin: 0 5px;
}

.mypage-post-date {
  display: flex;
  flex-direction: column;
  text-align: left;
}

.mypage-post-date p {
  margin: 0;
}

</style>