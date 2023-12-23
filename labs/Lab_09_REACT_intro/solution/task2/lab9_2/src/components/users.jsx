import React, { useState } from "react";

const Posts = () => {

    const [posts, setPosts] = useState([
      { id: 1, username: 'Ivan Vinograd', text: 'I like vinograd', likes: 0 },
      { id: 2, username: 'Roma Gvozd', text: 'I want to sleep', likes: 0 },
    ]);
  
    const handleLike = (postId) => {
      setPosts((prevPosts) =>
        prevPosts.map((post) =>
          post.id === postId ? { ...post, likes: post.likes + 1 } : post
        )
      );
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
          </div>
        ))}
      </div>
    );
  };
export default Posts;