import torch
print(torch.cuda.is_available())

import os
from dotenv import load_dotenv

import openai
print(openai.__version__)
from openai import OpenAI

import torch
import sklearn
import scipy


load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

OpenAI(api_key=openai_api_key)

import vec2text
