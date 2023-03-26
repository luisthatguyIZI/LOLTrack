const columns = document.querySelectorAll('.column');
const colours=['green','aquamarine','yellow','orange','orangered','red']

const onDragOver = (event) => {
  event.preventDefault();
};

const onDrop = (event) => {
  event.preventDefault();
  const id = event.dataTransfer.getData('text/plain');
  console.log('id:', id); // <-- add this line
  const draggedCard = document.getElementById(id);
  if (draggedCard) {
    event.target.appendChild(draggedCard);
    console.log(`the current id is ${id}`);
    console.log('dropped the element');
  } else {
    console.error(`Could not find element with id ${id}`);
  }
};

columns.forEach((column,index) => {
  const label = column.querySelector('.label');
  label.style.backgroundColor = colours[index];
  column.ondragover = onDragOver;
  column.ondrop = onDrop;
});