from flask import Flask, Blueprint, render_template
from modules import memory, cpu, capacity
import time
import random
import json

def statusCheck():
    with open('serverswitch.json', 'r') as openfile:
        json_object = json.load(openfile)
    
    if json_object["status"] == "on":
        return True
    elif json_object["status"] == "off":
        return False

api = Blueprint(__name__, "api")

@api.route("/")
def home():
    if statusCheck():
        return render_template("api.html")
    else:
        return "API is down..."

@api.route("/switch")
def switch():
    with open('serverswitch.json', 'r') as openfile:
        json_object = json.load(openfile)

    if json_object["status"] == "on":
        objects = {
            "status": "off"
        }
        with open("serverswitch.json", "w") as outfile:
            json.dump(objects, outfile)
        return "Server is now turning off..."
    elif json_object["status"] == "off":
        objects = {
            "status": "on"
        }
        with open("serverswitch.json", "w") as outfile:
            json.dump(objects, outfile)
        return "Server is now turning on..."
    else:
        return "Error[001]: JSON is corrupt..."

@api.route("/random/number/<min>/<max>")
def randomNumber(min, max):
    if not statusCheck():
        return "API is down..."
    else:
        return str(random.randint(int(min), int(max)))

@api.route("/random/word/<lenght>")
def randomWord(lenght):
    if not statusCheck():
        return "API is down..."
    else:
        a = ""
        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for x in range(int(lenght)):
            a += random.choice(letters)
        return str(a)

@api.route("/token/available")
def availableTokens():
    if not statusCheck():
        return "API is down..."
    else:
        return str(0)

@api.route("/get-cpu-usage-percent")
def getcpupercent():
    return str(cpu.cpu()) + "%"

@api.route("/get-cpu-usage")
def getcpu():
    return str(cpu.cpu())

@api.route("/get-ram-usage-percent")
def getram():
    return str(memory.memory()) + "%"

@api.route("/get-disk-usage-percent")
def getdisk():
    return str(capacity.percent()) + "%"
