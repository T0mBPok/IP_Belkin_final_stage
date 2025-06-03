<template>
  <div class="services-page">
    <AppHeader />
    <section class="services-content">
      <h1>Услуги компании <br /> ИП “Белкин”</h1>
      <div class="text-box">
        <div class="ride-text">
          <h2>Специальная оценка <br /> условий труда</h2>
          <p>
            Специальная оценка условий труда является единым комплексом последовательно осуществляемых мероприятий по идентификации вредных и (или) опасных факторов производственной среды и трудового процесса и оценке уровня их воздействия на работника с учетом отклонения их фактических значений от установленных уполномоченным Правительством Российской Федерации федеральным органом исполнительной власти нормативов (гигиенических нормативов) условий труда и применения средств индивидуальной и коллективной защиты работников.
          </p>
        </div>
        <img src="/images/helmet.png" alt="Каска" class="helmet-image" />
      </div>
      <div class="price-container">
        <div class="price">
          <h3>Периодичность проведения <br/> специальной оценки <br/> условий труда</h3>
          <h1 class="big-text">НЕ РЕЖЕ, <br/> ЧЕМ 1 РАЗ <br/> В 5 ЛЕТ</h1>
        </div>
        <div class="left-price">
          <h3>Штраф за нарушение требований охраны труда</h3>
          <h4>Для юридических лиц:</h4>
          <h1 class="big-text">60 - 70 тыс. руб.</h1>
          <h4>Для физических лиц:</h4>
          <h1 class="big-text">5 - 10 тыс. руб.</h1>
        </div>
      </div>
    </section>
  </div>
  <FormFive/>
  <AppFooter/>
</template>

<script>
import AppHeader from '@/components/AppHeader.vue';
import FormFive from '@/components/FormFive.vue';
import AppFooter from '@/components/AppFooter.vue';

export default {
  name: 'ServicesPage',
  components: {
    AppHeader,
    FormFive,
    AppFooter
  }
};
</script>

<style scoped>
.services-page {
  width: 100%;
  height: fit-content;
  
  overflow: hidden;
  margin-top: 7vh;
  position: relative;
  font-family: 'Nekst', sans-serif;
}

.services-content {
  padding: 10vh 7vh;
  text-align: center;
}

.services-content h1 {
  font-family: 'Nekst-SemiBold', sans-serif;
  font-size: clamp(2rem, 3.5vw, 4rem);
  color: black;
  margin-bottom: 2vh;
  line-height: 1;
}

.services-content h2 {
  font-family: 'Nekst-SemiBold', sans-serif;
  font-size: clamp(1.5rem, 2.5vw, 3.5rem);
  color: black;
  margin-bottom: 2vh;
  line-height: 1;
}

.services-content p {
  font-family: 'Nekst-Light', sans-serif;
  font-size: clamp(1rem, 1.5vw, 1.5rem);
  color: #4a5568;
}

/* Стили для text-box */
.text-box {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 2rem;
  margin-top: 4vh;
}

.ride-text {
  flex: 1;
  text-align: left;
}

.helmet-image {
  flex: 0 0 auto;
  width: clamp(250px, 35vw, 500px);
  height: auto;
  margin-left: 5vh;
  object-fit: cover;
}

/* Стили для price-container */
.price-container {
  display: flex; /* Используем Flexbox для горизонтального расположения */
  justify-content: space-between; /* Распределяем столбцы с равным расстоянием */
  align-items: center; /* Выравниваем по верхнему краю */
  gap: 4rem; /* Отступ между столбцами */
  margin-top: 6vh; /* Отступ сверху от text-box */
}

.price,
.left-price {
  flex: 1; /* Каждый столбец занимает половину доступного пространства */
  text-align: left; /* Выравниваем текст по левому краю */
}

.price h3,
.left-price h3 {
  text-align: center;
  font-family: 'Nekst-Regular', sans-serif;
  font-size: clamp(1.2rem, 2vw, 1.8rem);
  color: black;
  margin-bottom: 2.5vh;
}

.left-price h4 {
  text-align: center;
  font-family: 'Nekst-Light', sans-serif;
  font-size: clamp(1rem, 1.5vw, 1.5rem);
  color: #4a5568;
  
}

.big-text {
  text-align: center;
  font-family: 'Nekst-SemiBold', sans-serif;
  font-size: clamp(3rem, 4vw, 5rem);
  color: black;
  line-height: 1;
  margin-bottom: 2vh;
}

/* Адаптивность для мобильных устройств */
@media (max-width: 768px) {
  .services-page {
    max-height: none;
    margin-top: 5vh;
  }

  .services-content {
    padding: 5vh 3vh;
  }

  .services-content h1 {
    font-size: clamp(1.5rem, 5vw, 2rem);
  }

  .services-content h2 {
    font-size: clamp(1.2rem, 4vw, 1.8rem);
  }

  .services-content p {
    font-size: clamp(0.9rem, 3vw, 1.1rem);
  }

  .text-box {
    flex-direction: column;
    gap: 1.5rem;
    margin-top: 2vh;
  }

  .ride-text {
    text-align: center;
  }

  .price{
    text-align: center;
  }

  .helmet-image {
    width: clamp(150px, 50vw, 300px);
    margin: 0;
  }

  .price-container {
    flex-direction: column; /* Переключаем на вертикальное расположение */
    gap: 1rem; /* Увеличиваем отступ между столбцами */
    margin-top: 4vh;
  }

  .price h3,
  .left-price h3 {
    font-size: clamp(1rem, 3vw, 1.5rem);
  }

  .left-price h4 {
    font-size: clamp(0.9rem, 2.5vw, 1.2rem);
  }

  .big-text {
    font-size: clamp(1.5rem, 4vw, 2.5rem);
  }
}
</style>