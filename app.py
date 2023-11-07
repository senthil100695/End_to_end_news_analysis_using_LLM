import streamlit as st
from langchain.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

st.set_page_config(page_title="News Analysis")
st.header('News Analysis Q&A Bot Application')

def get_document(url:str):
    loader = UnstructuredURLLoader(urls=[
        url,
    ])
    data = loader.load()
    split = RecursiveCharacterTextSplitter(
        separators=['\n','.',' '],
        chunk_size =500,
        chunk_overlap = 20
    )

    chunks = split.split_documents(data)
    return chunks

if st.sidebar:
    url = st.text_input('Paste Your Url:')
    st.write(url)
    data = get_document(url)
    for i in range(len(data)):
        st.write(len(data[i].page_content)) 