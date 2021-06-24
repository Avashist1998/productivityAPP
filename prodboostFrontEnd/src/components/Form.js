import React from "react";
import TodoList from "./TodoList";
import Async from 'react-async';

const Form = (props) => {
    const inputTextHandler = (e) => {
        props.setInputItem(e.target.value);
    };
    const inputDateHandler = (e) => {
        props.setInputDate(e.target.value);
    };
    async function addItem(userName, itemName, date) {
      const url = "http://192.168.1.129:8000/list/?" + new URLSearchParams({"userName":userName});
      const data = {"name": itemName, "d": date};
      var response = await fetch(url, {method: "POST",
          headers: {
              'Content-Type': 'application/json;charset=UTF-8'
          },
          body: JSON.stringify(data),
      });
      console.log(response)
      return response.json();
  }
    let submitTodoHandler = async (e) => {
        e.preventDefault();
        const data = await addItem(props.userName, props.inputItem, props.inputDate);
        var inputId = data.data[0].id;
        props.setTodos([ ...props.todos, {text: props.inputItem, completed: false, id: inputId}]);
        props.setInputItem("");
    };
    return (
      <Async>
    <form id="inputform">
      <input value={props.inputItem} onChange={inputTextHandler} type="text" className="todo-input" />
      <button onClick={submitTodoHandler} className="todo-button" type="submit">
        <i className="fas fa-plus-square"></i>
      </button>
      <div className="select">
        <input value={props.inputDate} onChange={inputDateHandler} type="date" placeholder="mm-dd-yyyy"  defaultValue="01-30-2021" min="01-01-1990" max="01-01-2050"></input>
      </div>
    </form>
    </Async>
    )
};
export default Form;
