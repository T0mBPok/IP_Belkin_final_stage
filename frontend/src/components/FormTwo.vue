<template>
  <section class="form2">
    <div class="collage">
      <img src="/images/Rectangle 95.png" alt="Safety helmet" />
      <img src="/images/Rectangle 96.png" alt="Safety gloves" />
    </div>
    <div class="ride">
      <div class="ride-text">
        <h2>ИП "Белкин" - это надежный партнер в оценке условий труда</h2>
        <p>
          Мы предоставляем услуги по проведению специальной оценки условий труда и
          оформлению документов по охране труда для вашего предприятия
        </p>
        <button class="detalis-button">Узнать больше</button>
      </div>
    </div>
  </section>

  <section class="form3">
    <h2>Преимущества сотрудничества с ИП "Белкин"</h2>
    <div class="benefits">
      <div class="benefit-item">
        <div class="benefit-icon-background">
          <img src="/images/fire-icon.png" alt="Fire icon" class="benefit-icon" />
        </div>
        <h3>Опыт и <br/> надежность</h3>
        <p>Компании обладает многолетним опытом в сфере охраны труда, что делает нас надежным партнером.</p>
      </div>
      <div class="benefit-item">
        <div class="benefit-icon-background">
          <img src="/images/thumbs-up-icon.png" alt="Thumbs up icon" class="benefit-icon" />
        </div>
        <h3>Индивидуальный подход</h3>
        <p>Каждому клиенту мы предлагаем решение, разработанное под его задачи и потребности.</p>
      </div>
      <div class="benefit-item">
        <div class="benefit-icon-background">
          <img src="/images/bolt-icon.png" alt="Bolt icon" class="benefit-icon" />
        </div>
        <h3>Профессиональный коллектив</h3>
        <p>Наши специалисты постоянно повышают свои квалификации, чтобы предоставлять качественные услуги.</p>
      </div>
    </div>
  </section>

</template>

<script>
export default {
  name: 'FormTwo'
}
</script>

<style scoped>
.form2 {
  width: 100%;
  height: fit-content;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10vh 7vh;
  background-color: #f5f7fa;
  font-family: 'Nekst', sans-serif;
  margin-top: 0;
  position: relative;
  min-height: 50vh;
  overflow: visible;
  gap: 3rem; /* Фиксированный отступ между collage и ride */
}

.collage {
  display: flex;
  gap: 1.5vmin; /* Пропорциональный отступ между изображениями */
  position: relative;
  min-height: 40vh;
  width: fit-content;
}

.collage img {
  width: clamp(200px, 30vw, 750px); /* Пропорциональное масштабирование с ограничениями */
  height: clamp(200px, 30vw, 750px);
  border-radius: 15px;
  object-fit: cover;
  background-color: #fff;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  transition: transform 0.1s;
}

.collage img:nth-child(2) {
  position: absolute;
  width: 60%; /* Пропорционально первому изображению */
  height: auto; /* Пропорционально первому изображению */
  transform: translate(45%, 20%); /* Фиксированное смещение относительно первого изображения */
  right: 0;
  border-radius: 3vw;
  bottom: auto; /* Убрано фиксированное позиционирование снизу */
  top: 45%; /* Привязка к центру первого изображения */
  z-index: 1;
}

.ride {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  max-width: 50%;
}

.ride-text {
  width: 90%;
}

.ride-text h2 {
  font-family: 'Nekst-SemiBold', sans-serif;
  font-size: clamp(2.2rem, 3.3vw, 3.5rem); /* Пропорциональный размер шрифта */
  color: black;
  margin: 0 0 1vh 0;
  font-weight: bold;
  line-height: 1.1;
}

.ride-text p {
  font-family: 'Nekst-Thin', sans-serif;
  font-size: clamp(1.3rem, 1.7vw, 1.7rem); /* Пропорциональный размер шрифта */
  color: #4a5568;
  margin: 0 0 25px 0;
  line-height: 1.2;
}

.detalis-button {
  background-color: #fff;
  color: #5552E8;
  border: none;
  padding: clamp(8px, 1.3vw, 100px) clamp(20px, 2.5vw, 250px); /* Пропорциональные отступы */
  border-radius: 25px;
  cursor: pointer;
  font-size: clamp(0.9rem, 1.7vw, 1.7rem); /* Пропорциональный размер шрифта */
  transition: 0.7s;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.7);
  font-family: 'Nekst-Light', sans-serif;
}

.detalis-button:hover {
  /*background-color: #f5f7fa;*/
  box-shadow: 0 4px 12px rgba(0, 0, 0, 1.0);
}



