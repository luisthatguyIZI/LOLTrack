const bank = document.querySelectorAll('#bank')

const onDropCard= (event) =>{
    const id =event.dataTransfer.getData('id');
    bank.appendChild(document.getElementById(id));
}

bank.ondop=onDropCard;
bank.ondragover=(event) => event.preventDefault();