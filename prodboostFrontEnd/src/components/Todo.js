import React from 'react';
import Async from 'react-async';

const Todo = ({text, todo, todos, setTodos, userName}) => {
    async function deleteItem(userName, deleteItem) {
        console.log(userName);
        console.log(todo.text);
        const url = "http://192.168.1.129:8000/list/?" + new URLSearchParams({"userName":userName}) + "&" + new URLSearchParams({"itemName":deleteItem});
        const options = {
            method: "DELETE",
            headers: {
                'Content-Type': 'application/json;charset=UTF-8'
            }
        }
        fetch(url, options)
        .then(response => response.json())
        .then(data => {
            console.log('Sucess:', data);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    }
    let deleteHandler = async() => {
        deleteItem(userName, todo.text);
        setTodos(todos.filter((el) => el.id !== todo.id));
    }
    const completeHandler = () => {
        setTodos(todos.map((item) => {
            if (item.id === todo.id) {
                return {
                    ...item, completed: !item.completed
                };
            }
            return item;
        })
        );
    }
    return (
        <div className="todo">
            <Async>
                <li className={`todo-item ${todo.completed ? "completed" : ""}`}>{text}</li>
                <button onClick={completeHandler} className="complete-btn"><i className="fas fa-check"></i></button>
                <button onClick={deleteHandler} className="trash-btn"><i className="fas fa-trash"></i></button>
            </Async>
            
        </div>
    );
};
export default Todo;