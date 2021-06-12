<template>
  <div @click="openDetail">
    <div>
      <img :src="'https://image.tmdb.org/t/p/w500/'+movie.poster_path" width="50px" height="80px">
      {{ movie.title }}
    </div>

    <MovieDetailModal 
      :movie="movie"
      :popup="popup" 
      @hidemodal="popup=false"
      @checklike="loadLike"
    />
  </div>
</template>

<script>
import MovieDetailModal from '@/components/movies/modals/MovieDetailModal'

export default {
  components: {
    MovieDetailModal
  },
  props: {
    movie: {
      type: Object
    },
  },
  data() {
    return {
      popup: false,
    }
  },
  methods: {
    openDetail() {
      this.popup = !this.popup
    }
  }
}
</script>

<style>

</style>