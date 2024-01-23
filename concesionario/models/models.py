# -*- coding: utf-8 -*-

from odoo import models, fields, api

class coche(models.Model):
    _name = 'concesionario.coche'
    _description = 'concesionario.coche'
    _rec_name = 'matricula'

    matricula = fields.Char(string="Matrícula: ",help="Introduzca la matrícula")
    modelo = fields.Char(string="Modelo: ",help="Introduzca el modelo del coche")
    year = fields.Date(string="Año de creación: ",help="Año de creación")
    puertas = fields.Integer(string="Número de puertas: ",
                             help="Indique el número de puertas")
    motor = fields.Selection([('gasolina','Gasolina'),('diesel','Diésel'),('electrico','Eléctrico')],string="Tipo de motor: ")
    marca = fields.Many2one(
        'concesionario.marca',
        string="Marca: ")
    
    @api.onchange('puertas')
    def _numpuertas(self):
        if self.puertas > 5 or self.puertas < 2:
            self.puertas = 5

class marca(models.Model):
    _name = 'concesionario.marca'
    _description = 'concesionario.marca'
    _rec_name = 'nombre'

    direccion = fields.Char(string="Dirección: ",help="Indique la dirección")
    sede = fields.Char(string="Sede: ",help="Sede de la marca")
    director = fields.Char(string="Nombre del director: ",help="Nombre y apellidos del director")
    nombre = fields.One2many(
        'concesionario.coche',
	    'marca', 
        string='Coches')

class concesionario(models.Model):
    _name = 'concesionario.concesionario'
    _description = 'concesionario.concesionario'
    _rec_name = 'nombre'
    
    nombre = fields.Char(string="Nombre: ",help="Indique el nombre del concesionario: ")
    direccion = fields.Char(string="Dirección: ",help="Indique la dirección del concesionario: ")
    n_bastidor = fields.One2many(
        'concesionario.coche',
        'matricula',
        string="Nº de bastidor: ")
    trabajador = fields.Many2many(comodel_name='concesionario.concesionario',
                                  relation='trabajadores_concesionario',
                                  column1='trabajador_id',
                                  column2='concesionario_id')

class trabajador(models.Model):
    _name = 'concesionario.trabajador'
    _description = 'concesionario.trabajador'
    _rec_name = 'nombre'
    
    nombre = fields.Char(string="Nombre: ",help="Nombre del trabajador: ")
    apellido1 = fields.Char(string="Primer apellido: ",help="Primer apellido")
    apellido2 = fields.Char(string="Segundo apellido: ",help="Segundo apellido")
    telefono = fields.Char(string="Teléfono: ",help="Teléfono de contacto")
    concesionario = fields.Many2many(comodel_name='concesionario.trabajador',
                                relation='trabajadores_concesionario',
                                column1='concesionario_id',
                                column2='trabajador_id')
