<template>
  <div v-if="video" class="youtube-video">
    <iframe 
      width=392
      height=220.5
      :src="videoUrl"
      title="YouTube video player" 
      frameborder="0" 
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
      allowfullscreen>
    </iframe>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'https://www.googleapis.com/youtube/v3/search'
const API_KEY = 123//Your Youtube API KEY

export default {
  name: 'MovieDetailPreview',
  props: {
    movieTitle: String
  },
  data() {
    return {
      video: null
    }
  },
  methods: {
    getVideo () {
      const params = {
        key: API_KEY,
        part: 'snippet',
        type: 'video',
        q: this.movieTitle + 'official trailer',
      }
      axios ({
        method: 'GET',
        url: API_URL,
        params,
      })
        .then((response)=>{
          this.video = response.data.items[0]
        })
        .catch((error)=>{
          console.log(error)
        })
    },
  },
  computed: {
    videoUrl () {
      const baseURL = 'https://www.youtube.com/embed/'
      return baseURL + this.video.id.videoId
    },
  },
  created() {
    this.getVideo()
  }
}
</script>

<style>
.youtube-video {
  margin-left: 20px;
}
</style>