import Post from "../models/Post.js";
import {spawn} from 'child_process';
/** For Getting Post Analysis */
posts=await Post.find();
export const getPostStats=(req,res)=>{
    const childPython=spawn('python',['sentimentAnalysis.py',JSON.stringify({...posts})]);
    childPython.stdout.on('data',(data)=>{
        console.log(`Output of dataPreprocessing.py file: ${data}`)
    });
    childPython.stderr.on('data',(err)=>{
        console.log(`Error of python file: ${err}`);
    });
};
  