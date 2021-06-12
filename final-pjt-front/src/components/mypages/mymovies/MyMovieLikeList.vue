<template>
  <div>
    <h2 class="Mytitle">Liked Movies</h2>
    <div class="index">
      <div class="mymovie-flex-container">
        <MyMovieInfo 
          v-for="movie in like_list"
          :key="movie.id"
          :movie="movie"
          @checklike="checklike"
        />
      </div>
    </div>
  </div>
</template>

<script>
import MyMovieInfo from './MyMovieInfo'

export default {
  name: 'MyMovieLikeList',
  props: {
    like_list: {
      type: Array,
    }
  },
  components: {
    MyMovieInfo,
  },
  methods: {
    checklike() {
      this.$emit('checklike')
    }
  }
}
</script>

<style>
.Mytitle {
  margin: 50px 0 20px 0;
}

.mymovie-flex-container {
  display: flex;
  flex-wrap: wrap;
  margin: 0 7vw 0 15vw;
}
</style>