#!/usr/bin/env python

import flask
from flask import Flask
from flask import render_template, request


class Square(object):
    def __init__(self, name, image="", url="#"):
        self.name = name
        self.image = image
        self.url = url



app = Flask(__name__)

@app.route('/')
def index():

    projects = [ 
            [ Square("Jenkins", flask.url_for('static', filename='img/jenkins.png')), 
                Square("Monitoring", "https://avatars0.githubusercontent.com/u/7195757"), 
                Square("DockerHub"), 
                Square("GitHub"), 
                Square("TeamZeus"), 
                Square("Lukapo") 
            ], 
            [ Square("Email"), 
                Square("Ansible"), 
                Square("Servers"), 
                Square("Database"), 
            ], 
#            [ Square("Jenkins", "#000000", "#FFFFFF"), 
#                Square("Jenkins", "#000000", "#FFFFFF"), 
#                Square("Grafana", "#ffffff", "#000000"), 
#                Square("Docker", "#000000", "#FFFFFF"),
#                Square("Docker", "#000000", "#FFFFFF") 
#            ], 

        ] 

    return render_template('index.html', projects=projects)

