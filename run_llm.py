from dotenv import load_dotenv
import logging
from typing import Any, Dict, List
from langchain import hub
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from langchain.chains.retrieval import create_retrieval_chain
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

# Load environment variables
load_dotenv()

# Constants
INDEX_NAME = "mongodb-doc-index"
EMBEDDING_MODEL = "text-embedding-3-small"

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run_llm(query: str, chat_history: List[Dict[str, Any]] = []) -> Dict[str, Any]:
    try:
        embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)
        docsearch = PineconeVectorStore(index_name=INDEX_NAME, embedding=embeddings)
        chat = ChatOpenAI(verbose=True, temperature=0)

        rephrase_prompt = hub.pull("langchain-ai/chat-langchain-rephrase")
        retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")

        stuff_documents_chain = create_stuff_documents_chain(chat, retrieval_qa_chat_prompt)
        history_aware_retriever = create_history_aware_retriever(
            llm=chat, retriever=docsearch.as_retriever(), prompt=rephrase_prompt
        )
        qa = create_retrieval_chain(
            retriever=history_aware_retriever, combine_docs_chain=stuff_documents_chain
        )

        result = qa.invoke(input={"input": query, "chat_history": chat_history})
        return result

    except Exception as e:
        logger.error(f"An error occurred during LLM invocation: {e}")
        return {"error": str(e)}

def format_docs(docs) -> str:
    return "\n\n".join(doc.page_content for doc in docs)
