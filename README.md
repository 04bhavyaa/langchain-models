# LangChain Models

This repository contains implementations of various **Language Models (LLMs)**, **Chat Models** and **Embedding Models** using LangChain. It demonstrates different model integrations for LLMs and embeddings, including OpenAI, Hugging Face, Google, Sentence Transformers and Anthropic.

## 📂 Directory Structure
```plaintext
04bhavyaa-langchain-models/
├── README.md                  # Project documentation
├── requirements.txt           # Required dependencies
├── LLMs/
│   └── llm_demo.py            # Basic LLM demonstration
├── chat-models/               # Various chat models
│   ├── chatmodel_anthropic.py # Anthropic's Claude integration
│   ├── chatmodel_google.py    # Google Gemini (PaLM) integration
│   ├── chatmodel_hf_api.py    # Hugging Face API integration
│   ├── chatmodel_hf_local.py  # Local Hugging Face LLM integration
│   └── chatmodel_openai.py    # OpenAI ChatGPT integration
└── embedding-models/          # Embedding models for similarity search
    ├── document_similarity.py # Cosine similarity for document search
    ├── embedding_hf_local.py  # Local Hugging Face embeddings
    ├── embedding_openai_docs.py # OpenAI document embeddings
    └── embedding_openai_query.py # OpenAI query embeddings
```

## ⚡ Tech Stack
- **LangChain** (Core framework for chaining LLMs)
- **OpenAI API** (ChatGPT & Embeddings)
- **Anthropic API** (Claude models)
- **Google Generative AI** (Gemini/PaLM models)
- **Hugging Face** (Transformer-based LLMs & embeddings)
- **Scikit-learn** (Cosine similarity for document search)
- **Pandas & NumPy** (Data processing utilities)

## 🧠 Theory Behind LangChain Models
- **LLMs:** These are large-scale neural networks trained on vast text corpora. LangChain provides a structured way to interact with them.
- **Chat Models:** Variants of LLMs optimized for dialogue, such as OpenAI's ChatGPT, Claude, and Gemini.
- **Embedding Models:** Convert text into high-dimensional vectors to perform similarity search, useful for document retrieval and semantic search.

## 🔧 Setup Instructions
### 1. Clone the repository:
```
git clone https://github.com/yourusername/04bhavyaa-langchain-models.git
cd 04bhavyaa-langchain-models
```
### 2. Create and activate a virtual environment:
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3. Install dependencies:
```
pip install -r requirements.txt
```
### 4. Set Up Environment Variables
Create a `.env` file and add your API keys:
```
OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
GOOGLE_API_KEY=your_google_api_key
HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_key
```
### 5. Run the Models
Example usage for document similarity:
```bash
python embedding-models/document_similarity.py
```
Sample Output:
![image](https://github.com/user-attachments/assets/924c9bd4-bef3-4ac6-8e94-7c2034c0b42d)

---
💡 **Contributions are welcome!** Feel free to fork, open issues, or submit PRs.
