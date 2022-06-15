import React from 'react'

function Form(submitData) {
  return (
    
    <div className="w-full max-w-xs">

    <form  onSubmit={submitData} className='bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4'>
        <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2" >
                Title
            </label>
            <input type="text" 
                   className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" 
                   placeholder='Todo item title..' 
                   name="title"
                   />
        </div>
        <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2" >
                Contnet
            </label>
            <input type="text" 
                   className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" 
                   placeholder='Todo item content..' 
                   name="content"
                   />
        </div>
        <button type='submit' className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">Add todo</button>
    </form>
</div>
  )
}

export default Form