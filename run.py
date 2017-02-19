#!/usr/bin/env python

from flask import Flask, request, redirect
app = Flask(__name__)

@app.route('/')
def test1():
	return 'x-me-v1.0'


@app.route('/test')
def test2():
	return 'x-me-v1.0/test'
