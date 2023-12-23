import React from 'react';
import { Link } from 'react-router-dom';

const users = [
  { id: 1, name: 'Ivan' },
  { id: 2, name: 'Dmitriy' },
];

const UserList = () => {
  return (
    <div>
      <h1>User List</h1>
      <ul>
        {users.map((user) => (
          <li key={user.id}>
            <Link to={`/users/${user.id}`}>{user.name}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default UserList;