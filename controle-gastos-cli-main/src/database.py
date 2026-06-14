from supabase import create_client
import os

# Sua URL e Chave Secreta do Supabase prontas para o projeto
URL = os.getenv("SUPABASE_URL", "https://tdeicixvfdnlukloxfby.supabase.co")
KEY = os.getenv("SUPABASE_KEY", "sb_secret_BW-ZzcXJIKiX04ykJLvR7A_xxe91j2S")

supabase = create_client(URL, KEY)