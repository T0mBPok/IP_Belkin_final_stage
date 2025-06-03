import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '@/components/HomePage.vue';
import ServicesPage from '@/components/ServicesPage.vue';
import AdminLogin from '@/components/AdminLogin.vue'; // Новый компонент для входа
import AdminPanel from '@/components/AdminPanel.vue'; // Новый компонент для админ-панели

// Функция для проверки авторизации
const isAuthenticated = () => {
  return !!localStorage.getItem('authToken'); // Проверяем наличие токена в localStorage
};

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomePage
  },
  {
    path: '/services',
    name: 'Services',
    component: ServicesPage
  },
  {
    path: '/admin/login',
    name: 'AdminLogin',
    component: AdminLogin
  },
  {
    path: '/admin',
    name: 'AdminPanel',
    component: AdminPanel,
    beforeEnter: (to, from, next) => {
      if (isAuthenticated()) {
        next(); // Пропускаем, если пользователь авторизован
      } else {
        next('/admin/login'); // Перенаправляем на страницу входа
      }
    }
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;