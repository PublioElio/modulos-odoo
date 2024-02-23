# -*- coding: utf-8 -*-

from odoo import models, fields, api

class profesor(models.Model):
    _name = 'instituto.profesor'
    _description = 'instituto.profesor'
    _rec_name = "nombre"

    nombre = fields.Char()
    direccion = fields.Char()
    ciudad = fields.Selection([('malaga','Málaga'),
                               ('sevilla','Sevilla'),
                               ('cordoba','Córdoba'),
                               ('jaen','Jaén'),
                               ('granada','Granada'),
                               ('huelva','Huelva'),
                               ('almeria','Almería'),
                               ('cadiz','Cádiz')],string="Ciudad: ")
    telefono = fields.Char()
    asignaturas = fields.One2many('instituto.asignatura',
                                  'profesor',
                                  string='Asignaturas: ')

class estudiante(models.Model):
    _name = 'instituto.estudiante'
    _description = 'instituto.estudiante'
    _rec_name = "nombre"

    nombre = fields.Char()
    apellidos = fields.Char()
    direccion = fields.Char()
    ciudad = fields.Selection([('malaga','Málaga'),
                               ('sevilla','Sevilla'),
                               ('cordoba','Córdoba'),
                               ('jaen','Jaén'),
                               ('granada','Granada'),
                               ('huelva','Huelva'),
                               ('almeria','Almería'),
                               ('cadiz','Cádiz')],string="Ciudad: ")
    asignaturas = fields.Many2many(comodel_name='instituto.asignatura',
                               relation='estudiantes_asignaturas',
                               column1='nombre_estudiante',
                               column2='nombre_asignatura')

class asignatura(models.Model):
    _name = 'instituto.asignatura'
    _description = 'instituto.asignatura'
    _rec_name = "nombre"
    
    nombre = fields.Char()
    nivel = fields.Integer()
    imagen = fields.Binary()
    profesor = fields.Many2one('instituto.profesor',
                               string="Profesor: ")
    alumnado = fields.Many2many(comodel_name='instituto.estudiante',
                               relation='asignaturas_estudiantes',
                               column1='nombre_asignatura',
                               column2='nombre_estudiante')
