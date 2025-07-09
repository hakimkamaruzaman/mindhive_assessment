from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document
from langchain_core.runnables import RunnableLambda

# Load the FAISS vector store
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_store = FAISS.load_local("app/rag/faiss_drinkware_index", embeddings=embedding_model, allow_dangerous_deserialization=True)

# Create a retriever from the vector store
retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 3})

# LangChain-compatible retriever
def retrieve_docs(inputs: dict) -> list[Document]:
    query = inputs["query"]
    docs = retriever.get_relevant_documents(query)
    return docs

retriever_chain = RunnableLambda(retrieve_docs)
