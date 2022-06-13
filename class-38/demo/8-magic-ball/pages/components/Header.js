export default function Header({counter,title}) {

  return (
    <header className="flex justify-between bg-teal-600 py-4 items-center">
      <h1 className="text-4xl mx-1">{title}</h1>
      <p>{counter} Question Added</p>
    </header>
  );
}

// export default Header = () => {
//     return (
//         <>
//             <h1>8 Magic Balls</h1>
//         </>
//     )
    
// }


// let counter = props.counter
// let title = props.title

// {counter,title}=props