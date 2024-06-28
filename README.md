# FactCheck-LLM
This repository contains the performance results of different LLMs on fact-checking tasks.

## Download Ollama

If you are using linux

    curl -L https://ollama.com/download/ollama-linux-amd64 -o ollama
    chmod +x ollama

you may need to run command for ollama commands linux
    
    ./ollama

Or check Mac App or Windows app on: https://ollama.com/download/

## Download Models

Check from this libray: https://ollama.com/library

    ollama pull gemma2:9b
    ollama pull gemma2:27b
    ollama pull mixtral:8x7b
    ollama pull mixtral:8x22b
    ollama pull mistral:7b
    ollama pull llama3:8b
    ollama pull llama3:70b
    ollama pull qwen2:7b
    ollama pull qwen2:72b
    ollama pull phi3:3.8b
    ollama pull phi3:14b

Note: You may need to run as ./ollama pull gemma2:9b on Linux


# Generate predictions 
Before starting run ollama server:

On Mac: 

    run ollama app from applications

On linux:
    
    ollama serve

After
    
    # generate predictions 
    python main.py gemma2:9b

output will be in data folder.

    # how many completed
    wc -l data/results_gemma2:9b.json

    # realtime watch
    tail -f data/results*.json 
    
