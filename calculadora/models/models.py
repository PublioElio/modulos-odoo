# -*- coding: utf-8 -*-

from odoo import models, fields, api

class calculadora(models.Model):
    _name = 'calculadora.calculadora'
    _description = 'calculadora.calculadora'

    name = fields.Char(string="Nombre de la operación: ",help="Dale un nombre a la operación") # el primer campo siempre se llama name
    valor1 = fields.Integer(string="Valor 1: ",help="Pon el primer número")
    valor2 = fields.Integer(string="Valor 2: ",help="Pon el segundo número")
    total = fields.Integer(compute="_calcular",string="Total: ",help="Aquí te saldrá el resultado",readonly=True,store="true")

    @api.depends('valor1','valor2')
    def _calcular(self):
        for record in self:
            record.total = int(record.valor1) + int(record.valor2)