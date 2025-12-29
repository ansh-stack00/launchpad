from src.pipelines.load_documents import load_doc
from langchain_text_splitters import RecursiveCharacterTextSplitter


# splitting the docs into smalle chunks 

def chunk_docs(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=700,
        chunk_overlap=300,
    )

    return splitter.split_documents(documents)

if __name__=="__main__":
# loading the pdf file 
    docs = load_doc()

# chunking the file into small chunk 
    chunks = chunk_docs(docs)
    print(f"Total chunks created: {len(chunks)}\n")