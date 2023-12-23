import React, {useState} from "react";

const Counter =() => {

    const [count,setCount] = useState(0);


    const handleInkrement = () =>{
        setCount(count+1);
        console.log(count);
    };

    const handleDecrement = () =>{
        setCount(count-1);
        console.log(count); 
    };

    return (
    <>
        <h1>{count}</h1>
        <button onClick={handleInkrement}>+ 1</button>
        <button onClick={handleDecrement}>- 1</button>
    </>
    );

};

export default Counter;