/* Стили нового раздела*/
.form3 {
  width: 100%;
  padding: 10vh 7vh;
  background-color: #fff;
  font-family: 'Nekst', sans-serif;
  text-align: center;
}

.form3 h2 {
  font-family: 'Nekst-SemiBold', sans-serif;
  font-size: clamp(1.5rem, 3.3vw, 3.5rem);
  color: #1a202c;
  margin-bottom: 5vh;
  font-weight: bold;
  line-height: 1.1;


}

.form3 h3 {
  font-family: 'Nekst-SemiBold', sans-serif;
  font-size: clamp(1.2rem, 2.3vw, 1.9rem);
  color: #1a202c;
  margin-bottom: 2vw;
}

.benefits {
  display: flex;
  justify-content: space-around;
  gap: 2rem;
  flex-wrap: wrap;
}

.benefit-item {
  max-width: 30%;
  padding: 2rem;
  display: flex; /* Добавляем Flexbox */
  flex-direction: column; /* Устанавливаем вертикальное расположение */
  align-items: center;
}

.benefit-icon-background{
  width: clamp(50px, 7.5vw, 110px);
  height: clamp(50px, 7.5vw, 110px);
  border-radius: 50%;
  background-color: #fff;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.7);
  display: grid;
  place-items: center;
  margin-bottom: 3vw;

}
.benefit-item img:nth-child(1){
  width: clamp(20px, 4vw, 80px);
  height: auto;
  
}

.benefit-icon {
  width: clamp(20px, 5vw, 80px);
  height: auto;
  
}

.benefit-item p {
  font-family: 'Nekst-Thin', sans-serif;
  font-size: clamp(0.9rem, 1.7vw, 1.5rem);
  color: #4a5568;
  line-height: 1.4;
}

@media (max-width: 768px) {
  .form2 {
    display: flex;
    flex-direction: column;
    padding: 5vh 3vh;
    padding-bottom: 0;
    min-height: auto;
    gap: 0rem;
  }

  .collage {
    right: 15%;
    margin-right: 0;
    justify-content: center;
    width: 100%;
    min-height: 30vh;
    overflow: visible;
  }

  .collage img {
    width: clamp(150px, 40vw, 200px);
    height: clamp(150px, 40vw, 200px);
    position: relative;
    transform: none;
    border-radius: 10px;
    transition: transform 0.5s ease, opacity 0.5s ease;
    opacity: 0; /* Для анимации появления */
  }

  .collage img:nth-child(1) {
    transform: rotate(-5deg);
    animation: fadeIn 0.5s ease forwards;
  }

  .collage img:nth-child(2) {
    position: absolute;
    width: clamp(150px, 40vw, 200px);
    height: clamp(150px, 40vw, 200px);
    transform: rotate(5deg);
    top: 0;
    border-radius: 20%;
    left: 50%;
    margin-left: calc(clamp(150px, 40vw, 200px) / 4); /* Смещение вправо */
    animation: fadeIn 0.5s ease 0.3s forwards;
  }

  @keyframes fadeIn {
    from {
      opacity: 0;
      transform: translateY(20px) rotate(-5deg);
    }
    to {
      opacity: 1;
      transform: rotate(-5deg);
    }
  }

  .ride {
    max-width: 100%;
    margin-left: 0;
    align-items: center;
  }

  .ride-text {
    width: 100%;
    text-align: center;
  }

  .ride-text h2 {
    font-size: clamp(1.5rem, 5vw, 2rem);
    margin-bottom: 1rem;
  }

  .ride-text p {
    font-size: clamp(1rem, 3.5vw, 1.3rem);
    margin-bottom: 1.5rem;
  }

  .detalis-button {
    font-size: clamp(0.9rem, 3vw, 1rem);
    padding: clamp(8px, 2vw, 12px) clamp(20px, 5vw, 30px);
  }

  .form3 {
    padding: 5vh 3vh;
  }

  .form3 h2 {
    font-size: clamp(1.5rem, 5vw, 2rem);
    margin-bottom: 3vh;
  }

  .form3 h3 {
    font-size: clamp(1rem, 4vw, 1.5rem);
    margin-bottom: 1rem;
  }

  .benefits {
    gap: 1rem;
  }

  .benefit-item {
    max-width: 100%;
    padding: 1.5rem;
    transition: transform 0.3s ease;
  }

  .benefit-item:hover {
    transform: scale(1.02);
  }

  .benefit-icon-background {
    width: clamp(60px, 15vw, 80px);
    height: clamp(60px, 15vw, 80px);
    margin-bottom: 1.5rem;
  }

  .benefit-icon {
    width: clamp(30px, 8vw, 40px);
  }

  .benefit-item p {
    font-size: clamp(1rem, 3.5vw, 1.3rem);
  }
}

</style>