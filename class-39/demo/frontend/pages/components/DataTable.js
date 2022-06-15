import axios from "axios"
import { useEffect, useState } from "react"

function DataTable({token}) {
    const [data, setData] = useState([])
    
    const getData = async ()=>{
        const config={
            headers:{
                'Authorization': `Bearer ${token}`
            }
        }
        const data = await axios.get("http://127.0.0.1:8000/api/v1/todo-list",config)
        return data.data;
    }

    useEffect(()=>{
        getData().then(res=>{setData(res)})
    },[])
    return (
        <table className="w-1/2 mx-auto my-4">
            <thead>
                <tr>
                    <th className="border border-blue-600">Id</th>
                    <th className="border border-blue-600">Title</th>
                    <th className="border border-blue-600">Content</th>
                </tr>
            </thead>
            <tbody>
                 {
                    data.map((item, index) => {
                       return  <tr key={index}>
                        <td className="border border-blue-600">{item.id}</td>
                        <td className="border border-blue-600">{item.title}</td>
                        <td className="border border-blue-600">{item.content}</td>
                    </tr>
                    })
                } 
            </tbody>
        </table>

    )
}

export default DataTable