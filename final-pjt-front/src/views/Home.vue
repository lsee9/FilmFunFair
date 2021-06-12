<template>
  <div class="mainpage" @click="onClick">
    <!-- modal -->
    <div>
      <Loginmodal 
        :popup="popup" 
        @hidemodal="popup=false"
        @login="login"
        @closeClick="closeClick"
      />
    </div>    

    <!-- mainpage -->
    <div>
      <div class="main-title-compo">
        <h2 class="main-title-fff">
          Film Fun Fair
          <div class="getstart">
            Get Start
          </div>
        </h2>
      </div>

    <section class="wrap">
      <div class="box">
      </div>
      <div class="box">
      </div>
      <div class="circle" />
    </section>
    </div>
  </div>
</template>

<script>
import Loginmodal from '@/components/accounts/LoginModal.vue'

const html = document.documentElement;

window.addEventListener("load", function(){
  html.style.setProperty('--x', 0);
  html.style.setProperty('--y', 0);
});

html.addEventListener("mousemove", function(e) {
  html.style.setProperty('--x', e.clientX + 'px');
  html.style.setProperty('--y', e.clientY + 'px');
})
export default {
  name: 'Home',
  components: {
    Loginmodal
  },
  data() {
    return {
      popup: false
    }
  },
  methods: {
    onClick() {
      this.popup = !this.popup
    },
    closeClick() {
      this.popup = !this.popup
    },
    login() {
      this.$emit('login')
    },
  },
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Lobster&display=swap');

.main-title-fff {
  color: white;
  position: absolute;
  z-index: 100;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Lobster', cursive;
  color: #F4F4F4;
  font-size: 8rem;
  cursor: pointer;
  transform: translate(calc(var(--x)/25), calc(var(--y)/25));
}

.main-title-compo {
  display: flex;
  justify-content: center;
  align-items: center;
  width:100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
}

.getstart {
  font-size: 4rem;
}

.startfont {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Lobster', cursive;
  color: white;
  font-size: 3.5rem;
  cursor: pointer;
}

.fontstyle {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Lobster', cursive;
  color: white;
  font-size: 10rem;
  cursor: pointer;

}
.wrap,
.box {
  position: absolute;
  top: 0;
  left: 0;
  width:100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center; 
}
.box {
  background: url('../assets/home.jpg');
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
  overflow: hidden;
}
.box:nth-child(1) {
  filter: blur(8px) brightness(50%);
}
.box:nth-child(2) {
  clip-path: circle(150px at var(--x) var(--y));
}
.box h2{
  position: relative;
  transform: translate(calc(var(--x)/25), calc(var(--y)/25));
}

.circle {
  position: absolute;
  width: 300px;
  height: 300px;
  border: 2px solid #fff;
  border-radius: 50%;
  box-shadow: 0 5px 23px rgba(0,0,0,0.5);
  top: -150px;
  left: -150px;
  transform: translate(var(--x),var(--y));
}
</style>