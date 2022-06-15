import Header from "./components/Header";
import Form from "./components/Form";
import DataTable from "./components/DataTable";
import Footer from "./components/Footer";
import axios from "axios";
import { useEffect, useState } from "react";

const Home= () => {
   
  const [token, setToken] = useState(null);

  const userData={
    username: "admin",
    password: "abcd1234"
  }

  useEffect(()=>{
    if (localStorage.token===undefined){
        axios.post("http://127.0.0.1:8000/api/v1/token", userData).then(res=>{
        localStorage.setItem('token', res.data.access)
        })
        setToken(localStorage.getItem("token"))
    }
    setToken(localStorage.getItem("token"))

  }, [])


  const submitData=(e)=>{
    // e.preventDefault();
    const config={
        headers:{
            'Authorization': `Bearer ${token}`
        }
    }
    const data = {
        title: e.target.title.value,
        content: e.target.content.value,
        user:"1"

    }
    axios.post("http://127.0.0.1:8000/api/v1/todo-list",data, config ).then(res=>{
        console.log(res)
        })
    console.log("form is working: ", data)
  }

  return (
    <>
    <Header/>
    {token? <DataTable token={token}/>: <h1>Not authorized</h1>}
    
    <br/>
    <Form submitData={submitData}/>
    <Footer/>
    </>
  )
}

export default Home
