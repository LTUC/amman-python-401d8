

function Form({questionAskedHandler}) {
  return (
    <>
    <form onSubmit={questionAskedHandler} className="flex w-1/2 p-2 mx-auto bg-gray-200">
        <input name="question" className="flex-auto pl-2" type={"text"} placeholder={"Ask us a question !"} />
        <button className="px-4 py-2 bg-gray-400 text-gray-50">Ask</button>
    </form>
    </>
  )
}

export default Form