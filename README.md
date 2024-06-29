# FactCheck-LLM
This repository contains the performance results of different LLMs on fact-checking tasks.

This document outlines the step-by-step instructions required to run Ollama.
## Download Ollama

If you are using linux

    curl -L https://ollama.com/download/ollama-linux-amd64 -o ollama
    chmod +x ollama

On Linux, you may need to run commands as follows:
    
    ./ollama

Or check Mac App or Windows app on: https://ollama.com/download/

## Download Models

Check from this libray: https://ollama.com/library

To download models, use the following commands:

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

To generate predictions:

    python main.py gemma2:9b
    python main.py gemma2:27b
    python main.py mixtral:8x7b
    python main.py mixtral:8x22b
    python main.py mistral:7b
    python main.py llama3:8b
    python main.py llama3:70b
    python main.py qwen2:7b
    python main.py qwen2:72b
    python main.py phi3:3.8b
    python main.py phi3:14b

The output will be saved in the data folder.

 ## Check Output

To see how many predictions were completed:

    wc -l data/results_gemma2:9b.json

For real-time monitoring:

    tail -f data/results*.json 


## Generate Metrics

To generate accuracy and F1 scores:

    python score_generator.py gemma2:9b





