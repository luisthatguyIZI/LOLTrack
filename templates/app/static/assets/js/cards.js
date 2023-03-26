const cards = document.querySelectorAll('.card');

const onDragStart = (event) => {
  console.log('dragging the element');
  const cardId = event.target.getAttribute('id');
  event.dataTransfer.setData('text/plain', cardId);
  setTimeout(() =>{
    event.target.style.visability='hidden';
  },50)
};

const onDragEnd = (event) => {
  event.target.style.visability='visiable';
  console.log('end the drag');
};

cards.forEach((card) => {
  card.addEventListener('dragstart', onDragStart);
  card.addEventListener('dragend', onDragEnd);
});