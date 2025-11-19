const saveToStorage = (key , data) => {

    localStorage.setItem(key , JSON.stringify(data));
}

const getFromStorage = (key) => {

    const data =  localStorage.getItem(key);

    return data ? JSON.parse(data) : []
}


const todoInput = document.querySelector("#todo-input");
const addBtn = document.querySelector("#add-btn");
const todoList = document.querySelector("#todo-list");

let todos = getFromStorage("todos") || [] ;


// let todos = getFromStorage("todos");

//  function to show the todos on UI 
function renderTodos() {

  todoList.innerHTML = "";

  todos.forEach((todo, index) => {
    const li = document.createElement("li");
    li.className = "todo-item";

    const span = document.createElement("span");
    span.innerText = todo;

// adding edit functionality
    const editBtn = document.createElement("button");
    editBtn.className = "edit-btn";
    editBtn.innerText = "Edit";

    editBtn.addEventListener("click", () => {
    
      const newText = prompt("Edit your todo:", todo);
      if (newText !== null && newText.trim() !== "") {
        todos[index] = newText.trim(); 
        saveToStorage("todos", todos);
        renderTodos(); 
      }
    });


// adding delete functionality
    const delBtn = document.createElement("button");
    delBtn.className = "delete-btn";
    delBtn.innerText = "Delete";

    delBtn.addEventListener("click", () => {
      todos.splice(index, 1);
      saveToStorage("todos", todos);
      renderTodos();
    });

    li.appendChild(span);
    li.appendChild(delBtn);
    li.appendChild(editBtn)
    todoList.appendChild(li);
  });
}



//adding todo
addBtn.addEventListener('click' , () => {
    try {
        const text = todoInput.value.trim()
        console.log(text);

        if(text === "") return alert('Please enter a task ')
         todos.push(text);
        saveToStorage('todos' , todos);
        renderTodos()
        todoInput.value="";
    }
    catch {
        console.log('error');
    }
})


renderTodos()
