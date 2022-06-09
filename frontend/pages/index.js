import React, {useState} from "react";

export default function Home() {
    const [value, setValue] = useState();

    const handleClick = async () => {
        fetch("http://localhost:5000/api/")
            .then((response) => response.json())
            .then((data) => {setValue(data.message)})
            .catch((error) => {setValue(error.toString())})
        // const data = await response.json()
        // console.log(data)
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
