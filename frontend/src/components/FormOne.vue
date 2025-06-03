<template>
  <section class="form1">
    <div class="image-container">
      <img class="image" src="/images/image_145.png" alt="Hero image" />
      <div class="blur-strip strip-1"></div>
      <div class="blur-strip strip-2"></div>
      <div class="blur-strip strip-3"></div>
      <div class="blur-strip strip-4"></div>
      <div class="blur-strip strip-5"></div>
      <div class="blur-strip strip-6"></div>
    </div>
    <div class="hero-text">
      <h1>СПЕЦИАЛЬНАЯ ОЦЕНКА УСЛОВИЙ ТРУДА</h1>
      <p>ИП “Белкин” - это надежная компания по оценке условий труда</p>
      <button class="hero-button">Подробнее о компании</button>
      <img class="angle" src="/images/angle.png" alt="Стрелочка" />
    </div>
  </section>
</template>

<script>
export default {
  name: 'FormOne'
}
</script>

<style scoped>
.form1 {
  width: 100%;
  height: fit-content;
  max-height: 93vh;
  overflow: hidden;
  margin-top: 7vh;
  position: relative; /* Добавляем для общего контекста */
}

.image-container {
  width: 100%;
  overflow: hidden;
  height: 93vh;
  display: block;
  position: relative; /* Делаем контейнер позиционированным для .blur-strip */
}

.image {
  width: 100%;
  height: 100%;
  max-height: 93vh;
  object-fit: cover;
  object-position: center;
}

.blur-strip {
  position: absolute;
  top: 0;
  width: 17%;
  height: 100%; /* Высота будет ограничена .image-container */
  border-right: 2px solid white;
  border-left: 2px solid white;
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  z-index: 1;
}

/* Позиционирование каждой полосы */
.strip-1 {
  left: 5%;
}

.strip-2 {
  width: 5%;
  left: 22%;
  border-right: 0px solid white;
  border-left: 0px solid white;
}

.strip-3 {
  left: 27%;
}

.strip-4 {
  right: 27%;
}

.strip-5 {
  width: 5%;
  right: 22%;
  border-right: 0px solid white;
  border-left: 0px solid white;
}

.strip-6 {
  right: 5%;
}

.hero-text {
  z-index: 5;
  position: absolute;
  top: 35%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
  color: white;
  width: 90%;
  text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.5);
}

.hero-text h1 {
  margin-top: 20vh;
  font-size: clamp(32px, 4.5vw, 100px);
  font-family: 'Nekst-Bold', sans-serif;
  text-shadow: 0px 0px 8px rgba(0, 0, 0, 1);
  margin-bottom: 20px;
}

.hero-text p {
  font-family: 'Nekst-Light', sans-serif;
  color: black;
  border-radius: 50px;
  background-color: white;
  text-align: center;
  margin: auto;
  width: 90%;
  max-width: 880px;
  height: auto;
  padding: 10px 20px;
  font-size: clamp(14px, 2vw, 18px);
}

.hero-button {
  background-color: #5552e8;
  color: white;
  border: none;
  padding: 2vw 4vw;
  font-size: clamp(1.2rem, 1.7vw, 2rem);
  border-radius: 15px;
  cursor: pointer;
  transition: background-color 0.3s;
  font-family: 'Nekst-Light', sans-serif;
  height: auto;
  margin-top: 20vh;
  width: auto;
  min-width: 200px;
}

.angle {
  width: 7%;
  z-index: 5;
  position: absolute;
  top: 110%;
  left: 50%;
  transform: translateX(-50%) rotate(90deg);
  height: auto;
}

/* Адаптивность для мобильных устройств */
@media (max-width: 768px) {
  .form1 {
    max-height: 60vh;
    margin-top: 5vh;
  }

  .image-container {
    height: 60vh;
  }

  .image {
    max-height: 60vh;
  }

  .blur-strip {
    width: 15%;
  }

  .strip-1 {
    left: 5%;
  }

  .strip-2 {
    width: 10%;
    left: 20%;
  }

  .strip-3 {
    left: 27%;
  }

  .strip-4 {
    right: 27%;
  }

  .strip-5 {
    z-index: 5;
    width: 10%;
    right: 20%;
  }

  .strip-6 {
    right: 5%;
  }

  .hero-text {
    
    width: 95%;
  }

  .hero-text h1 {
    margin-top: 20vh;
    font-size: clamp(20px, 6vw, 50px);
    margin-bottom: 10px;
  }

  .hero-text p {
    font-size: clamp(12px, 3vw, 16px);
    padding: 8px 15px;
    max-width: 100%;
  }

  .hero-button {
    margin-top: 10vh;
    padding: 3vw 6vw;
    font-size: clamp(1rem, 3vw, 1.5rem);
    min-width: 150px;
  }

  .angle {
    width: 10%;
    top: 105%;
  }
}
</style>