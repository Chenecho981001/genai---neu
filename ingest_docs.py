from dotenv import load_dotenv
import logging
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import ReadTheDocsLoader
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Constants
INDEX_NAME = "mongodb-doc-index"
EMBEDDING_MODEL = "text-embedding-3-small"

# Initialize embeddings
embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)

def ingest_docs():
    """Load documents from the source, split them, and load them into Pinecone."""
    try:
        loader = ReadTheDocsLoader("mongodb-docs/www.mongodb.com")
        raw_documents = loader.load()
        logger.info(f"Loaded {len(raw_documents)} documents")

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=20)
        documents = text_splitter.split_documents(raw_documents)

        for doc in documents:
            new_url = doc.metadata["source"]
            new_url = new_url.replace("mongodb-docs", "https:/")
            doc.metadata.update({"source": new_url})

        logger.info(f"Going to add {len(documents)} documents to Pinecone")
        PineconeVectorStore.from_documents(documents, embeddings, index_name=INDEX_NAME)
        logger.info("Loading to vector store done")
    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    ingest_docs()
