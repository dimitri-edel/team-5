// Button for testing a request to the backend
import React from 'react';
import {axiosReq} from '../api/axiosConfig';

const TestButton = () => {
    const handleClick = () => {
        axiosReq.get('test/')
            .then(response => {
                console.log(response.data);
            });
    };

    return (
        <button onClick={handleClick}>Test</button>
    );
}

export default TestButton;