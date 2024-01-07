from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader

from langchain_community.embeddings import GPT4AllEmbeddings
from langchain_community.vectorstores import Chroma


def retriever(question):

#loader = WebBaseLoader("https://lilianweng.github.io/posts/2023-06-23-agent/")

    data = 'data_pool\full_data.csv'
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
    all_splits = text_splitter.split_documents(data)

    vectorstore = Chroma.from_documents(documents=all_splits, embedding=GPT4AllEmbeddings())

    # similarity search
    docs = vectorstore.similarity_search(question)

if '__name__' == '__main__':
    question = "startups regarding"
    answer = retriever(question)
    print(answer)