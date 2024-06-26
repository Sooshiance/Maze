import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import apiCall from '../utils/Axios';

function SingleTask() {

    let todoid = useParams();

    const [task, setTask] = useState([]);

    console.log(todoid.id);

    useEffect(() => {
        async function fetchToDo() {
            try {
                const res = await apiCall.get(`task/${todoid.id}`)
                setTask(res?.data);
            } catch (error) {
                console.log(error);
            }
        }
        fetchToDo();
    }, [])

    return (
        <div>
            <h3>
                {task.title}
            </h3>
        </div>
    )
}

export default SingleTask
