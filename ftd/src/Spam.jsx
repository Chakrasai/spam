import React, { useState } from 'react';
import axios from 'axios';
import './Spam.css';
import Spamemail from './Spamemail';

function Spam() {
    const [text, setText] = useState('');
    const [result, setResult] = useState(null);
    const [loading, setLoading] = useState(false);

    async function detectSpam(ev) {
        ev.preventDefault();
        if (!text.trim()) {
            alert('Please enter some text.');
            return;
        }
        setLoading(true);
        try {
            const response = await axios.post('http://localhost:4000/detectspam', { text });
            setResult(response.data.result);
            console.log(result)
        } catch (error) {
            console.error('Failed to fetch:', error);
            alert('Something went wrong. Please try again.');
        } finally {
            setLoading(false);
        }
    }

    return (
        <div className="spam-detector-container">
            <h2 className="header">Spam Detection Tool</h2>
            <form onSubmit={detectSpam}>
                <div className="input-area">
                    <input 
                        type="text" 
                        className="text-input" 
                        placeholder="Enter text here..." 
                        value={text} 
                        onChange={(ev) => setText(ev.target.value)}
                    />
                    <button type="submit" className="detect-button" disabled={loading}>
                        {loading ? 'Detecting...' : 'Detect'}
                    </button>
                </div>
            </form>
            {result && <Spamemail result={result} />}
        </div>
    );
}

export default Spam;
