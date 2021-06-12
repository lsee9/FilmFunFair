<template>
  <div class="left" id="nav">
    <div id="sideLogo">
      Film 
      Fun Fair
    </div>
    <section v-if="isLogin" class="list">
      <div class="nav-overroll">
        <p>
          <router-link to="/mypage">MyPage</router-link>
        </p>
        <p>
          <router-link to="/movielist">MovieList</router-link> 
        </p>
        <p>
          <router-link to="/communitylist">Community</router-link>
        </p>
        <p>
          <router-link to="/random">Random</router-link>
        </p>
        <p>
          <router-link @click.native="logout" to="#">Logout</router-link>
        </p>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  props: {
    isToggle: {
      type: Boolean,
    },
    isLogin: {
      type: Boolean,
    }
  },
  methods: {
    logout() {
      this.$emit('logput')
      localStorage.removeItem('jwt')
      this.$router.push({ name:'Home' })
    },
  },
  watch: {
    isToggle() {
      const sideMenu = document.querySelector('.left')
      const sideMenuBtn = document.querySelector('.side-menu-x')
      if (this.isToggle) {
        sideMenu.style.left = '0px'
        sideMenuBtn.style.left = '300px'
      }else {
        sideMenu.style.left = '-300px'
        sideMenuBtn.style.left = '-300px'
      }
    },
    '$route' (to, from) {
      if (to.path !== from.path) {
        const sideMenu = document.querySelector('.left')
        sideMenu.style.left = '-300px'
        this.$emit('page-change')
      }  
    },
  },
}
</script>
  
<style>
.nav-overroll {
  display: flex;
  flex-direction: column;
}

.left {
  position: fixed;
  top: 0px;
  left: -300px;
  width: 300px;
  height: 1000px;
  background-color: rgba(240, 165, 0, 0.7);
  overflow: hidden;
  transition: all 0.2s;
}

#nav {
  padding: 50px 0 0 0;
}

#sideLogo {
  font-size: 40px;
}

#nav section {
  padding-top: 35px;
}

#nav a {
  font-size: 28px;
  font-weight: bold;
  color: #F4F4F4;
}

#nav a.router-link-exact-active {
  color: #e9880a;
}
</style>