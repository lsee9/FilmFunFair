<template>
  <div>
    <!-- 영화 검색 -->
    <div class="search-msg">
      <h3 class="before" v-if="!isSearch" @click="isSearch=true">
        <i class="fas fa-search"></i>
        <span>Movie Search</span> 
      </h3>
      <h3 class="after" v-else @click="searchClose">Stop Search</h3>
    </div>

    <!-- 영화 검색창 -->
    <div class="search-flex-container">
      <div class="search-input">
        <input 
          v-if="isSearch"
          id="searchArea"
          type="text" 
          @input="changeKeyword"
          @keyup="keywordMatch"
          @keydown="viewMatchList"
          placeholder="보고 싶은 영화를 입력하세요"
        >
      </div>
    </div>

    <!-- 영화 검색 결과 자동완성창 -->
    <div class="result-auto-complete">
      <div class="search-result-container" v-if="isSearch">
        <Search 
          class="search-results"
          v-for="movie in matchedLists" 
          :key="movie.id"
          :movie="movie"
        />
      </div>
    </div>

    <!-- 영화 추천 부분 -->
    <div class="list-sugg">
      <h2>Movie Present for YOU</h2>
      <MovieSuggest />
    </div>

    <!-- 섹션 나누는 선 -->
    <div class="movie-list-section">
    </div>

    <!-- 전체 영화 리스트 -->
    <h2>
      <i class="fas fa-film fa-sm"></i>
      Pick Your Favorite
      <i class="fas fa-film fa-sm"></i>
    </h2>
    <div class="flex-container">
      <MovieDetail 
        v-for="movie in movies"
        :key="movie.id"
        :movie="movie"
      />
    </div>
    
    <!-- 로딩스피너 -->
    <div class="text-center my-3">
      <b-spinner
        variant="warning"
        style="width: 3rem; height: 3rem;"
      ></b-spinner>
    </div>
  </div>
</template>


<script>
import axios from 'axios'
import lodash from 'lodash'
import MovieDetail from '@/components/movies/MovieDetail.vue'
import MovieSuggest from '@/components/movies/MovieSuggest.vue'
import Search from '@/components/movies/Search.vue'

