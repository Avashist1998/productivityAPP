import React, {useState, useEffect} from "react";
import './App.css';
import Form from './components/Form'
import TodoList from './components/TodoList'
import Calendar from './components/Calendar'

function App() {
  const userName = "abhay";
  const [inputItem, setInputItem] = useState("");
  const [inputDate, setInputDate] = useState("");
  const[todos, setTodos ] = useState([]);
  let getAllItems = async (e) => {
    const url = "http://192.168.1.129:8000/user/?" + new URLSearchParams({"userName":userName});
    console.log(url)
    const options = {
        method: "GET",
        headers: {
            'Content-Type': 'application/json;charset=UTF-8'
        }
    }
    var response = await fetch(url, options);
    const data = await response.json();
    // console.log(data);
    // console.log(data.data[0].itemNames)
    return data.data[0].itemNames;
  };
  let getId = async (userName, itemName) => {
    const url = "http://192.168.1.129:8000/list/?" + new URLSearchParams({"userName":userName}) + "&" + new URLSearchParams({"itemName":itemName});
    const options = {
        method: "GET",
        headers: {
            'Content-Type': 'application/json;charset=UTF-8'
        }
    }
    var response = await fetch(url)
    const data = await response.json();
    // console.log(data);
    var Inputid = data.data[0].id;
    // console.log(Inputid);
    return Inputid;
  };
  let getAllId = async () => {
    var startTodos = [];
    var array = await getAllItems();
    for (var item in array) {
      // e.preventDefault();
      var id = await getId(userName, array[item]);
      // console.log(item, id);
      startTodos.push({text: array[item], completed: false, id: id});
    }
    setTodos(startTodos);
  };
  useEffect( async () => {
    console.log(getAllId());
    console.log(todos);
  },[]);

  return (
    <div className="App">
      <div style={{ display: "grid", gridTemplateColumns: "repeat(2, 1fr)", gridGap: 20 }}>
      <div><nav role="navigation">
      <div id="menuToggle">
        <input type="checkbox" />
        <span></span>
        <span></span>
        <span></span>
        <ul id="menu">
        <li><input type="radio" id="StudyTime" name="StudyTime" value="1"></input><label for="male">1</label></li>
        <li><input type="radio" id="StudyTime" name="StudyTime" value="3"></input><label for="female">3</label></li>
        <li><input type="radio" id="StudyTime" name="StudyTime" value="5"></input><label for="other">5</label></li>
        </ul>
      </div>
    </nav><header><h1>To-Do List </h1></header><Form inputDate={inputDate} userName={userName} inputItem={inputItem} todos={todos} setTodos={setTodos} setInputItem={setInputItem} setInputDate={setInputDate}/><TodoList userName={userName} todos={todos} setTodos={setTodos}/></div>
      <div><Calendar /></div>
    </div>
    </div>
  );
}

export default App;
