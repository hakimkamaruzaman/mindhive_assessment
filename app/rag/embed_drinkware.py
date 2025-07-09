from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
import os

# Set file path
data_path = "app/rag/data/drinkware.txt"
output_path = "app/rag/faiss_drinkware_index"

# Read and split text
with open(data_path, "r", encoding="utf-8") as file:
    content = file.read()

# Split into smaller chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=30
)
texts = splitter.split_text(content)
documents = [Document(page_content=text) for text in texts]

# Use HuggingFace embedding model
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Create FAISS vector store
vectorstore = FAISS.from_documents(documents, embeddings)

# Save vector store
os.makedirs(output_path, exist_ok=True)
vectorstore.save_local(output_path)

print(f"✅ Embedding complete. Vector store saved to: {output_path}")
