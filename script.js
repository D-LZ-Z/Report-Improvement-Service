let index = 0;

setInterval(() => {
  const slides = document.querySelector('.slides');
  const total = slides.children.length;

  index++;

  if (index >= total) {
    index = 0;
  }

  slides.style.transform = `translateX(-${index * 270}px)`;
}, 2000);
