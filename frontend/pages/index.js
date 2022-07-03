import React, {useState} from "react";

export default function Home() {
    const [value, setValue] = useState();

    const handleClick = async () => {
        const response = await fetch("http://localhost:5000/api/")
        const data = await response.json()
        setValue(data.body)
    }

    return (
        <div className={"w-full flex flex-col items-center"}>
            <h1 className={"text-2xl"}>This is the homepage</h1>
            <h3>Press the button to get some data from the backend server</h3>
            <button className={"bg-blue-200 p-2 rounded-lg"} onClick={handleClick}>Get data</button>
            <h1>{value}</h1>
        </div>
    )
}
