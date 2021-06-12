<template>
  <div>
    <h2 class="Mytitle">My Post</h2>
    <div class="post-flex-container">
      <MyPostInfo
        v-for="post in post_list"
        :key="post.id" 
        :post="post"
        :like="post.like_count"
        :comment="post.comment_count"
      />
    </div>
  </div>
</template>

<script>
import MyPostInfo from './MyPostInfo.vue'

export default {
  name: 'MyPostList',
  components: {
    MyPostInfo,
  },
  props: {
    post_list: {
      type: Array,
    }
  },
}
</script>

<style>
.Mytitle {
  margin: 50px 0 20px 0;
}
.post-flex-container {
  display: flex;
  flex-wrap: wrap;
  margin: 0 5vw 0 16vw;
}
</style>