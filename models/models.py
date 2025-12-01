# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import date

class Autoescuela(models.Model):
    _name = 'autoescuela.autoescuela'
    _description = 'Autoescuela'
    name = fields.Char(string="Nombre", required=True)
    domicilio = fields.Char()
    localidad = fields.Char()
    provincia = fields.Char()
    contacto = fields.Char(string="Teléfono de contacto")
    profesor_ids = fields.One2many(
        'autoescuela.profesor',
        'autoescuela_id',
        string="Profesores"
    )
    alumno_ids = fields.One2many(
        'autoescuela.alumno',
        'autoescuela_id',
        string="Alumnos"
    )
    examen_ids = fields.Many2many(
        'autoescuela.examen',
        'autoescuela_examen_rel',
        'autoescuela_id',
        'examen_id',
        string="Exámenes"
    )

class Profesor(models.Model):
    _name = 'autoescuela.profesor'
    _description = 'Profesor de autoescuela'
    name = fields.Char(string="Nombre", required=True)
    dni = fields.Char(required=True)
    coche = fields.Char()
    matricula = fields.Char()
    autoescuela_id = fields.Many2one(
        'autoescuela.autoescuela',
        string="Autoescuela"
    )
    incorporacion = fields.Date(string="Fecha incorporación")
    antiguedad = fields.Integer(
        string="Años antigüedad",
        compute='_compute_antiguedad',
        store=True
    )
    alumno_ids = fields.One2many(
        'autoescuela.alumno',
        'profesor_id',
        string="Alumnos"
    )
    _sql_constraints = [
        ('profesor_dni_uniq',
         'unique (dni)',
         'No se pueden repetir DNIs de profesor.'),
    ]
    @api.depends('incorporacion')
    def _compute_antiguedad(self):
        today = date.today()
        for prof in self:
            if prof.incorporacion:
                prof.antiguedad = today.year - prof.incorporacion.year
            else:
                prof.antiguedad = 0

class Alumno(models.Model):
    _name = 'autoescuela.alumno'
    _description = 'Alumno de autoescuela'
    name = fields.Char(string="Nombre", required=True)
    dni = fields.Char(required=True)
    domicilio = fields.Char()
    matricula = fields.Char(string="Número de matrícula")
    autoescuela_id = fields.Many2one(
        'autoescuela.autoescuela',
        string="Autoescuela"
    )
    profesor_id = fields.Many2one(
        'autoescuela.profesor',
        string="Profesor"
    )
    examen_ids = fields.Many2many(
        'autoescuela.examen',
        'alumno_examen_rel',
        'alumno_id',
        'examen_id',
        string="Exámenes"
    )
    _sql_constraints = [
        ('alumno_matricula_uniq',
         'unique (matricula)',
         'No se pueden repetir números de matrícula de alumno.'),
    ]

class Examen(models.Model):
    _name = 'autoescuela.examen'
    _description = 'Examen de autoescuela'
    name = fields.Char(
        string="Código del examen",
        readonly=True,
        copy=False,
        default='Autogenerado'
    )
    fecha = fields.Date(string="Fecha examen")
    autoescuela_ids = fields.Many2many(
        'autoescuela.autoescuela',
        'autoescuela_examen_rel',
        'examen_id',
        'autoescuela_id',
        string="Autoescuelas asociadas"
    )
    alumno_id = fields.Many2one(
        'autoescuela.alumno',
        string="Alumno"
    )
    moneda_id = fields.Many2one(
        'res.currency',
        string="Moneda",
        default=lambda self: self.env.ref('base.EUR')
    )
    precio = fields.Monetary(
        string="Precio",
        currency_field='moneda_id'
    )
    clases = fields.Integer(string="Número de clases")
    carnet = fields.Char(
        string="Tipo de carnet",
        help="Ejemplo: B, A2, C1..."
    )
    aprobado = fields.Boolean(string="Aprobado", default=False)
