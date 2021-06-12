<template>
  <div>
    <div class="frame">
      <h1 class="randomtitle">오늘의 랜덤 영화</h1>
      <div class="center">
        <div class="card">
          <div class="wrap">
            <div class="front">
            <img class="front-img" src="@/assets/randombox.png">
            </div>
            <div class="back">
              <div class="sky">
              </div>
              <div class="compo">
                <div class="back-img"><MovieDetail :movie="movie"/></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieDetail from '@/components/movies/MovieDetail.vue'

export default {
  data() {
    return {
      movie: []
    }
  },
  components: {
    MovieDetail,
  },
  methods: {
    getMovie() {
      axios({
        method: 'GET',
        url: 'http://127.0.0.1:8000/movies/random/',
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },
      })
        .then(res => {
          this.movie = res.data
        })
        .catch(err => {
          console.log(err)
        })
    }
  },
  created() {
    this.getMovie()
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Fredoka+One&family=Jua&display=swap');

.randomtitle {
  font-family: 'Fredoka One', cursive;
  font-family: 'Jua', sans-serif;
  color: #F4F4F4;
}

.frame {
  position: absolute;
  top: 40%;
  left: 40%;
  width: 40rem;
  height: 40rem;
  margin-top: -200px;
  margin-left: -200px;
  border-radius: 10%;
  overflow: hidden;
  color: rgb(0, 0, 0, 0.89);
  font-family: 'Open Sans', Helvetica, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.center {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%,-50%);
}
.card,
.wrap{
  position: relative;
  width: 18rem;
  height: 27rem;
  border-radius: 10%;
  perspective: 27rem;
  background-color: rgba(0, 0, 0, 0);
}
.wrap {
  transition: 1.5s;  
  transform-style: preserve-3d;
}
.card:hover .wrap {
  transform: rotateX(180deg);
}

.back,
.front {
  position: absolute;
  width: 18rem;
  height: 27rem;
  border-radius: 10%;
  top: 50%;
  left: 50%;
  transform: translate(-50%,-50%);
  transform-origin: 50% 0;
  background: #fff;
  text-align: center;
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
}
.front {
  z-index: 1;
}
.back {
  transform: rotateX(180deg) translate(-50%,-50%);
}

.front-img{
  width: 18rem;
  height: 27rem;
  position: relative;
  border-radius: 10%;
}

.back-img {
  width: 18rem;
  height: 27rem;
  position: relative;
  border-radius: 10%;
}

.compo {
  margin-top: -24px;
}

</style>