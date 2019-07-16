# -*- coding: utf-8 -*-
from flask import Blueprint, request, redirect, jsonify
from application import app, db


route_index = Blueprint('index_page', __name__)


@route_index.route("/index")
def index():
    return "Mina Api V1.0~~"