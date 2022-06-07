
function MagicBall({reply}) {
  return (
    <div className="relative mx-auto my-8 bg-gray-900 rounded-full h-96 w-96">
        <div className="absolute flex items-center justify-content-center w-48 h-48 rounded-full bg-gray-50 top-16 left-16">
        <p className="text-center">{reply}</p>
        </div>
    </div>
  )
}
// function Answer(reply){
//     return <p className="text-center">{reply}</p>
// }
export default MagicBall