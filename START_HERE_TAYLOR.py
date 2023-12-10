import torch
print(torch.cuda.is_available())

import os
from dotenv import load_dotenv


from openai import OpenAI
# get version of OpenAI
#print version of openai

import torch
import sklearn
import scipy


load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

OpenAI(api_key=openai_api_key)

import vec2text
