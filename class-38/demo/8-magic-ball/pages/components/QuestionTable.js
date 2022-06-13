export default function QuestionTable({ answersList }) {
  return (
    <table className="w-1/2 mx-auto my-4">
      <thead>
        <th className="border border-blue-600">No</th>
        <th className="border border-blue-600">Question</th>
        <th className="border border-blue-600">responses</th>
      </thead>
          <tbody>
              {
              answersList.map(answer => {
                  return (
                    <tr>
                      <td className="border border-blue-600">{answer.id}</td>
                      <td className="border border-blue-600">
                        {answer.question}
                      </td>
                      <td className="border border-blue-600">{answer.reply}</td>
                    </tr>
                  );
              })
            }
              </tbody>
    </table>
    //   <h1> try 01</h1>
  );
}