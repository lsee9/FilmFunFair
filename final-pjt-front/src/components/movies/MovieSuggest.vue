<template>
  <div>
    <carousel-3d :width="310" :height="480" :space="300">
      <slide class='slideColor' :index="0" style="border-radius: 10%">
        <div v-if="movies.length > 0">
          <MovieDetail 
            :movie="movies[0]"
          />
        </div>
      </slide>
      <slide class='slideColor' :index="1" style="border-radius: 10%">
        <div v-if="movies.length > 0">
          <MovieDetail 
            :movie="movies[1]"
          />
        </div>
      </slide>
      <slide class='slideColor' :index="2" style="border-radius: 10%">
        <div v-if="movies.length > 0">
          <MovieDetail 
            :movie="movies[2]"
          />
        </div>
      </slide>
      <slide class='slideColor' :index="3" style="border-radius: 10%">
        <div v-if="movies.length > 0">
          <MovieDetail 
            :movie="movies[3]"
          />
        </div>
      </slide>
      <slide class='slideColor' :index="4" style="border-radius: 10%">
        <div v-if="movies.length > 0">
          <MovieDetail 
            :movie="movies[4]"
          />
        </div>
      </slide>
    </carousel-3d>

  </div>
</template>

<script>
import axios from 'axios'
import MovieDetail from '@/components/movies/MovieDetail'
import { Carousel3d, Slide } from 'vue-carousel-3d'

export default {
  name: 'MovieSuggest',
  components: {
    MovieDetail,
    Carousel3d,
    Slide,
  },
  data() {
    return {
      movies: [],
    }
  },
  methods: {
    getRecommendations() {
      axios({
        method: 'GET',
        url: 'http://127.0.0.1:8000/movies/recommendation/',
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },
      })
        .then((res)=>{
          this.movies = res.data
        })
        .catch((err)=>{
          console.log(err)
        })
    },
  },
  created() {
    this.getRecommendations()
  }
}
</script>

<style scoped>
  .sugTitle {
    margin: 20px 0 50px 0;
  }

  .slideColor {
    background-color: #CF7500;
  }
  .test {
    height: 200px;
  }
</style>