<template>
  <footer class="footer">
    <div class="footer-content">
      <div class="footer-logo">
        <h3>ИП "Белкин"</h3>
      </div>
      <div class="footer-links">
        <a href="#" class="footer-link">О компании</a>
        <a href="#" class="footer-link">Преимущества</a>
        <a href="#" class="footer-link">Отзывы</a>
        <a href="#" class="footer-link">Связаться с нами</a>
      </div>
      <div class="footer-contact">
        <p>+7 (777) 777-77-77</p>
        <p>abcde@email.ru</p>
      </div>
      <div class="footer-contacts">
        
        <div class="social-icons">
          <a href="#" class="social-icon">
            <img src="/images/telegram.png" alt="Telegram" />
          </a>
          <a href="#" class="social-icon">
            <img src="/images/whatsapp.png" alt="WhatsApp" />
          </a>
          <a href="#" class="social-icon">
            <img src="/images/twitter.png" alt="Twitter" />
          </a>
          <a href="#" class="social-icon">
            <img src="/images/vk-logo.png" alt="VK" />
          </a>
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'AppFooter'
}
</script>

<style scoped>
.footer {
  width: 100%;
  background-color: #fff;
  padding: 1rem 7vh;
  padding-bottom: 3rem;
  font-family: 'Nekst', sans-serif;
  border-top: 1px solid #e0e0e0;
}

.footer-content {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  max-width: 1200px;
  margin: 0 auto;
  gap: 1rem;
}

.footer-logo h3 {

  font-family: 'Nekst-SemiBold', sans-serif;
  font-size: clamp(1.5rem, 3vw, 4rem);
  color: #1a202c;
  margin-top: 1rem;
}

.footer-links {
  display: flex;
  flex-direction: column; /* Изменено на столбец */
  gap: 1rem;
}

.footer-link {
  font-family: 'Nekst-Light', sans-serif;
  font-size: clamp(0.9rem, 1.4vw, 1.5rem);
  color: #4a5568;
  text-decoration: none;
  transition: color 0.3s;
}

.footer-link:hover {
  color: #5552E8;
}

.footer-contacts {
  text-align: right;
}

.footer-contact {
  font-family: 'Nekst-Regular', sans-serif;
  font-size: clamp(0.9rem, 1.4vw, 1.5rem);
  color: #5552E8;
  margin: 0.5rem 0;
  display: flex;
    flex-direction: column;
    gap: 1rem;
}


.social-icons {
  display: flex;
  gap: 1rem;
  justify-content: flex-end;
  margin-top: 1rem;
}

.social-icon img {
  width: clamp(20px, 2vw, 24px);
  height: auto;
  transition: opacity 0.3s;
}

.social-icon:hover img {
  opacity: 0.7;
}

/* Адаптивность для мобильных устройств */
@media (max-width: 768px) {
  .footer {
    padding: 2rem 3vh;
  }

  .footer-content {
    flex-direction: column;
    align-items: center;
    text-align: center;
    gap: 1.5rem;
  }

  .footer-links {
    flex-direction: column;
    gap: 1rem;
  }

  .footer-contacts {
    text-align: center;
  }

  .social-icons {
    justify-content: center;
  }
}
</style>