export default {
  name: 'MovieList',
  components: {
    MovieDetail,
    MovieSuggest,
    Search,
  },
  data () {
    return {
      isSearch: false,
      searchdatas: [],
      movies: [],
      isClick: false,
      keyword: '',
      matchedLists: [],
      page: 1,
    }
  },
  methods: {
    getDatas() {
      axios({
        method: 'GET',
        url: 'http://127.0.0.1:8000/movies/search/',
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },
      })
        .then(res => {
            this.searchdatas = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    getMovie() {
      axios({
        method: 'GET',
        url: 'http://127.0.0.1:8000/movies/index/',
        params: {
          p: this.page,
        },
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },
      })
        .then(res => {
          this.movies.push(...res.data)
        })
        .catch(err => {
          console.log(err)
        })
    },
    viewDetail () {
      this.isClick = !this.isClick
    },

    changeKeyword (word) {
      this.keyword = word.target.value
    },
    
    ch2pattern (ch) {
      const offset = 44032;
      if (/[가-힣]/.test(ch)) {
        const chCode = ch.charCodeAt(0) - offset;
        if (chCode % 28 > 0) {
          return ch;
        }
        const begin = Math.floor(chCode / 28) * 28 + offset;
        const end = begin + 27;
        return `[\\u${begin.toString(16)}-\\u${end.toString(16)}]`;
      }
      if (/[ㄱ-ㅎ]/.test(ch)) {
        const con2syl = {
          'ㄱ': '가'.charCodeAt(0),
          'ㄲ': '까'.charCodeAt(0),
          'ㄴ': '나'.charCodeAt(0),
          'ㄷ': '다'.charCodeAt(0),
          'ㄸ': '따'.charCodeAt(0),
          'ㄹ': '라'.charCodeAt(0),
          'ㅁ': '마'.charCodeAt(0),
          'ㅂ': '바'.charCodeAt(0),
          'ㅃ': '빠'.charCodeAt(0),
          'ㅅ': '사'.charCodeAt(0),
        };
        const begin = con2syl[ch] || ( ( ch.charCodeAt(0) - 12613 ) * 588 + con2syl['ㅅ'] );
        const end = begin + 587;
        return `[${ch}\\u${begin.toString(16)}-\\u${end.toString(16)}]`;
      }
      return lodash.escapeRegExp(ch);
    },
    createFuzzyMatcher (input) {
      const pattern = input.split('').map(this.ch2pattern).join('.*?');
      return new RegExp(pattern, 'gi');
    },
    keywordMatch () {
      const matchedListstmp = this.searchdatas.filter(movie => {
        const regex = this.createFuzzyMatcher(this.keyword)
        return movie.title.match(regex)
      })
      if (matchedListstmp.length > 8) {
        this.matchedLists = matchedListstmp.slice(0, 8)
      } else {
        this.matchedLists = matchedListstmp
      }
      if (this.keyword.length === 0) {
        this.matchedLists = []
      }
    },
    viewMatchList () {

    },
    titleSearch () {

    },
    goLogin () {
      this.$emit('is-login')
    },
    searchClose () {
      this.isSearch = false
      this.matchedLists = false
    },
  },
  created () {
    this.goLogin()
    this.getMovie()
    document.addEventListener('scroll', ()=>{
      const {scrollTop, clientHeight, scrollHeight} = document.documentElement
      if (scrollHeight - scrollTop === clientHeight) {
        if (this.page === 10) {
          this.page = 0
        }
        this.page += 1
        this.getMovie()
      }
    })
    this.getDatas()
  },
}
</script>

<style>
.result-auto-complete{
  display: flex;
  flex-wrap: wrap;
  margin: 0 30vw 20px 30vw;
  flex-direction: column;
  position: relative;
}

.search-results {
  display: flex;
  justify-content: left;
  border-bottom: 1px solid #F4F4F4;
  font-size: 18px;
}

.search-results:hover,
.search-results:active,
.search-results:focus {
  color: #CF7500;
}

.search-result-container {
  background: black;
  position: absolute;
  z-index: 1;
  width: 100%;
  opacity: 0.85;
}

.search-msg {
  display: flex;
  flex-direction: row-reverse;
  margin: 0 15vw 0 17vw;
  padding-top: 10px;
}

.search-msg > h3 {
  font-size: 24px;
}

.search-msg .before {
  color: #F4F4F4;
}

.search-msg .before:hover,
.search-msg .before:active {
  color: #CF7500;
}

.before span {
  margin-left: 10px;
}

.search-msg .after {
  color: #F4F4F4;
}

.search-msg .after:hover,
.search-msg .after:active {
  color: #CF7500;
}

.search-msg .after:hover::before{
  content: '\f256';
  font-family: "Font Awesome 5 Free";
  font-weight: 600;
  margin-right: 10px;
  font-size: 20px;
}

.search-flex-container {
  display: flex;
  flex-wrap: wrap;
  margin: 0 30vw 0 30vw;
  flex-direction: column;
  position: relative;
}

.search-input input {
  background-color: rgb(0, 0, 0, 0.01);
  border: 1px solid #F4F4F4;
  width: 100%;
  height: 50px;
  border-radius: 0.25rem;
  color: #F4F4F4;
}

.search-input input:focus {
  background-color: rgb(0, 0, 0, 0.01);
  color: #F4F4F4;
  outline: none;  
}

.flex-container {
  display: flex;
  flex-wrap: wrap;
  margin: 0 15vw;
}
.list-sugg {
  padding: 40px 0;
}

.movie-list-section {
  border-top: 4px double #bbb;
  text-align: center;
}

.movie-list-section::after {
  content: '\002665';
  display: inline-block;
  position: relative;
  top: -20px;
  padding: 0;
  background-color: rgb(0, 0, 0, 0.05);
  color: #bbb;
  font-size: 25px;
}
</style>
