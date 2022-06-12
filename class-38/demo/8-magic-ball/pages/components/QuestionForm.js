export default function QuestionForm({ QuestionHandler }) {
  return (
    <form
      className="flex w-1/2 bg-gray-200 mx-auto my-5 p-2"
      onSubmit={QuestionHandler}
    >
      <input
        className="flex-auto p-2"
        name="question"
        placeholder="Ask AQuestion"
      />
      <button className="px-4 py-1 mx-2  bg-gray-500 rounded-full">Ask</button>
    </form>
  );
}