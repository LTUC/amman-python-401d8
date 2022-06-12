
import Head from 'next/head'
import Header from './components/Header';
import { useState } from 'react';
import QuestionForm from "./components/QuestionForm";
import responses from '../data';
import EightBall from "./components/EightBall";
import QuestionTable from './components/QuestionTable'
import Footer from './components/footer'
const Home = () => {
  const [counter, setCounter] = useState(0);
 const [answersList,setAnswerList]=useState([])
  const [latestAnswer, setLatestAnswer] = useState('');
  const title = "8 Magic Ball";


   const QuestionHandler = (e) => {
     e.preventDefault();
     setCounter(counter + 1);

     const randomReply = responses[Math.floor(Math.random() * responses.length)];

    //  alert(randomReply);
    //  console.log(randomReply);
     let answer = {
       question: e.target.question.value,
       reply: randomReply,
       id: answersList.length,
     };
     setAnswerList([...answersList, answer]);
     console.log(answersList);
     setLatestAnswer(randomReply);



   };

  return (
    <>
      <Header counter={counter} title={title} />
      {answersList.length <= 5 ? (
        <QuestionForm QuestionHandler={QuestionHandler} />
      ) : (
        <></>
      )}
      <EightBall reply={latestAnswer} />

      <QuestionTable answersList={answersList} />
      <Footer latestAnswer={latestAnswer} />
    </>
  );
}

export default Home
