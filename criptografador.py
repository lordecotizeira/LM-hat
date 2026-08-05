#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ferramenta de Criptografia AES para Scripts Python
Uso: python3 crypt_aes.py
"""

import os
import sys
import base64
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import secrets

def gerar_chave():
    """Gera uma chave AES-256 (32 bytes)."""
    return AESGCM.generate_key(bit_length=256)

def criptografar_script(arquivo_entrada, chave=None, salvar_como=None):
    if not os.path.exists(arquivo_entrada):
        print(f"Erro: arquivo '{arquivo_entrada}' não encontrado.")
        return None

    with open(arquivo_entrada, 'r', encoding='utf-8') as f:
        codigo_original = f.read().encode('utf-8')

    if chave is None:
        chave = gerar_chave()
    elif isinstance(chave, str):
        # Se fornecer string, converte para 32 bytes usando hash
        import hashlib
        chave = hashlib.sha256(chave.encode()).digest()

    aesgcm = AESGCM(chave)
    nonce = secrets.token_bytes(12)  # 96 bits para GCM
    dados_criptografados = aesgcm.encrypt(nonce, codigo_original, None)

    # Combina nonce + dados criptografados
    payload = nonce + dados_criptografados
    payload_b64 = base64.b64encode(payload).decode()

    # Gera o script stub que descriptografa e executa
    stub = f'''import base64, os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

chave = {repr(chave)}
payload_b64 = "{payload_b64}"

payload = base64.b64decode(payload_b64)
nonce = payload[:12]
dados_criptografados = payload[12:]

aesgcm = AESGCM(chave)
codigo = aesgcm.decrypt(nonce, dados_criptografados, None)
exec(codigo.decode())
'''
    if salvar_como is None:
        nome_base, ext = os.path.splitext(arquivo_entrada)
        salvar_como = f"{nome_base}_crypt.py"

    with open(salvar_como, 'w', encoding='utf-8') as f:
        f.write(stub)

    print(f"✅ Script criptografado com sucesso: {salvar_como}")
    print(f"🔑 Chave utilizada (guarde se quiser): {base64.b64encode(chave).decode()}")
    return salvar_como

def main():
    print("\n=== CRIPTOGRAFIA AES PARA SCRIPTS PYTHON ===")
    arquivo = input("Arquivo a criptografar (ex: exemplo.py): ").strip()
    if not arquivo:
        print("Nenhum arquivo informado.")
        return

    usar_chave_propria = input("Deseja fornecer uma senha/chave? (s/N): ").strip().lower()
    chave = None
    if usar_chave_propria == 's':
        senha = input("Digite a senha (qualquer string): ").strip()
        import hashlib
        chave = hashlib.sha256(senha.encode()).digest()
    else:
        chave = gerar_chave()

    salvar = input("Nome do arquivo de saída (Enter para automático): ").strip()
    if salvar == "":
        salvar = None

    criptografar_script(arquivo, chave, salvar)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nCancelado.")
        sys.exit(0)