import subprocess
import os
nome_ferramenta = ""
nome_ferramenta_essa = ""
os.system(f"pkg install rust binutils openssl libffi python -y")
os.system("pkg install python-cryptography")
os.system("clear")
print("baixando dependencias")
subprocess.run(["pip", "install", "discord.py"])
subprocess.run(["pkg", "install", "python", "rust", "binutils", "openssl", "libffi", "termux-api", "-y"])
subprocess.run(["pip", "install", "psutil", "numpy"])
subprocess.run(["termux-setup-storage"])
if nome_ferramenta_essa:
    os.system(f"rm {nome_ferramenta_essa}")
if nome_ferramenta and nome_ferramenta_essa:
    os.system(f"mv {nome_ferramenta} {nome_ferramenta_essa}")