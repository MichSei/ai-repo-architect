from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.Client()
collection = client.get_or_create_collection(name="repo_code")


def index_code_files(code_files):

    documents = []
    ids = []
    metadatas = []

    for i, path in enumerate(code_files):

        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()

            chunks = [
                content[i:i+1200]
                for i in range(0, len(content), 1200)
            ][:5]

            for chunk in chunks:
                documents.append(chunk)
                ids.append(f"{i}_{len(ids)}")
                metadatas.append({"path": path})

        except:
            continue

    embeddings = model.encode(documents).tolist()

    collection.add(
        documents=documents,
        embeddings=embeddings,
        ids=ids,
        metadatas=metadatas
    )


def search_code(query):

    query_embedding = model.encode([query]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=5
    )

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]

    combined = []

    for doc, meta in zip(documents, metadatas):
        combined.append({
            "code": doc,
            "path": meta["path"]
        })

    return combined