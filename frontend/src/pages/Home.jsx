import React, { useState, useEffect } from 'react';
import { Link, Route, Routes } from 'react-router-dom'
import UpdateTask from './UpdateTask'
import SingleTask from './SingleTask';
import apiCall from '../utils/Axios';
import Table from 'react-bootstrap/Table';

function Home() {
    const [todos, setTodo] = useState([]);

    useEffect(() => {
        async function fetchToDo() {
            try {
                const res = await apiCall.get("tasks/")
                setTodo(res.data);
            } catch (error) {
                console.log(error);
            }
        }
        fetchToDo();
    }, []);

    return (
        <div>

            <Table striped>
                <thead>
                    <tr>
                        <th>#</th>
                        <th>Title</th>
                        <th>Content</th>
                        <th>Compeleted</th>
                        <th>See</th>
                        <th>Edit</th>
                        <th>Delete</th>
                    </tr>
                </thead>
                <tbody>
                    {todos.map((todo) => (
                        <tr id='todos' key={todo.id}>
                            <td>
                                {todo.id}
                            </td>
                            <td>
                                {todo.title}
                            </td>
                            <td>
                                {todo.content}
                            </td>
                            <td>
                                {todo.status}
                            </td>
                            <td>
                                <Link to={`/task/${todo.id}/`}>See</Link>
                            </td>
                            <td>
                                <Link to={`/edit/${todo.id}/`}>Edit</Link>
                            </td>
                            <td>

                            </td>
                        </tr>
                    ))}
                </tbody>
            </Table>
        </div>
    )
}

export default Home
