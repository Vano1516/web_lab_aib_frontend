import React, { useState } from "react";

const Posts = () => {
  const [posts, setPosts] = useState([
    {id: 1, username: 'Ivan Vinograd', text: 'I like vinograd', tags: ['vinograd', 'life', ], likes: 0 },
    { id: 2, username: 'Roma Gvozd', text: 'I want to sleep', tags: ['sleep', 'life'], likes: 0 },
    // Добавьте другие посты по аналогии
  ]);

  const [newPost, setNewPost] = useState({ username: '', text: '', tags: '' });
  const [selectedTags, setSelectedTags] = useState([]);
  const [filteredPosts, setFilteredPosts] = useState(posts);

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
      const tagsArray = newPost.tags.split(',').map((tag) => tag.trim());
      setPosts((prevPosts) => [
        ...prevPosts,
        {
          id: prevPosts.length + 1,
          username: newPost.username,
          text: newPost.text,
          tags: tagsArray,
          likes: 0,
        },
      ]);
      setNewPost({ username: '', text: '', tags: '' });
    }
  };

  const handleTagClick = (tag) => {
    if (selectedTags.includes(tag)) {
      setSelectedTags(selectedTags.filter((selectedTag) => selectedTag !== tag));
    } else {
      setSelectedTags([...selectedTags, tag]);
    }
  };

  // Обновляем фильтрованные посты при изменении выбранных тэгов
  React.useEffect(() => {
    if (selectedTags.length === 0) {
      setFilteredPosts(posts);
    } else {
      const filtered = posts.filter((post) =>
        post.tags.some((tag) => selectedTags.includes(tag))
      );
      setFilteredPosts(filtered);
    }
  }, [selectedTags, posts]);

  const allTags = Array.from(new Set(posts.flatMap((post) => post.tags)));

  return (
    <div>
      <h1>Новости</h1>
      {filteredPosts.map((post) => (
        <div key={post.id} className="card-body">
            <p>
              <span className='m-2' >{post.username}</span> 
            </p>
            <p>
              <span className='m-2' >{post.text}</span> 
            </p>
          <p>
              <span className='m-2' >(Tags: {post.tags.join(', ')})</span> 
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
        <input
          type="text"
          placeholder="Tags "
          value={newPost.tags}
          onChange={(e) => setNewPost({ ...newPost, tags: e.target.value })}
        />
        <button onClick={handleAddPost}>Add Post</button>
      </div>
      <div  className='m-2'>
        <h2>Теги</h2>
        {allTags.map((tag) => (
          <span
            key={tag}
            onClick={() => handleTagClick(tag)}
            style={{
              cursor: 'pointer',
              textDecoration: selectedTags.includes(tag) ? 'underline' : 'none',
            }}
          >
            {tag}{' '}
          </span>
        ))}
      </div>
    </div>
  );
};
export default Posts;