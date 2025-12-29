import os 
from langchain_community.document_loaders import (
    PyPDFLoader, TextLoader, CSVLoader, Docx2txtLoader
)

DATA_PATH = "src/data/raw"

def load_doc():

    documents=[]

    for file in os.listdir(DATA_PATH):
        file_path = os.path.join(DATA_PATH,file)

        if file.endswith(".pdf"):
            documents.extend(PyPDFLoader(file_path).load())

        elif file.endswith(".txt"):
            documents.extend(TextLoader(file_path).load())

        elif file.endswith(".csv"):
            documents.extend(CSVLoader(file_path).load())

        elif file.endswith(".docx"):
            documents.extend(Docx2txtLoader(file_path).load())

    return documents

if __name__ =="__main__":
    docs = load_doc()

    print(f"Loaded {len(docs)} documents\n")
    print(docs[12])