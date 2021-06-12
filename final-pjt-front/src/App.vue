<template>
  <div id="app">
    <Home 
      v-if="isLogin===false"
      v-show="false"
      @login="login"
    />

    <!-- side Menu -->
    <div>
      <div class="sticky-top">
        <SideBar 
          :isToggle="isToggle" 
          :isLogin="true" 
          @logput="logout"
          @page-change="isToggle=false"
        />
      </div>
    </div>

    <!-- Nav부분 -->
    <div v-show="isLogin" id="navIndex" class="sticky-top" v-if="login">
      <b-navbar variant="faded" type="light" class="nav-color">
        <b-navbar-brand href="#" class="navbar">
          <div id="totalLogo">
            <span id="mainlogo">Film Fun Fair</span>
            <img 
              id="logoImg" 
              src="@/assets/3f_logo.png" 
              width=96
              height=60
              class="d-inline-block align-top" 
              alt="logoImg"
            >
          </div>
          <span v-if="isToggle"  @click="toggle" class="fas fa-times fa-2x bar-after"></span>
          <span v-if="!isToggle" @click="toggle" class="fas fa-bars fa-lg bar"></span>
        </b-navbar-brand>
      </b-navbar>
    </div>  
    

    <router-view @is-login="isLogin=true"/>
  </div>
</template>

<script>
import SideBar from '@/components/SideBar.vue'
import Home from '@/views/Home.vue'

export default {
  name: 'App',
  components: {
    SideBar,
    Home,
  },
  data() {
    return {
      isLogin: false,
      isToggle: false,
    }
  },
  methods: {
    logout () {
      this.isLogin = false
    },
    toggle () {
      this.isToggle = !this.isToggle
    },
    login () {
      this.isLogin = true
      this.$router.push({ name:'MovieList' })
    }
  },
  watch: {
    isToggle() {
      const logo = document.querySelector('#totalLogo')
      if (this.isToggle) {
        logo.style.visibility = 'hidden'
      }else {
        logo.style.visibility = 'visible'
      }
    },
  },
  created() {
    const token = localStorage.getItem('jwt')
    if (token) {
      this.isLogin = true
      this.$router.push({ name: 'MovieList' })
    } else {
      this.$router.push({ name: 'Home'})
      console.log('home')
    }
  },
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Fredoka+One&family=Jua&display=swap');

#app {
  font-family: 'Fredoka One', cursive;
  font-family: 'Jua', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #F4F4F4;
  background-color: rgb(0, 0, 0, 0.89);
}
#mainlogo {
  padding-left: 13px;
  font-size: 40px;
  color: #F0A500;
}

#mainLogo {
  visibility: visible;
}

.bar {
  color: #F4F4F4;
}
.bar:hover,
.bar:active,
.bar:focus {
  color: #F0A500;
}
.bar-after {
  color: #F4F4F4;
  height: 30px;
  top: 2rem;
}
.bar-after:hover,
.bar-after:active,
.bar-after:focus {
  color: #F0A500;
}

html {
  background-color: rgb(0, 0, 0, 0.89);
}
</style>
