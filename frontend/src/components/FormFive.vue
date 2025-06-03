<template>
  <section class="form5">
    <div class="contact-banner">
      <img src="/images/contact-bg.png" alt="Contact background" class="contact-image" />
      <div class="contact-content">
        <h2>Оцените условия труда <br /> в вашей компании</h2>
        <p>Оставьте заявку и мы свяжемся с вами</p>
        <div class="contact-info">
          <div class="contact-item">
            <input
              type="text"
              placeholder="Имя"
              v-model="form.name"
              :class="{ 'error': errors.name }"
            />
            <span v-if="errors.name" class="error-message">{{ errors.name }}</span>
          </div>
          <div class="contact-item">
            <input
              type="tel"
              placeholder="+7 (777) 777-77-77"
              v-model="form.phone"
              :class="{ 'error': errors.phone }"
            />
            <span v-if="errors.phone" class="error-message">{{ errors.phone }}</span>
          </div>
          <div class="contact-item">
            <input
              type="email"
              placeholder="Почта"
              v-model="form.email"
              :class="{ 'error': errors.email }"
            />
            <span v-if="errors.email" class="error-message">{{ errors.email }}</span>
          </div>
          <button class="contact-button" @click="submitForm" :disabled="isSubmitting">
            {{ isSubmitting ? 'Отправка...' : 'Получить консультацию' }}
          </button>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'FormFive',
  data() {
    return {
      form: {
        name: '',
        phone: '',
        email: ''
      },
      errors: {
        name: '',
        phone: '',
        email: ''
      },
      isSubmitting: false
    };
  },
  methods: {
    
    sanitizeInput(input) {
      const div = document.createElement('div');
      div.textContent = input;
      return div.innerHTML;
    },
    validateForm() {
      this.errors = { name: '', phone: '', email: '' };
      let isValid = true;

      
      const nameRegex = /^[a-zA-Zа-яА-Я\s-]{2,50}$/;
      if (!this.form.name.trim()) {
        this.errors.name = 'Введите имя';
        isValid = false;
      } else if (!nameRegex.test(this.form.name.trim())) {
        this.errors.name = 'Имя должно содержать 2–50 букв, пробелов или дефисов';
        isValid = false;
      }

      
      const phoneRegex = /^\+?\d{10,15}$/;
      if (!this.form.phone.trim()) {
        this.errors.phone = 'Введите номер телефона';
        isValid = false;
      } else if (!phoneRegex.test(this.form.phone.replace(/\D/g, ''))) {
        this.errors.phone = 'Некорректный формат телефона';
        isValid = false;
      }

      
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!this.form.email.trim()) {
        this.errors.email = 'Введите email';
        isValid = false;
      } else if (!emailRegex.test(this.form.email)) {
        this.errors.email = 'Некорректный формат email';
        isValid = false;
      }

      return isValid;
    },
    async submitForm() {
      if (!this.validateForm()) return;

      this.isSubmitting = true;

      
      const sanitizedForm = {
        name: this.sanitizeInput(this.form.name.trim()),
        phone: this.sanitizeInput(this.form.phone.trim()),
        email: this.sanitizeInput(this.form.email.trim())
      };

      try {
        const response = await fetch('https://your-backend-api.com/submit', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(sanitizedForm)
        });

        if (!response.ok) {
          throw new Error('Ошибка при отправке данных');
        }

        const result = await response.json();
        console.log('Ответ сервера:', result);
        alert('Заявка успешно отправлена!');
        // Сброс формы
        this.form = { name: '', phone: '', email: '' };
      } catch (error) {
        alert('Произошла ошибка: ' + error.message);
      } finally {
        this.isSubmitting = false;
      }
    }
  }
};
</script>

<style scoped>
/* Существующие стили */
.form5 {
  width: 100%;
  position: relative;
  overflow: hidden;
}

.contact-banner {
  position: relative;
  width: 100%;
  height: 60vh;
  max-height: 500px;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #4a90e2;
}

.contact-image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: 0;
  filter: brightness(65%);
}

.contact-content {
  position: relative;
  z-index: 1;
  text-align: center;
  color: #fff;
  padding: 20px;
}

.contact-content h2 {
  font-family: 'Nekst-SemiBold', sans-serif;
  font-size: clamp(2.9rem, 4.3vw, 4.5rem);
  margin-bottom: 2vh;
  line-height: 1.1;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.9);
}

.contact-content p {
  font-family: 'Nekst-Medium', sans-serif;
  font-size: clamp(1.2rem, 1.7vw, 2rem);
  margin-bottom: 3vh;
  text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.5);
}

.contact-info {
  display: flex;
  justify-content: center;
  gap: 1rem;
  flex-wrap: wrap;
}

.contact-item {
  background-color: rgba(255, 255, 255, 0.9);
  color: #1a202c;
  width: 23%;
  padding: clamp(8px, 1.5vw, 12px);
  padding-left: 1vw;
  border-radius: 25px;
  font-family: 'Nekst-Light', sans-serif;
  font-size: clamp(14px, 1.5vw, 16px);
  text-align: left;
}

.contact-item input {
  background: none;
  border: none;
  width: 100%;
  font-family: 'Nekst-Light', sans-serif;
  font-size: clamp(14px, 1.5vw, 16px);
  color: #1a202c;
  text-align: left;
  outline: none;
}

.contact-button {
  background-color: #5552e8;
  color: #fff;
  border: none;
  padding: clamp(8px, 1.5vw, 12px) clamp(20px, 2.5vw, 25px);
  border-radius: 25px;
  cursor: pointer;
  font-size: clamp(14px, 1.5vw, 16px);
  transition: background-color 0.3s;
  font-family: 'Nekst-Medium', sans-serif;
  text-decoration: none;
}

.contact-button:hover {
  background-color: #5a67d8;
}

.contact-button:disabled {
  background-color: #a0a0a0;
  cursor: not-allowed;
}

/* Стили для ошибок */
.error {
  border: 1px solid #ff4d4f;
}

.error-message {
  color: #ff4d4f;
  font-size: clamp(12px, 1vw, 14px);
  margin-top: 5px;
  display: block;
}

/* Адаптивность для мобильных устройств */
@media (max-width: 768px) {
  .contact-banner {
    height: 60vh;
    max-height: 350px;
  }

  .contact-content h2 {
    font-size: clamp(1.2rem, 2.5vw, 1.8rem);
  }

  .contact-content p {
    font-size: clamp(0.9rem, 1.2vw, 1.2rem);
  }

  .contact-info {
    flex-direction: column;
    align-items: center;
  }

  .contact-item {
    width: 80%;
    font-size: clamp(12px, 1.2vw, 14px);
    padding: clamp(6px, 1vw, 10px) clamp(15px, 2vw, 20px);
  }

  .contact-button {
    font-size: clamp(14px, 1.8vw, 24px);
    padding: clamp(6px, 1vw, 10px) clamp(15px, 2vw, 20px);
  }
}
</style>