<template>
  <section class="form4">
    <h2>Отзывы клиентов</h2>
    <p class="subtitle">Доверие, подтвержденное результатами</p>
    <div class="reviews" v-if="reviews.length">
      <div class="review-card" v-for="review in reviews.slice(0, 3)" :key="review.id">
        <img src="/images/review-icon.png" alt="Review icon" class="review-icon" />
        <p>{{ review.text }}</p>
        <p class="author">{{ review.author }}</p>
      </div>
    </div>
    <div v-else class="loading">Загрузка отзывов...</div>
  </section>
</template>

<script>
import axios from 'axios';

export default {
  name: 'FormFour',
  data() {
    return {
      reviews: []
    };
  },
  async mounted() {
    await this.fetchReviews();
  },
  methods: {
    async fetchReviews() {
      try {
        const response = await axios.get('http://localhost:3000/reviews', {
          params: {
            _limit: 3 // Загружаем только 3 отзыва
          }
        });
        this.reviews = response.data;
      } catch (error) {
        console.error('Ошибка при загрузке отзывов:', error);
      }
    }
  }
};
</script>

<style scoped>
.form4 {
  width: 100%;
  padding: 10vh 7vh;
  background-color: #fff;
  font-family: 'Nekst', sans-serif;
  text-align: center;
}

.form4 h2 {
  font-family: 'Nekst-SemiBold', sans-serif;
  font-size: clamp(1.5rem, 3.3vw, 3.5rem);
  color: #1a202c;
  margin-bottom: 1rem;
  line-height: 1.1;
}

.subtitle {
  font-family: 'Nekst-Thin', sans-serif;
  font-size: clamp(1rem, 1.7vw, 1.2rem);
  color: #4a5568;
  margin-bottom: 3rem;
}

.reviews {
  display: flex;
  justify-content: space-around;
  gap: 2rem;
  flex-wrap: wrap;
}

.review-card {
  background-color: #fff;
  border-radius: 15px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.9);
  padding: 2rem;
  width: 25%;
  min-width: 250px;
  text-align: center;
}

.review-icon {
  width: clamp(80px, 10vw, 120px);
  height: auto;
  margin-bottom: 1rem;
  display: block;
  margin-left: auto;
  margin-right: auto;
}

.review-card p {
  font-family: 'Nekst-Thin', sans-serif;
  font-size: clamp(0.9rem, 1.2vw, 1.1rem);
  color: #4a5568;
  line-height: 1.4;
}

.author {
  font-family: 'Nekst-SemiBold', sans-serif;
  font-size: clamp(1rem, 1.3vw, 1.2rem);
  color: #1a202c;
  margin-top: 1rem;
}

.loading {
  font-family: 'Nekst-Light', sans-serif;
  font-size: clamp(1rem, 1.2vw, 1.2rem);
  color: #4a5568;
  text-align: center;
  margin: 2rem 0;
}

@media (max-width: 768px) {
  .form4 {
    padding: 5vh 3vh;
  }

  .form4 h2 {
    font-size: clamp(1.2rem, 2.5vw, 1.8rem);
  }

  .subtitle {
    font-size: clamp(0.9rem, 1.2vw, 1rem);
    margin-bottom: 2rem;
  }

  .reviews {
    flex-direction: column;
    align-items: center;
  }

  .review-card {
    width: 80%;
    margin-bottom: 2rem;
  }
}
</style>