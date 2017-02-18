#!/usr/bin/env python

from flask import Flask, request, redirect
app = Flask(__name__)

@app.route('/')
def test1():
	return 'hello world'


@app.route('/test')
def test2():
	return '/test hello world'
