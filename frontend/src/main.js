import { createApp } from 'vue';
import App from './App.vue'; // Убедитесь, что App.vue существует
import router from './router';
import './style.css';

const app = createApp(App);
app.use(router);
app.mount('#app');