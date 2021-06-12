<template>
  <div>
    <!-- 전체 리스트에서 보이는 영화 포스터 -->
    <article class="myInfoItems">
      <div class="myInfoItem">
        <img
          class="myMoviePoster"
          :src="'https://image.tmdb.org/t/p/w500/'+movie.poster_path"
          alt=""
        >

        <div class="myInfoCaption">
          <!--상세내용을 담는 공간  -->
          <div class="myInfo-cap-detail">
            <h4>{{ movie.title }}</h4>
            <p class='myInfo-overview-limit myIfo-cap-overview' v-if="movie.overview.length">
              {{ movie.overview }}
            </p>
            <p v-else>
              줄거리 미제공
            </p>
            <!-- 좋아한 사람 수 -->
            <p>
              <i class="fas fa-heart fa-lg info-caption-like"></i>
              <span class="info-cap-like-count">
                {{ this.likeCount }}명
              </span> 
              이 좋아합니다!
            </p>
            <button class="my-detail-btn" @click="selectMovie">상세보기</button>
          </div>
        </div>
      </div>
    </article>

    <MovieDetailModal 
      :movie="movie"
      :popup="popup" 
      @hidemodal="popup=false"
      @checklike="checklike"
      @checkwatch="checkwatch"
    />
  </div>
</template>

<script>
import axios from 'axios'
import MovieDetailModal from '@/components/movies/modals/MovieDetailModal'

export default {
  name: 'MovieDetail',
  components: {
    MovieDetailModal,
  },
  props: {
    movie: {
      type: Object,
    }
  },
  data () {
    return {
      popup: false,
      like: false,
      likeCount: 0,
    }
  },
  methods: {
    selectMovie () {
      this.popup = !this.popup
    },
    checkwatch () {
      this.$emit('checkwatch')
    },
    checklike () {
      axios({
        method: 'GET',
        url: `http://127.0.0.1:8000/movies/${this.movie.id}/like/`,
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },
      })
        .then(res=>{
          this.like = res.data.like
          this.likeCount = res.data.count
          this.$emit('checklike')
        })
        .catch(err=>{
          console.log(err)
        })
    },
  },
  created() {
    this.checklike()
  },
}
</script>

<style >
  .my-detail-btn {
    font-size: 15px;
    color: #F4F4F4;
    background-color: rgb(0, 0, 0, 0.01);
    border: 1px solid #F4F4F4;
    height: 35px;
    padding: 0 6px;
    border-radius: 0.25rem;
  }
  .my-detail-btn:hover,
  .my-detail-btn:active {
    border: 1px solid #F0A500;
    color: #F0A500;
  }

  .myInfoItems {
    text-align: center;
    margin: 30px 7px 0 7px;
  }

  .myInfoItem {
    display: inline-block;
    position: relative;
  }

  .myMoviePoster,
  .myInfoItem,
  .myInfoCaption {
    width:16rem; 
    height: 22rem;
    border-radius: 10%;
  }

  .myInfoCaption {
    background-color: #000;
    position: absolute;
    top: 0;
    left: 0;
    color: #fff;
    padding: 20px;
    box-sizing: border-box;
    padding-top: 45px;
    opacity: 0;
    transition: 0.4s;
  }

  .myInfoItem:hover .myInfoCaption {    
    opacity: 80%;
  }

  .myInfo-cap-detail {
    padding-top: 25px;
  }

  .myInfo-cap-detail > h4 {
    font-size: 22px;
    padding-bottom: 15px;
  }

  .myInfo-cap-detail > .myIfo-cap-overview {
    font-size: 16px;
    padding-bottom: 10px;
  }

  .info-caption-like {
    color: rgb(181, 25, 25);
  }

  .info-cap-like-count {
    color: rgb(181, 25, 25);
    font-size: 18px;
  }

  .myInfo-overview-limit {
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    line-height: 21px;
    max-height: 80px;
    -webkit-line-clamp: 4;
    -webkit-box-orient: vertical;
  }
</style>