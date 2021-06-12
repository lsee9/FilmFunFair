import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home'
import MyPage from '@/views/accounts/MyPage.vue'
import CommunityCreate from '@/views/communities/CommunityCreate.vue'
import CommunityDetail from '@/views/communities/CommunityDetail.vue'
import CommunityList from '@/views/communities/CommunityList.vue'
import CommunityUpdate from '@/views/communities/CommunityUpdate.vue'
import MovieList from '@/views/movies/MovieList.vue'
import Random from '@/views/movies/Random.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/home',
    name: 'Home',
    component: Home
  },
  {
    path: '/mypage',
    name: 'MyPage',
    component: MyPage
  },
  {
    path: '/communitycreate',
    name: 'CommunityCreate',
    component: CommunityCreate
  },
  {
    path: '/communitydetail/:postId',
    name: 'CommunityDetail',
    component: CommunityDetail,
    props: true
  },
  {
    path: '/communitylist',
    name: 'CommunityList',
    component: CommunityList
  },
  {
    path: '/communityupdate/:postId',
    name: 'CommunityUpdate',
    component: CommunityUpdate,
    props: true
  },
  {
    path: '/movielist',
    name: 'MovieList',
    component: MovieList
  },
  {
    path: '/random',
    name: 'Random',
    component: Random
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
