import React from 'react';
import Todo from "./Todo";
const TodoList = ({todos, setTodos, userName}) => {
    return (
        <div className="todo-contianer">
            <ul className="todo-list">
                {todos.map((todo) => (
                    <Todo userName={userName} todos={todos} setTodos={setTodos} todo={todo} text={todo.text}/>
                ))}
            </ul>
        </div>
    );
};
export default TodoList;