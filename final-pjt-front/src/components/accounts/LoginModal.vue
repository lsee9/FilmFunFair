<template>
  <div class="login-modal">
    <b-modal 
      v-model="popup" 
      centered 
      hide-header-close
      hide-footer
      no-close-on-backdrop
    >
      <template #modal-header>
          <h4 class="headertitle">로그인</h4>
          <b-button class="headerbtn" variant="outline" @click="closeClick">
            x
          </b-button>
      </template>
      <div class="mt-5">
        <b-form-input
          type="text" 
          placeholder="사용자이름" 
          v-model="username"
        />
      </div>
      <div class="py-1"></div>
      <div class="mt-5"> 
        <b-form-input 
          type="password" 
          placeholder="비밀번호" 
          v-model="password"
          @keyup.enter="login"
        />
      </div>
      <div class="goleft login-login-btn">
        <b-button class="mt-4" button-size="sm" variant="outline-warning" @click="login">Login</b-button>
      </div>
      <div class="goleft mt-3 login-signup-btn">
        <b-button variant="ligth" @click="clickSignup">Signup</b-button>
      </div>
    </b-modal>

    <SignupModal
      @click="clickSignup"
      :signuppopup="signuppopup"
      @signupCloseClick="signupCloseClick"
    />

  </div>
</template>

<script>
import axios from 'axios'
import SignupModal from './SignupModal.vue'

  export default {
    name: 'Login',
    components: {
      SignupModal
    },
    data() {
      return {
        username: '',
        password: '',
        signuppopup: false        
      }
    },
    props: {
      popup: Boolean
    },
    methods: {
      closeClick() {
        this.$emit('closeClick')
      },
      login() {
        axios({
          url: 'http://127.0.0.1:8000/accounts/login/',
          method: 'POST',
          data: {
            username: this.username,
            password: this.password,
          },
        }).then((res)=>{
          localStorage.setItem('jwt', res.data.token)
          this.$emit('login')
          this.$router.push({ name: 'MovieList' })
        }).catch((err)=>{
          alert(JSON.stringify(err.response.data))
        })
      },
      clickSignup() {
        this.signuppopup = !this.signuppopup
      },
      signupCloseClick() {
        this.signuppopup = !this.signuppopup
      }
    },
  }
</script>

<style>
.goleft {
  display: flex;
  flex-direction: row-reverse;
}

.headertitle {
  margin-bottom: 0;
}

.headerbtn {
  margin-bottom: 0.5rem;
}

.modal-body .form-control,
.modal-body .form-control:focus {
  color: #F4F4F4;
  background-color: rgb(0, 0, 0, 0.01);
  font-size: 18px;
  border: rgb(0, 0, 0, 0.01);
  border-bottom: 1px solid #F4F4F4;
  border-radius: 0;
}

.modal-body .form-control:focus {
  box-shadow: none;
}

.login-login-btn button {
  font-size: 18px;
  color: #F0A500;
  border: 1px solid #F0A500;
  width: 100%;
}

.login-login-btn button:hover,
.login-login-btn button:active {
  color: #F4F4F4;
  background-color: #F0A500;
}

.login-signup-btn button {
  font-size: 16px;
  color: #908b8b;
  border: 1px solid #908b8b;
}

.login-signup-btn button:hover,
.login-signup-btn button:active {
  color: #e2651c;
  border: 1px solid #e2651c;
}

.login-signup-btn button:focus {
  box-shadow: none;
}
</style>