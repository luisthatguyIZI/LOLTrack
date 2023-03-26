const bank = document.querySelector('.bank');

const onDropCard = (event) => {
  event.preventDefault();
  const cardId = event.dataTransfer.getData('text/plain');
  const card = document.getElementById(cardId);
  bank.appendChild(card);
};

bank.addEventListener('drop', onDropCard);
bank.addEventListener('dragover', (event) => event.preventDefault());
