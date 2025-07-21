# CLIP Embedding API (FastAPI)

This project is a FastAPI server that provides endpoints for generating **text**, **image**, and **combined** (text + image) embeddings using the `clip-ViT-B-32` model from SentenceTransformers.

---

## Requirements

Make sure you have **Python 3.7+** installed.

Install all dependencies using the provided batch file:

```bat
requirementsInstall.bat
```

---

## Running the Server

To start the FastAPI server, simply run:

```bat
start.bat
```

---

## API Access

Once the server is running, you can access the API locally at:

```
http://127.0.0.1:8000
```

The automatic **interactive Swagger UI** is available at:

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### 1. `/embed-text`

* **Method**: POST
* **Body (form)**:

  * `text`: string
* **Returns**: Normalized text embedding

---

### 2. `/embed-image`

* **Method**: POST
* **Body (form-data)**:

  * `file`: image file (JPG, PNG, etc.)
* **Returns**: Normalized image embedding

---

### 3. `/embed-both`

* **Method**: POST
* **Body (form-data)**:

  * `text`: string
  * `file`: image file
* **Returns**: Averaged embedding from both image and text

---

## ⚙️ Notes

* Model used: `clip-ViT-B-32`
* Supports **GPU acceleration** if available (automatically detected).
* CORS is enabled for `*` (can be adjusted in code).

---

## 🧪 Example curl Request

```bash
curl -X POST http://127.0.0.1:8000/embed-text -F "text=A dog playing guitar"
```
