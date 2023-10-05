import { createApp } from 'vue'
import store from './lib/store_vuex'
// import './style.css'
import App from './App.vue'
import router from './router/router'
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap-icons/font/bootstrap-icons.css';
import 'bootstrap/dist/js/bootstrap';
import 'bootstrap/dist/js/bootstrap.min.js';
import { createPinia } from 'pinia' //피니아
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate' //피니아

const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)

const app = createApp(App)
app.use(pinia)
app.use(router)
// app.use(store)
app.mount('#app')
