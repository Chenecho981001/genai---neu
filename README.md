# Vector DB Chatbot with RAG

### link to youtube https://youtu.be/rAVvjdwP_S4

### Project Overview

**Domain:** A chatbot designed to assist users with information about Vector DB  
**Scope:** Provide detailed responses and resources regarding Vector DB and its capabilities.

### Installation Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-repository.git
   cd your-repository

3. **Create a virtual environment**
   
   pipenv shell
   pipenv install

4. **Set up environment variables**

   Create a .env file in the root directory and add your Pinecone and OpenAI API keys:
      env
      Copy code
      PINECONE_API_KEY=your-pinecone-api-key
      OPENAI_API_KEY=your-openai-api-key

5. **Fetch data from the Vector DB website**
   
   bash
   Copy code

6. **Fetch data from the Vector DB website**
   
   mkdir vector-db-docs
   wget -r -P vector-db-docs -E https://www.vector-db.com/docs
   streamlit run app.py

7. **Fetch data from the Vector DB website**
    
   Pre-process the data by running the ingest_docs.py script

8. **Start the Streamlit app**
    
   streamlit run run_llm.py


