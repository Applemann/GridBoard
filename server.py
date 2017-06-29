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
STATIC_FILES="file:///home/martin/Programming/Python/gridBoard/static/"

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


#@app.route('/move_issue', methods=['GET', 'POST'])
#def move_issue():
#    from_column = request.form['from_column']
#    to_column = request.form['to_column']
#    issue = request.form['issue']
#    position_before = request.form['position_before']
#
#    redis.lrem(from_column, issue)
#    if position_before != '': 
#        redis.linsert(to_column, 'before', position_before, issue)
#    else: 
#        redis.rpush(to_column, issue)
#
#    return from_column + ' ' + to_column
