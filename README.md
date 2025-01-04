# FactCheck-LLM
This repository contains the performance results of different LLMs on fact-checking tasks.

You can see the results in the [metrics_graph.ipynb](https://github.com/basakbozkurt/FactCheck-LLM/blob/main/metrics_graph.ipynb) notebook.

This document outlines the step-by-step instructions required to run Ollama and includes the code for measuring performance of different LLMs on fact-checking tasks.

# Instructions for Running Ollama
 Follow the installation instructions provided to set it up on your machine.

## Download Ollama

If you are using Linux:

    curl -L https://ollama.com/download/ollama-linux-amd64 -o ollama
    chmod +x ollama

On Linux, you may need to run commands as follows:
    
    ./ollama

Or check Mac App or Windows app on: https://ollama.com/download/

## Download Models

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
    ollama pull command-r:35b
    ollama pull command-r-plus:104b

Note: You may need to run as ./ollama pull gemma2:9b on Linux

For more info on models, see this library: https://ollama.com/library.

# Generate predictions 
Before starting run ollama server:

On Mac: 

    run ollama app from applications

On Linux:
    
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
    python main.py command-r:35b
    python main.py command-r-plus:104b

The output will be saved in the data folder.

 ## Check Output

To see how many predictions were completed:

    wc -l data/results_gemma2:9b.json

For real-time monitoring:

    tail -f data/results*.json 


# Generate Metrics

To generate accuracy and F1 scores:

    python score_generator.py gemma2:9b
    
 # Evaluating Accuracy of LLMs
For a pilot experiment, I chose 1,000 samples for each category from a total pool of 21,152 PolitiFact claims to ensure equal representation. This approach helps us eliminate any bias that might arise from imbalanced data. If I had reflected on the actual distribution of claims, some categories might have been underrepresented, potentially skewing the results and affecting the reliability of our model comparisons. 
In the preprocessing step, I eliminated instances where the models refused to respond.

 ## Models
I selected 11 models from 6 different LLM families, as shown in  Table \ref{tab:models_llm}. This choice is informed by their open-source nature and their representation of the latest advancements in the field.

| **LLM Family** | **Parameter Count**                                                                                                 | **Provider**     | **Release Date**                                                                                                                                  |
|-----------------|---------------------------------------------------------------------------------------------------------------------|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Mixtral         | 8x7B [[1]](https://example.com/mistralaiteamMixtralExperts2023) / 8x22B [[2]](https://example.com/mistralaiteamCheaperBetterFaster2024) | Mistral AI       | 11/12/2023 [[1]](https://example.com/mistralaiteamMixtralExperts2023), 17/04/2024 [[2]](https://example.com/mistralaiteamCheaperBetterFaster2024) |
| Command R       | 35B                                                                                                                | Cohere           | 11/03/2024 [[3]](https://example.com/gomezCommandRetrievalAugmentedGeneration2024)                                                              |
| Llama 3         | 8B/70B                                                                                                            | Meta             | 18/04/2024 [[4]](https://example.com/metaIntroducingMetaLlama)                                                                                  |
| Phi-3           | 8B/14B                                                                                                            | Microsoft        | 21/05/2024 [[5]](https://example.com/bilenkoIntroducingPhi3Redefining2024)                                                                      |
| Qwen-2          | 7B/22B                                                                                                            | Alibaba Cloud    | 07/06/2024 [[6]](https://example.com/qwenteamHelloQwen22024)                                                                                    |
| Gemma 2         | 9B/27B                                                                                                            | Google           | 27/06/2024 [[7]](https://example.com/farabetGemmaNowAvailable2024)                                                                              |

---

### References:
1. [Mixtral Experts 2023](https://example.com/mistralaiteamMixtralExperts2023)
2. [Cheaper Better Faster 2024](https://example.com/mistralaiteamCheaperBetterFaster2024)
3. [Command Retrieval Augmented Generation 2024](https://example.com/gomezCommandRetrievalAugmentedGeneration2024)
4. [Introducing Meta Llama](https://example.com/metaIntroducingMetaLlama)
5. [Introducing Phi-3 Redefining](https://example.com/bilenkoIntroducingPhi3Redefining2024)
6. [Hello Qwen-2 2024](https://example.com/qwenteamHelloQwen22024)
7. [Gemma Now Available](https://example.com/farabetGemmaNowAvailable2024)






