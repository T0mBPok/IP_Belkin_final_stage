<template>
  <div class="admin-panel">
    <header class="panel-header">
      <h1>Админ-панель</h1>
      <button @click="logout">Выйти</button>
    </header>
    <section class="requests-section">
      <h2>Заявки с сайта</h2>
      <div v-if="loading" class="loading">Загрузка...</div>
      <div v-else-if="error" class="error">{{ error }}</div>
      <div v-else>
        <table class="requests-table">
          <thead>
            <tr>
              <th>Имя</th>
              <th>Телефон</th>
              <th>Email</th>
              <th>Дата</th>
              <th>Действия</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="request in paginatedRequests" :key="request.id">
              <td>{{ request.name }}</td>
              <td>{{ request.phone }}</td>
              <td>{{ request.email }}</td>
              <td>{{ formatDate(request.createdAt) }}</td>
              <td>
                <button class="delete-btn" @click="deleteRequest(request.id)">Удалить</button>
              </td>
            </tr>
          </tbody>
        </table>
        <div class="pagination">
          <button :disabled="currentPage === 1" @click="currentPage--">Назад</button>
          <span>Страница {{ currentPage }} из {{ totalPages }}</span>
          <button :disabled="currentPage === totalPages" @click="currentPage++">Вперёд</button>
        </div>
      </div>
    </section>
    <section class="reviews-section">
      <h2>Управление отзывами</h2>
      <div class="review-form">
        <div class="form-group">
          <label for="review-text">Текст отзыва</label>
          <textarea
            id="review-text"
            v-model="newReview.text"
            placeholder="Введите текст отзыва"
          ></textarea>
        </div>
        <div class="form-group">
          <label for="review-author">Автор</label>
          <input
            type="text"
            id="review-author"
            v-model="newReview.author"
            placeholder="Введите имя автора"
          />
        </div>
        <button @click="addReview" :disabled="adding">Добавить отзыв</button>
      </div>
      <div v-if="loadingReviews" class="loading">Загрузка отзывов...</div>
      <div v-else-if="reviewError" class="error">{{ reviewError }}</div>
      <div v-else>
        <table class="reviews-table">
          <thead>
            <tr>
              <th>Текст</th>
              <th>Автор</th>
              <th>Дата</th>
              <th>Действия</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="review in paginatedReviews" :key="review.id">
              <td>{{ review.text }}</td>
              <td>{{ review.author }}</td>
              <td>{{ formatDate(review.createdAt) }}</td>
              <td>
                <button class="edit-btn" @click="editReview(review)">Редактировать</button>
                <button class="delete-btn" @click="deleteReview(review.id)">Удалить</button>
              </td>
            </tr>
          </tbody>
        </table>
        <div class="pagination">
          <button :disabled="currentReviewPage === 1" @click="currentReviewPage--">Назад</button>
          <span>Страница {{ currentReviewPage }} из {{ totalReviewPages }}</span>
          <button :disabled="currentReviewPage === totalReviewPages" @click="currentReviewPage++">Вперёд</button>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'AdminPanel',
  data() {
    return {
      requests: [],
      reviews: [],
      loading: false,
      loadingReviews: false,
      error: '',
      reviewError: '',
      currentPage: 1,
      currentReviewPage: 1,
      itemsPerPage: 5,
      reviewItemsPerPage: 3, // Ровно 3 отзыва на страницу
      newReview: {
        text: '',
        author: '',
        createdAt: new Date().toISOString()
      },
      adding: false,
      editingReview: null
    };
  },
  computed: {
    paginatedRequests() {
      const start = (this.currentPage - 1) * this.itemsPerPage;
      const end = start + this.itemsPerPage;
      return this.requests.slice(start, end);
    },
    totalPages() {
      return Math.ceil(this.requests.length / this.itemsPerPage);
    },
    paginatedReviews() {
      const start = (this.currentReviewPage - 1) * this.reviewItemsPerPage;
      const end = start + this.reviewItemsPerPage;
      return this.reviews.slice(start, end);
    },
    totalReviewPages() {
      return Math.ceil(this.reviews.length / this.reviewItemsPerPage);
    }
  },
  watch: {
    currentPage() {
      this.fetchRequests();
    },
    currentReviewPage() {
      this.fetchReviews();
    }
  },
  methods: {
    async fetchRequests() {
      this.loading = true;
      this.error = '';

      try {
        const token = localStorage.getItem('authToken');
        const response = await axios.get('http://localhost:3000/requests', {
          headers: { Authorization: `Bearer ${token}` },
          params: { _page: this.currentPage, _limit: this.itemsPerPage }
        });
        this.requests = response.data;
      } catch (error) {
        if (error.response && error.response.status === 401) {
          this.logout();
        } else {
          this.error = 'Ошибка при загрузке заявок. Попробуйте снова.';
          console.error('Fetch requests error:', error);
        }
      } finally {
        this.loading = false;
      }
    },
    async fetchReviews() {
      this.loadingReviews = true;
      this.reviewError = '';

      try {
        const token = localStorage.getItem('authToken');
        const response = await axios.get('http://localhost:3000/reviews', {
          headers: { Authorization: `Bearer ${token}` },
          params: { _page: this.currentReviewPage, _limit: this.reviewItemsPerPage }
        });
        this.reviews = response.data;
      } catch (error) {
        this.reviewError = 'Ошибка при загрузке отзывов. Попробуйте снова.';
        console.error('Fetch reviews error:', error);
      } finally {
        this.loadingReviews = false;
      }
    },
    async addReview() {
      if (!this.newReview.text.trim() || !this.newReview.author.trim()) {
        this.reviewError = 'Заполните все поля';
        return;
      }

      this.adding = true;
      try {
        const token = localStorage.getItem('authToken');
        const response = await axios.post('http://localhost:3000/reviews', this.newReview, {
          headers: { Authorization: `Bearer ${token}` }
        });
        this.reviews.push(response.data);
        this.newReview = { text: '', author: '', createdAt: new Date().toISOString() };
        this.reviewError = '';
      } catch (error) {
        this.reviewError = 'Ошибка при добавлении отзыва.';
        console.error('Add review error:', error);
      } finally {
        this.adding = false;
      }
    },
    editReview(review) {
      this.editingReview = { ...review };
    },
    async saveReview() {
      if (!this.editingReview.text.trim() || !this.editingReview.author.trim()) {
        this.reviewError = 'Заполните все поля';
        return;
      }

      try {
        const token = localStorage.getItem('authToken');
        await axios.put(`http://localhost:3000/reviews/${this.editingReview.id}`, this.editingReview, {
          headers: { Authorization: `Bearer ${token}` }
        });
        const index = this.reviews.findIndex(r => r.id === this.editingReview.id);
        if (index !== -1) this.reviews.splice(index, 1, this.editingReview);
        this.editingReview = null;
        this.reviewError = '';
      } catch (error) {
        this.reviewError = 'Ошибка при сохранении отзыва.';
        console.error('Save review error:', error);
      }
    },
    async deleteReview(id) {
      if (!confirm('Вы уверены, что хотите удалить этот отзыв?')) return;

      try {
        const token = localStorage.getItem('authToken');
        await axios.delete(`http://localhost:3000/reviews/${id}`, {
          headers: { Authorization: `Bearer ${token}` }
        });
        this.reviews = this.reviews.filter(review => review.id !== id);
      } catch (error) {
        this.reviewError = 'Ошибка при удалении отзыва.';
        console.error('Delete review error:', error);
      }
    },
    async deleteRequest(id) {
      if (!confirm('Вы уверены, что хотите удалить эту заявку?')) return;

      try {
        const token = localStorage.getItem('authToken');
        await axios.delete(`http://localhost:3000/requests/${id}`, {
          headers: { Authorization: `Bearer ${token}` }
        });
        this.requests = this.requests.filter(request => request.id !== id);
      } catch (error) {
        this.error = 'Ошибка при удалении заявки.';
        console.error('Delete request error:', error);
      }
    },
    formatDate(dateString) {
      const date = new Date(dateString);
      return date.toLocaleString('ru-RU', {
        day: '2-digit',
        month: '2-digit',
        year: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
      });
    },
    logout() {
      localStorage.removeItem('authToken');
      this.$router.push('/admin/login');
    }
  },
  mounted() {
    this.fetchRequests();
    this.fetchReviews();
  }
};
</script>

