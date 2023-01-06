from flask import Blueprint, render_template
from modules import memory, cpu, capacity
import time

dashboard = Blueprint(__name__, "dashboard")

@dashboard.route("/")
def home():
    return render_template("dashboard.html", cpu=cpu.cpu(), ram=memory.memory())
