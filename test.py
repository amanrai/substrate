from llama_index import SimpleDirectoryReader
from llama_index.node_parser import SimpleNodeParser
from llama_index.langchain_helpers.text_splitter import TokenTextSplitter
import json
from llama_index.node_parser.extractors import (
    MetadataExtractor,
    TitleExtractor,
    QuestionsAnsweredExtractor
)

documents = SimpleDirectoryReader('/Users/amanrai/Downloads/test').load_data()

text_splitter = TokenTextSplitter(separator=" ", chunk_size=256, chunk_overlap=128)

nodes = SimpleNodeParser(
    text_splitter=text_splitter,
).get_nodes_from_documents(documents)

types = []
for node in nodes:
    types.append(type(node))


print(set(types))