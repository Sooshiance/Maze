import React, { useState, useEffect } from 'react'
import { useParams } from 'react-router-dom';
import apiCall from '../utils/Axios';

function UpdateTask() {

    let todoid = useParams();

    const [title, setTitle] = useState("");
    const [content, setContent] = useState("");
    const [active, setActive] = useState(true);
    const [status, setStatus] = useState(1);

    return (
        <div></div>
    )
}

export default UpdateTask
