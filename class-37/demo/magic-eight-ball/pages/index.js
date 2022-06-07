import Head from "next/head";
import Header from "./components/Header";
import Form from "./components/Form";
import MagicBall from "./components/MagicBall";
import Footer from "./components/Footer";
import { useState } from "react";


function Home(){
  const [reply, setReply] = useState("Ask me anything....");
  const [question, setQuestion] = useState();

  const questionAskedHandler = (e)=>{
    e.preventDefault();
    const randomReply = Math.random() > .5 ? "Yes": "No";
    setReply(randomReply);
    question = e.target.question.value;
    setQuestion(question)

  }
  return(
        <>
        <Head>
          <title>Welcome to magic eight ball</title>
        </Head>
          <Header/>
          <Form questionAskedHandler={questionAskedHandler}/>
          <MagicBall reply={reply}/>
          <br/>
          <h1 className="text-[#50d71e]">{question}</h1>
          <Footer/>
        </>
       

  )
}
export default Home
