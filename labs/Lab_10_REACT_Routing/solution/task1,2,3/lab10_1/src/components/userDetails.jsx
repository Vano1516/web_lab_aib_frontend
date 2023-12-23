import React from 'react';
import { useParams } from 'react-router-dom';

const UserDetails = () => {
  const { id } = useParams();

  const user = { id, name: `User ${id}`, additionalInfo: 'Some additional information.' };

  return (
    <div>
      <h1>User Details</h1>
      <p>ID: {user.id}</p>
      <p>Name: {user.name}</p>
      <p>Additional Info: {user.additionalInfo}</p>
    </div>
  );
};

export default UserDetails;