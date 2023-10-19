import streamlit as st


import torch
from transformers import pipeline

generate_text = pipeline(model="databricks/dolly-v2-3b", torch_dtype=torch.bfloat16, trust_remote_code=True, device_map="auto")

output=generate_text("What is biggest fish in the world? Anwer me in less than 10 words. ")

st.write(output)
