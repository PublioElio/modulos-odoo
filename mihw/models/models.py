# -*- coding: utf-8 -*-

from odoo import models, fields, api

class equipo(models.Model):
    _name = 'mihw.equipo'
    _description = 'mihw.equipo'
    _rec_name = "identificador"

    identificador = fields.Char()
    fecha_montaje = fields.Date()
    precio = fields.Float()
    componentes = fields.Many2many(comodel_name='mihw.componente',
                               relation='equipos_componentes',
                               column1='identificador_equipo',
                               column2='nombre_componente')
    comprador = fields.Many2one('mihw.comprador',
                               string="Comprador: ")
    
class comprador(models.Model):
    _name = 'mihw.comprador'
    _description = 'mihw.comprador'
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
    equipos = fields.One2many('mihw.equipo',
                              'comprador',
                              string='Equipos: ')

class componente(models.Model):
    _name = 'mihw.componente'
    _description = 'mihw.componente'
    _rec_name = "nombre"

    nombre = fields.Char()
    tipo = fields.Selection([('hardware','Hardware'),
                             ('software','Software')],
                            string="Tipo: ")
    valor = fields.Float()
    imagen = fields.Binary()
    equipos = fields.Many2many(comodel_name='mihw.equipo',
                               relation='componentes_equipos',
                               column1='nombre_componente',
                               column2='identificador_equipo')