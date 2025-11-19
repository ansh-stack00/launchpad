let counter = 0;

counterDisplay = document.getElementById('counter');

const addBtn = document.getElementById('add');
const subBtn = document.getElementById('subtract');
const resetBtn = document.getElementById('reset')
console.log(counterDisplay)

const updateDisplay = () => {
    counterDisplay.innerText = counter ;
}


// add eventListeners 
addBtn.addEventListener ('click' , () => {
    counter++;
    updateDisplay()
});


subBtn.addEventListener('click' , ()=> {
    counter--;
    updateDisplay();
})

resetBtn.addEventListener('click' , () => {
    counter = 0;
    updateDisplay()
})