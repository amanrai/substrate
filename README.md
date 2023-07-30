# substrate
Substrate for RAG

https://app.diagrams.net/#Hamanrai%2FTuliusBackend%2Fmain%2FUntitled%20Diagram.drawio

Connectors for RAG
    - Docs + Images
        - PDF
        - Word
        - HTML
    - Structured Data
        - CSV
        - Excel
        - JSON
        - MySQL
    - Work
        - JIRA
        - Bitbucket
    
Metadata Preprocessor for RAG
    - Docs 
        - Author
        - Title
        - Date of Creation
    - Structured Data
        - Column Names
        - Column Types
    - Work
        - Author
        - Title
        - Date of Creation
        - Parent Post
        - Post type {Story, Epic, Task, Subtask, Bug, Subbug, Commit Message}

Preprocessor for RAG
    - Discover Text (llama_index)
    - Discover Images (PyMuPDF, Pillow)
    - Discover tables (camelot)
    - Add metadata

Processor for RAG
    - Create SQLite Tables for the tables.
    - Chunk
    - v2 - Create RDF for everything.

Embedders
    - BLip-2 QFormer for image + text chunks
    - Resnet for pure images
    - SQLite for tables
    - Sentence Transformers for pure text. (? - maybe use the same as BLip-2)

Storage
    - Write Vectors to Vector DB's
    - Write Metadata to Relational DB
    - Write SQLite to S3/Local storage