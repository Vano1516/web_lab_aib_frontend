import React, { useState } from "react";

const Posts = () => {
  const [posts, setPosts] = useState([
    { id: 1, username: 'Ivan Vinograd', text: 'I like vinograd', likes: 0 },
    { id: 2, username: 'Roma Gvozd', text: 'I want to sleep', likes: 0 },
  ]);

  const [newPost, setNewPost] = useState({ username: '', text: '' });

  const handleLike = (postId) => {
    setPosts((prevPosts) =>
      prevPosts.map((post) =>
        post.id === postId ? { ...post, likes: post.likes + 1 } : post
      )
    );
  };

  const handleDelete = (postId) => {
    setPosts((prevPosts) => prevPosts.filter((post) => post.id !== postId));
  };

  const handleAddPost = () => {
    if (newPost.username && newPost.text) {
      setPosts((prevPosts) => [
        ...prevPosts,
        {
          id: prevPosts.length + 1,
          username: newPost.username,
          text: newPost.text,
          likes: 0,
        },
      ]);
      setNewPost({ username: '', text: '' });
    }
  };

  return (
    <div>
        <h1>Новости</h1>
      {posts.map((post) => (
        <div key={post.id}  className="card-body">
            <p>
              <span className='m-2' >{post.username}</span> 
            </p>
            <p>
              <span className='m-2' >{post.text}</span> 
            </p>
          <button onClick={() => handleLike(post.id)}>
            Like ({post.likes})
          </button>
          <button onClick={() => handleDelete(post.id)}>Delete</button>
        </div>
      ))}
      <div  className='m-2'>
        <h2>Добавить новый пост</h2>
        <input
          type="text"
          placeholder="Username"
          value={newPost.username}
          onChange={(e) => setNewPost({ ...newPost, username: e.target.value })}
        />
        <input
          type="text"
          placeholder="Post Text"
          value={newPost.text}
          onChange={(e) => setNewPost({ ...newPost, text: e.target.value })}
        />
        <button onClick={handleAddPost}>Add Post</button>
      </div>
    </div>
  );
};
export default Posts;