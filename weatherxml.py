#coding: utf-8
import requests
import json
from lxml import etree
from jinja2 import Template

ciudades = ['Almeria','Cadiz','Cordoba','Huelva','Jaen','Malaga','Sevilla']
f = open("plantilla.html","r")
salida = open("salida.html","w")
html = ''