<style scoped>
.admin-panel {
  width: 100%;
  min-height: 100vh;
  background-color: #f5f7fa;
  font-family: 'Nekst', sans-serif;
  padding: 2rem;
}

.panel-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 3vh;
}

.panel-header h1 {
  font-family: 'Nekst-SemiBold', sans-serif;
  font-size: clamp(2rem, 3.5vw, 4rem);
  color: #1a202c;
}

.panel-header button {
  padding: 0.5rem 1.5rem;
  background-color: #e53e3e;
  color: #fff;
  border: none;
  border-radius: 5px;
  font-family: 'Nekst-Medium', sans-serif;
  font-size: clamp(1rem, 1.2vw, 1.2rem);
  cursor: pointer;
  transition: background-color 0.3s;
}

.panel-header button:hover {
  background-color: #c53030;
}

.requests-section h2,
.reviews-section h2 {
  font-family: 'Nekst-SemiBold', sans-serif;
  font-size: clamp(1.5rem, 2.5vw, 3rem);
  color: #1a202c;
  margin-bottom: 2vh;
}

.requests-table,
.reviews-table {
  width: 100%;
  border-collapse: collapse;
  background-color: #fff;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  margin-bottom: 2rem;
}

.requests-table th,
.requests-table td,
.reviews-table th,
.reviews-table td {
  padding: 1rem;
  text-align: left;
  font-family: 'Nekst-Light', sans-serif;
  font-size: clamp(0.9rem, 1vw, 1rem);
  color: #4a5568;
}

