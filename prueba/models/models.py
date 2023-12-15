# -*- coding: utf-8 -*-

from odoo import models, fields, api

class prueba(models.Model):
     _name = 'prueba.prueba'
     _description = 'prueba.prueba'

     name = fields.Char() # el primer campo debería llamarse siempre 'name'
     numeros = fields.Integer()
     descripcion = fields.Text(string="DESCRIPCIÓN",help="Debes introducir una descripción en este campo")