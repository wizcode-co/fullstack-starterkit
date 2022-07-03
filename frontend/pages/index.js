import React, {useState} from "react";

export default function Home() {
    const [value, setValue] = useState();

    const handleClick = async () => {
        try{
            const response = await fetch("http://localhost:5000/api/");
            const data = await response.json();
            setValue(data.message);
        } catch(error){
            setValue(error.toString());
        }
    }

    return (
        <div>
            <h1>This is the homepage</h1>
            <h3>Press the button to get some data from the backend server</h3>
            <button onClick={handleClick}>Get data</button>
            <h1>{value}</h1>
        </div>
    )
}
