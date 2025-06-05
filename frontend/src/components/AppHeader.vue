<template>
  <header class="header">
    <div class="header-top">
      <router-link to="/" class="logo">ИП "Белкин"</router-link>
      <button class="menu-toggle" @click="toggleMenu">
        {{ isMenuOpen ? '✖' : '☰' }}
      </button>
      <nav class="nav nav-desktop">
        <router-link to="/services" class="nav-link">Услуги</router-link>
        <router-link to="/pricing" class="nav-link">Прейскурант</router-link>
        <router-link to="/reviews" class="nav-link">Отзывы</router-link>
        <router-link to="/contacts" class="nav-link">Контакты</router-link>
      </nav>
    </div>

    <!-- ВЫПАДАЮЩЕЕ МЕНЮ: только на мобильных -->
    <transition name="slide-down">
      <nav v-show="isMenuOpen" class="nav nav-menu-mobile">
        
        <router-link to="/services" class="nav-link">Услуги</router-link>
        <router-link to="/pricing" class="nav-link">Прейскурант</router-link>
        <router-link to="/reviews" class="nav-link">Отзывы</router-link>
        <router-link to="/contacts" class="nav-link">Контакты</router-link>
      </nav>
    </transition>

    <!-- НАВИГАЦИЯ НА ДЕСКТОПЕ -->
    
  </header>
</template>

<script>
export default {
  name: 'AppHeader',
  data() {
    return {
      isMenuOpen: false,
    };
  },
  methods: {
    toggleMenu() {
      this.isMenuOpen = !this.isMenuOpen;
    },
  },
};
</script>

<style scoped>
.header {
  
  background-color: black;
  color: #ffffff;
  width: 100%;
  position: fixed;
  height: 7vh;
  top: 0;
  z-index: 1000;
  padding: 1rem 5%;
  display: flex;
  flex-direction: column;
  justify-content: center; /* Распределяет элементы по краям контейнера */
  
}

/* Контейнер с логотипом и кнопкой */
.header-top {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

/* Логотип */
.logo {
  align-self: flex-start;
  font-size: clamp(24px, 2.3vw, 50px);
  font-family: 'Nekst-Bold', sans-serif;
}

/* Кнопка меню (гамбургер / крестик) */
.menu-toggle {
  align-self: flex-end;
  display: none;
  background: none;
  border: none;
  font-size: 2rem;
  color: #ffffff;
  cursor: pointer;
}

/* Общие стили ссылок */
.nav-link {
  color: #ffffff;
  text-decoration: none;
  font-size: clamp(1.1rem, 1.3vw, 1.7rem);
  transition: color 0.3s;
}

.nav-link:hover {
  color: #cccccc;
}

/* Десктопная навигация */
.nav-desktop {
  display: flex;
  gap: 2rem;
  font-family: 'Nekst-Light', sans-serif;
  justify-content: flex-end;
  
}

/* Мобильная навигация — по умолчанию скрыта */
.nav-menu-mobile {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  font-family: 'Nekst-Light', sans-serif;
  padding-top: 1rem;

  position: absolute;
  top: 100%;
  left: 0;
  width: 100%;
  background-color: black;
  z-index: 999;
  align-items: center;
}


/* Анимация для мобильного меню */
.slide-down-enter-active,
.slide-down-leave-active {
  transition: max-height 0.3s ease-out, opacity 0.3s ease;
  overflow: hidden;
}
.slide-down-enter-from,
.slide-down-leave-to {
  max-height: 0;
  opacity: 0;
}
.slide-down-enter-to,
.slide-down-leave-from {
  max-height: 300px;
  opacity: 1;
}

/* Адаптация под мобильные */
@media (max-width: 768px) {
  .header{
    padding: 0.5rem 5%;
  }
  .logo{
    padding-top: 1%;
  }
  .nav-desktop {
    display: none;
  }

  .menu-toggle {
    display: block;
  }

  .nav-menu-mobile {
    display: flex;
  }

  .nav-link {
    font-size: clamp(1rem, 4vw, 1.2rem);
  }
}
</style>