.requests-table th,
.reviews-table th {
  background-color: #f7fafc;
  font-family: 'Nekst-Medium', sans-serif;
  color: #1a202c;
}

.requests-table tr:nth-child(even),
.reviews-table tr:nth-child(even) {
  background-color: #f9fafb;
}

.requests-table tr:hover,
.reviews-table tr:hover {
  background-color: #edf2f7;
}

.delete-btn {
  padding: 0.3rem 0.8rem;
  background-color: #e53e3e;
  color: #fff;
  border: none;
  border-radius: 5px;
  font-family: 'Nekst-Light', sans-serif;
  font-size: clamp(0.8rem, 1vw, 0.9rem);
  cursor: pointer;
  transition: background-color 0.3s;
  margin-right: 0.5rem;
}

.delete-btn:hover {
  background-color: #c53030;
}

.edit-btn {
  padding: 0.3rem 0.8rem;
  background-color: #5552e8;
  color: #fff;
  border: none;
  border-radius: 5px;
  font-family: 'Nekst-Light', sans-serif;
  font-size: clamp(0.8rem, 1vw, 0.9rem);
  cursor: pointer;
  transition: background-color 0.3s;
  margin-right: 0.5rem;
}

.edit-btn:hover {
  background-color: #4542c8;
}

.review-form {
  margin-bottom: 2rem;
}

.form-group {
  margin-bottom: 1rem;
}

.form-group label {
  display: block;
  font-family: 'Nekst-Medium', sans-serif;
  font-size: clamp(1rem, 1.2vw, 1.2rem);
  color: #4a5568;
  margin-bottom: 0.5rem;
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #e0e0e0;
  border-radius: 5px;
  font-family: 'Nekst-Light', sans-serif;
  font-size: clamp(1rem, 1.2vw, 1.2rem);
  color: #1a202c;
  outline: none;
  transition: border-color 0.3s;
}

.form-group input:focus,
.form-group textarea:focus {
  border-color: #5552e8;
}

button {
  padding: 0.5rem 1.5rem;
  background-color: #5552e8;
  color: #fff;
  border: none;
  border-radius: 5px;
  font-family: 'Nekst-Medium', sans-serif;
  font-size: clamp(1rem, 1.2vw, 1.2rem);
  cursor: pointer;
  transition: background-color 0.3s;
}

button:disabled {
  background-color: #a0a0a0;
  cursor: not-allowed;
}

button:hover:not(:disabled) {
  background-color: #4542c8;
}

.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 1rem;
  margin-top: 2rem;
}

.loading,
.error {
  font-family: 'Nekst-Light', sans-serif;
  font-size: clamp(1rem, 1.2vw, 1.2rem);
  color: #4a5568;
  text-align: center;
  margin: 2rem 0;
}

.error {
  color: #e53e3e;
}

/* Адаптивность для мобильных устройств */
@media (max-width: 768px) {
  .admin-panel {
    padding: 1rem;
  }

  .panel-header h1 {
    font-size: clamp(1.5rem, 5vw, 2rem);
  }

  .panel-header button {
    font-size: clamp(0.9rem, 3vw, 1rem);
    padding: 0.5rem 1rem;
  }

  .requests-section h2,
  .reviews-section h2 {
    font-size: clamp(1.2rem, 4vw, 1.8rem);
  }

  .requests-table th,
  .requests-table td,
  .reviews-table th,
  .reviews-table td {
    font-size: clamp(0.8rem, 2.5vw, 0.9rem);
    padding: 0.5rem;
  }

  .delete-btn,
  .edit-btn {
    font-size: clamp(0.7rem, 2vw, 0.8rem);
    padding: 0.2rem 0.5rem;
  }

  .form-group input,
  .form-group textarea {
    font-size: clamp(0.9rem, 3vw, 1rem);
  }

  button {
    font-size: clamp(0.9rem, 3vw, 1rem);
    padding: 0.5rem 1rem;
  }

  .pagination button {
    font-size: clamp(0.8rem, 2.5vw, 0.9rem);
    padding: 0.4rem 0.8rem;
  }
}
</style>