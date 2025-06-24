from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def add_cors(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["https://sleekwithdeals-ui.onrender.com"],  # <- exact React frontend port
        allow_methods=["*"],
        allow_headers=["*"],
    )
