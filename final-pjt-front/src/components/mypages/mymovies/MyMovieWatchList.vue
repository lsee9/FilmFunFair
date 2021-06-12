<template>
  <div>
    <h2 class="watch-title">Watched Movies</h2>
    <div class="index">
      <div class="mymovie-flex-container">
        <MyMovieInfo 
          v-for="movie in watch_list"
          :key="movie.id"
          :movie="movie"
          @checkwatch="checkwatch"
        />
      </div>
    </div>
  </div>
</template>

<script>
import MyMovieInfo from './MyMovieInfo'

export default {
  name: 'MyMovieWatchList',
  props: {
    watch_list: {
      type: Array,
    }
  },
  components: {
    MyMovieInfo,
  },
  methods: {
    checkwatch() {
      this.$emit('checkwatch')
    },
  },
}
</script>

<style>
.watch-title {
  margin: 50px 0 20px 0;
}

.mymovie-flex-container {
  display: flex;
  flex-wrap: wrap;
  margin: 0 7vw 0 15vw;
}
</style>