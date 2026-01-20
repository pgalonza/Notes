---
title: "Artificial intelligence"
date: 2026-01-19T18:35:59+03:00
draft: false
description: "Explore AI insights, trends, and practical applications in our curated notes — stay ahead with expert analysis on machine learning, generative AI, and ethical challenges."
summary: "A collection of concise, up‑to‑date notes on artificial intelligence: from core algorithms and LLMs to real‑world use cases and ethical debates, updated regularly for professionals and enthusiasts."
aliases:
  - /development/ai/ai/
---

{{< toc >}}


## NLP

1. NLU (Natural Language Understanding)
2. DM (Dialog Management)
3. NLG (Natural Language Generation)

1. Tokenization
2. Stop words
3. Lemmatization and stemming
4. Bag of words
5. TF-IDF (term frequency-inverse document frequency)
6. Intent recognition

## Machine Learning Approaches

- Prompt Engineering
- Zero-shot learning
- Few-shot learning
- Fine-tuning
- Retrieval-Augmented Generation (RAG)

## LLM (Large Language Model)

### LLM Deployment Tools

- [Ollama](https://ollama.com/)
- [vLLM](https://vllm.ai/)
- [llama.cpp](https://github.com/ggml-org/llama.cpp)
- [LM Studio](https://lmstudio.ai/)
- [koboldcpp](https://github.com/LostRuins/koboldcpp)

### LLM UI Clients

- [Cherry Studio](https://www.cherry-ai.com/)
- [Open WebUI](https://openwebui.com/)
- [Msty Studio](https://msty.ai)
- [Librechat](https://www.librechat.ai)
- [Chatbox](https://chatboxai.app)
- [AnythingLLM](https://anythingllm.com/)
- [GPT4All](https://www.nomic.ai/gpt4all)
- [Jan.ai](https://www.jan.ai)
- [Text Generation Web UI](https://github.com/oobabooga/text-generation-webui)

### Frameworks

- [LangChain](https://github.com/hwchase17/langchain)
- [Llamaindex](https://www.llamaindex.ai/)

### Prompt engineering

- Ask Clarifying Questions: Instruct the model to ask follow‑up questions if any part of the prompt is unclear — this prevents misinterpretation and ensures alignment with user intent.
- Provide Examples: Include specific examples to demonstrate the desired output format and style — concrete samples help the model grasp nuances and replicate the expected result.
- Request Reasoning: For complex tasks, ask the model to explain its reasoning step‑by‑step — this increases transparency, allows error tracing, and improves trust in the output.
- Role Definition: Specify the role or persona you want the model to adopt — a defined role (e.g., “expert linguist”) guides tone, depth, and perspective consistently.
- Context Setting: Provide relevant background information to guide the response — context anchors the model’s knowledge and ensures responses are situationally appropriate.
- Define Subtasks: Create specific subtasks for each component — breaking down the prompt into actionable steps helps the model manage complexity and deliver complete answers.
- Identify Main Components: Break the task into logical sections — clear segmentation improves organization and ensures all aspects of the request are addressed systematically.
- Output Structure: Define the structure and format of the desired response — specify headings, bullet points, tables, or paragraph count to match your preferred layout.
- Shadow Prompting: Embed indirect cues and hints within the main prompt to guide the model toward the desired outcome without explicit instructions — subtle framing can shape tone and focus effectively.
- Set Constraints: Define boundaries such as word count, tone, or prohibited topics — constraints prevent irrelevant or overly verbose outputs and keep responses focused.
- Specify Audience: Indicate who the output is for (e.g., beginners, experts) — this adjusts complexity, terminology, and explanatory depth accordingly.
- Use Positive Framing: Frame requests in a constructive way (e.g., “include key benefits” vs. “don’t forget benefits”) — positive phrasing yields more cooperative and complete responses.
- Prioritize Elements: Rank components by importance (e.g., “focus first on X, then Y”) — this guides the model to emphasize critical aspects when trade‑offs arise.
- Include Validation Criteria: State how the output will be evaluated (e.g., accuracy, clarity, creativity) — this aligns the model’s priorities with your quality standards.
- Leverage Iteration: Design prompts to allow follow‑up refinements (e.g., “provide a draft, then we’ll improve it”) — iterative prompting often yields higher‑quality final results.
- Metaprompting: Instruct the model to reflect on its own reasoning or prompt‑design process (e.g., “Explain how you interpreted this prompt” or “Suggest improvements to this request”) — this enhances self‑awareness and helps refine future prompts.
- Prompt Templates: Save effective prompts as reusable templates with placeholders (e.g., [TOPIC], [AUDIENCE]) — this ensures consistency, speeds up workflow, and allows quick adaptation for similar tasks.


## Resources

- Developing Apps with GPT-4 and ChatGPT (Olivier Caelen, Marie-Alice Blete)
- RAG-Driven Generative AI (Denis Rothman)
- Prompt Engineering for Generative AI: Future-Proof Inputs for Reliable AI Outputs at Scale (James Phoenix & Mike Taylor)
