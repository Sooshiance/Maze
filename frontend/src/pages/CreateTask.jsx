import React, { useState, useEffect } from 'react'
import apiCall from '../utils/Axios';

function CreateTask() {

    const [title, setTitle] = useState("");
    const [content, setContent] = useState("");
    const [active, setActive] = useState(true);
    // how to pass multi parameters to a useState?
    const [status, setStatus] = useState(1);

    const createtask = async (title, content, active, status) => {
        try {
            // send request to the backend
            const { data, status_code } = await apiCall.post('create/task/', {
                title, content, active, status
            })
            if (status_code == 201) {
                console.log("success!");
                return "success"
            }
        } catch (error) {
            console.log(error?.detail);
        }
    }

    const handleSubmit = (e) => {

        e.preventDefault();

        const { data, error } = createtask(title, content, active, status)

        if (!error) {
            console.log("successful!");
        } else {
            console.log(error?.detail);
        }
    }

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <label htmlFor="">Title</label>
                <br />
                <input type="text" name="" id="title" value={title} onChange={(e) => setTitle(e.target.value)} />
                <br />
                <label htmlFor="">Content</label>
                <br />
                <input type="text" name="" id="content" value={content} onChange={(e) => setContent(e.target.value)} />
                <br />
                <label htmlFor="">Active</label>
                <br />
                <input type="checkbox" id='active' name="" value={active} onChange={(e) => setActive(e.target.value)} />
                <br />
                <label htmlFor="">Status</label>
                <br />
                {/* how show to user an appropriate respons, instead of numbers */}
                <input type='radio' name="" id='status' value={status} onChange={(e) => setStatus(e.target.value)} />
                <br />
                <button type="submit">
                    Submit
                </button>
            </form>
        </div>
    )
}

export default CreateTask
