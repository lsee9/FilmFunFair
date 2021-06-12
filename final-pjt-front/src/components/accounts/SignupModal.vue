<template>
  <div>
    <b-modal 
      v-model="signuppopup" 
      centered 
      hide-header-close
      hide-footer
      no-close-on-backdrop
    >
      <template #modal-header>
          <h4 class="headertitle">회원가입</h4>
          <b-button class="headerbtn" variant="outline" @click="signupCloseClick">
            x
          </b-button>
      </template>
      <div>
        <div>
          <b-form-input
            class="mt-4"
            type="text" 
            placeholder="사용자이름" 
            v-model="username"
          />
        </div>
        <div class="py-1"> 
          <b-form-input 
            class="mt-5"
            type="password" 
            placeholder="비밀번호" 
            v-model="password"
          />
        </div>
        <div> 
          <b-form-input 
            class="mt-5"
            type="password" 
            placeholder="비밀번호 확인" 
            v-model="passwordConfirmation"
            @keyup.enter="signup"
          />
        </div>
        <div class="goleft mt-4 signup-signup-btn">
          <b-button variant="outline-primary" @click="signup">Signup</b-button>
        </div>
      </div>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Signup',
  props: {
    signuppopup: Boolean
  },
  data: function () {
    return {
      username: '',
      password: '',
      passwordConfirmation: '',
      success: false
    }
  },
  methods: {
    signup: function () {
      axios({
        url: 'http://127.0.0.1:8000/accounts/signup/',
        method: 'POST',
        data: {
          username: this.username,
          password: this.password,
          passwordConfirmation: this.passwordConfirmation,
        },
      }).then(()=>{
        this.signupCloseClick()
        this.username= ''
        this.password= ''
        this.passwordConfirmation= ''
        alert('회원가입이 성공적으로 완료되었습니다.')
        
      }).catch((err)=>{
        alert(JSON.stringify(err.response.data))
      })
    },
    signupCloseClick() {
      this.$emit('signupCloseClick')
      this.username= ''
      this.password= ''
      this.passwordConfirmation= ''
    }
  }
}
</script>

<style scoped>
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

.signup-signup-btn button {
  color: #e2651c;
  border: 1px solid #e2651c;
  width: 100%;
}

.signup-signup-btn button:hover,
.signup-signup-btn button:active {
  color: #F4F4F4;
  background-color: #e2651c;
  border: 1px solid #e2651c;
}

.signup-signup-btn button:focus {
  box-shadow: none;
}

.signup-signup-btn {
  margin-bottom: 10px;
}
</style>