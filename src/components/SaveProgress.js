import React from 'react';
import axios from 'axios';

const SaveProgress = ({ progress }) => {
    const handleSave = async () => {
        const token = localStorage.getItem('token');
        try {
            await axios.post('http://localhost:5000/api/users/progress', {token, progress });
            alert('Progress saved successfully');
        } catch (error) {
            alert(error.response.data.error);
        }
    };

    return <button onClick={handleSave}>Save Progress</button>;
};

export default SaveProgress;