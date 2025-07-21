from fastapi import FastAPI, UploadFile, File, Form
from sentence_transformers import SentenceTransformer
from PIL import Image
import io
import torch

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ Allow frontend origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 👈 or ["*"] to allow all
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 🔥 Check for GPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 🚀 Load model on GPU
model = SentenceTransformer("clip-ViT-B-32", device=device)

@app.post("/embed-text")
async def embed_text(text: str = Form(...)):
    emb = model.encode(text, convert_to_tensor=True, normalize_embeddings=True)
    return {"embedding": emb.tolist()}

@app.post("/embed-image")
async def embed_image(file: UploadFile = File(...)):
    img = Image.open(io.BytesIO(await file.read())).convert("RGB")
    emb = model.encode(img, convert_to_tensor=True, normalize_embeddings=True)
    return {"embedding": emb.tolist()}

@app.post("/embed-both")
async def embed_both(text: str = Form(...), file: UploadFile = File(...)):
    img = Image.open(io.BytesIO(await file.read())).convert("RGB")
    img_emb = model.encode(img, convert_to_tensor=True, normalize_embeddings=True)
    txt_emb = model.encode(text, convert_to_tensor=True, normalize_embeddings=True)
    combined = (img_emb + txt_emb) / 2
    return {"embedding": combined.tolist()}

print("CUDA available:", torch.cuda.is_available())
print("Running on:", model.device)
