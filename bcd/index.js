const express = require('express');
const axios = require('axios');
const cors = require('cors');


const app = express();

app.use(cors({ credentials: true, origin: 'http://localhost:3000' })); 
app.use(express.json());

const flaskapi = 'https://spam-deployment.onrender.com/detectspam';


app.get('/',(req,res)=>{
    res.send('hello world , running backend!');
})

app.post('/detectspam', async (req, res) => {
    const { text } = req.body;

    if(!text){
        return res.status(400).json({error:"No text provided"})
    }
    try{    
        const response = await axios.post(flaskapi,{text});
        const result  = response.data;
        res.json(response.data)
        console.log(response.data)

    }
    catch(error){
        console.error('error communicating with api',error.message);
        res.status(500).json({error:"interval server error"})

    }
    
})

app.listen(4000, () => {
    console.log('Server is running on port 4000');
});