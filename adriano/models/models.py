# -*- coding: utf-8 -*-

from odoo import models, fields, api

class adriano(models.Model):
    _name = 'adriano.adriano'
    _description = 'adriano.adriano'

    name = fields.Char(string="Nombre: ",help="Pon tu nombre",default="Adriano")
    apellidos = fields.Char(string="Apellidos: ",default="Díaz Benítez",help="Pon tus apellidos")
    nombre_apellidos = fields.Char(compute="_nombreyapellidos",string="Nombre y apellidos: ",help="Nombre y apellidos",readonly=True,store="true")
    direccion = fields.Char(string="Dirección: ",help="Pon tu dirección")
    ciudad = fields.Char(string="Ciudad: ",help="Pon tu ciudad")
    edad = fields.Integer(string="Edad: ",help="Escribe tu edad")
    mayor_edad = fields.Char(compute="_mayoredad",string="Mayoría de edad: ",help="Indica si eres mayor de edad",readonly=True,store="true")
    sexo = fields.Char(string="Sexo: ",help="Hombre/mujer")


    @api.depends('name','apellidos')
    def _nombreyapellidos(self):
        self.nombre_apellidos = self.name + " " + self.apellidos
    
    @api.depends('edad')
    def _mayoredad(self):
        if self.edad >= 18:
            self.mayor_edad = "Sí"
        else:
            self.mayor_edad = "No"
