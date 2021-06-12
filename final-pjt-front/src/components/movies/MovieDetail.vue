<template>
  <div>
    <!-- 전체 리스트에서 보이는 영화 포스터 -->
    <article class=" items d-flex justify-content-center py-4 px-3">
      <div class="item" style="width: 18rem; height: 27rem;">
        <img
          class="card-img"
          style="width:18rem; height: 27rem; border-radius: 10%;"
          :src="'https://image.tmdb.org/t/p/w500/'+movie.poster_path"
          alt=""
             >
        <div class="caption" style="border-radius: 10%">
          <!--상세내용을 담는 공간(마우스 올리면 보이는 정보)  -->
          <div class="caption-detail">
            <h4>{{ movie.title }}</h4>
            <p class='overview-limit caption-overview' v-if="movie.overview.length">
              {{ movie.overview }}
            </p>
            <p v-else class="caption-overview">
              줄거리 미제공
            </p>
            <p >
              <i class="fas fa-heart fa-lg caption-like"></i>
              <span class="caption-like-count">
                {{ this.likeCount }}명
              </span>
              <span class="cap-like-word">이 좋아합니다!</span> 
            </p>
            <button class='show-detail-btn' @click="selectMovie"> 상세보기 </button>
          </div>
        </div>
      </div>
    </article>

    <MovieDetailModal 
      :movie="movie"
      :popup="popup" 
      :loginuser="loginuser"
      @hidemodal="popup=false"
      @checklike="loadLike"
    />

  </div>
</template>

<script>
import axios from 'axios'
import MovieDetailModal from '@/components/movies/modals/MovieDetailModal'

export default {
  name: 'MovieDetail',
  components: {
    // ReviewDetail,
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
      loginuser: 0,
    }
  },
  methods: {
    getLoginUser(token) {
      const base64Url = token.split('.')[1];
      const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
      const jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c) {
          return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
      }).join(''));

      return JSON.parse(jsonPayload).user_id;
    },
    selectMovie () {
      this.loginuser = this.getLoginUser(`JWT ${localStorage.getItem('jwt')}`)
      this.popup = !this.popup
    },
    loadLike () {
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
        })
        .catch(err=>{
          console.log(err)
        })
    },
  },
  created() {
    this.loadLike()
  },
}
</script>

<style>
  .show-detail-btn {
    font-size: 18px;
    color: #F4F4F4;
    background-color: rgb(0, 0, 0, 0.01);
    border: 1px solid #F4F4F4;
    height: 36px;
    padding: 0 6px;
    border-radius: 0.25rem;
  }

  .show-detail-btn:hover,
  .show-detail-btn:active {
    border: 1px solid #F0A500;
    color: #F0A500;
  }

  .items {
    border: 1px solid while;
    text-align: center;
  }

  .item {
    display: inline-block;
    width: 18rem;
    height: auto;
    position: relative;
  }

  .caption {
    width: 18rem;
    height: 27rem;
    background-color: #000;
    position: absolute;
    top: 0;
    left: 0;
    color: #fff;
    padding: 20px;
    box-sizing: border-box;
    padding-top: 40px;
    opacity: 0;
    transition: 0.4s;
  }

  .item:hover .caption {    
    opacity: 0.8;
  }

  .caption-detail {
    padding-top: 35px;
  }

  .caption-detail > h4 {
    font-size: 26px;
    padding-bottom: 20px;
  }

  .caption-detail > .caption-overview {
    font-size: 20px;
    padding-bottom: 10px;
  }

  .caption-like {
    color: rgb(181, 25, 25);
  }

  .caption-like-count {
    color: rgb(181, 25, 25);
    font-size: 20px;
  }

  .cap-like-word {
    font-size: 17px;
  }

  .overview-limit {
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    line-height: 21px;
    max-height: 80px;
    -webkit-line-clamp: 4;
    -webkit-box-orient: vertical;
  }

  .radius {
    border-radius: 30%;
  }
</style>