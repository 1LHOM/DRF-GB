import React from 'react'
const ToDoItem = ({todo_user}) => {
    return (
        <tr>
            <td>
                {todo_user.first_name}
            </td>
            <td>
                {todo_user.last_name}
            </td>
            <td>
                {todo_user.birthday_year}
            </td>
            <td>
                {todo_user.email}
            </td>
        </tr>
    )
}
const ToDo_User_List = ({todo_users}) => {
    return (
        <table>
            <th>
                First name
            </th>
            <th>
                Last Name
            </th>
            <th>
                Birthday year
            </th>
            <th>
                Email
            </th>

            {todo_users.map((todo_user) => <ToDoItem todo_user={todo_user} />)}
        </table>
    )
}
export default ToDo_User_List
