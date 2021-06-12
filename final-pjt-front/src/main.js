import Vue from 'vue'
import App from './App.vue'
import router from './router'
import Carousel3d from 'vue-carousel-3d'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import VModal from 'vue-js-modal'

Vue.use(VModal, { dynamic: true })
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)

Vue.use(Carousel3d)

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
