import React from 'react';
import logo from './logo.svg';
import './App.css';
import AuthorList from './components/ToDoApp.js'
import axios from 'axios'


class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'todo_users': []
        }
    }
    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/todo_users/')
            .then(response => {
                const todo_users = response.data
                this.setState({
                    'todo_users': todo_users
                    }
                )
            }).catch(error => console.log(error))
        }
    render () {
        return (
            <div>
                <AuthorList todo_users={this.state.todo_users} />
            </div>
        )
    }
}

export default App;
