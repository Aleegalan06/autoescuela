# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import date

# -----------------------------
# MODELO AUTOESCUELA
# -----------------------------
class Autoescuela(models.Model):
    # Nombre técnico del modelo (tabla en Odoo)
    _name = 'autoescuela.autoescuela'
    # Descripción legible en la interfaz
    _description = 'Autoescuela'
    # Nombre de la autoescuela
    name = fields.Char(string="Nombre", required=True)
    # Dirección
    domicilio = fields.Char()
    # Localidad (ciudad/pueblo)
    localidad = fields.Char()
    # Provincia
    provincia = fields.Char()
    # Teléfono de contacto
    contacto = fields.Char(string="Teléfono de contacto")
    # Relación 1 (autoescuela) a N (profesores)
    # En el otro modelo, la FK es autoescuela_id
    profesor_ids = fields.One2many('autoescuela.profesor', 'autoescuela_id', string="Profesores")
    # Relación 1 (autoescuela) a N (alumnos)
    alumno_ids = fields.One2many('autoescuela.alumno', 'autoescuela_id', string="Alumnos")
    # Relación N a N entre autoescuela y examen
    # autoescuela_examen_rel es la tabla intermedia
    examen_ids = fields.Many2many('autoescuela.examen', 'autoescuela_examen_rel', 'autoescuela_id', 'examen_id', "string="Exámenes")

# -----------------------------
# MODELO PROFESOR
# -----------------------------
class Profesor(models.Model):
    _name = 'autoescuela.profesor'
    _description = 'Profesor de autoescuela'
    # Nombre del profesor
    name = fields.Char(string="Nombre", required=True)
    # DNI del profesor (obligatorio y único, ver _sql_constraints)
    dni = fields.Char(required=True)
    # Coche que utiliza (modelo, marca...)
    coche = fields.Char()
    # Matrícula del coche
    matricula = fields.Char()
    # Relación N (profesores) a 1 (autoescuela)
    autoescuela_id = fields.Many2one('autoescuela.autoescuela', string="Autoescuela")
    # Fecha de incorporación a la autoescuela
    incorporacion = fields.Date(string="Fecha incorporación")
    # Campo calculado de años de antigüedad
    antiguedad = fields.Integer(string="Años antigüedad", compute='_compute_antiguedad', store=True)
    # Relación 1 (profesor) a N (alumnos)
    alumno_ids = fields.One2many('autoescuela.alumno', 'profesor_id', string="Alumnos" )
    # Restricciones SQL a nivel de base de datos
    _sql_constraints = [('profesor_dni_uniq', 'unique (dni)', 'No se pueden repetir DNIs de profesor.'),]
    # Decorador que indica que este método recalcula el campo "antiguedad"
    # cuando cambie el campo "incorporacion"
    @api.depends('incorporacion')
    def _compute_antiguedad(self):
        today = date.today()  # fecha actual del sistema
        for prof in self:
            if prof.incorporacion:
                # Diferencia de años entre hoy y el año de incorporación
                prof.antiguedad = today.year - prof.incorporacion.year
            else:
                prof.antiguedad = 0


# -----------------------------
# MODELO ALUMNO
# -----------------------------
class Alumno(models.Model):
    _name = 'autoescuela.alumno'
    _description = 'Alumno de autoescuela'
    # Nombre del alumno
    name = fields.Char(string="Nombre", required=True)
    # DNI del alumno
    dni = fields.Char(required=True)
    # Dirección del alumno
    domicilio = fields.Char()
    # Número de matrícula de la autoescuela
    matricula = fields.Char(string="Número de matrícula")
    # N (alumnos) a 1 (autoescuela)
    autoescuela_id = fields.Many2one('autoescuela.autoescuela', string="Autoescuela")
    # N (alumnos) a 1 (profesor)
    profesor_id = fields.Many2one('autoescuela.profesor', string="Profesor")
    # N a N entre alumnos y exámenes (un alumno puede hacer varios exámenes)
    examen_ids = fields.Many2many('autoescuela.examen', 'alumno_examen_rel', 'alumno_id', 'examen_id', string="Exámenes")
    # Restricción para que no se repita el número de matrícula
    _sql_constraints = [('alumno_matricula_uniq', 'unique (matricula)', 'No se pueden repetir números de matrícula de alumno.'),]

# -----------------------------
# MODELO EXAMEN
# -----------------------------
class Examen(models.Model):
    _name = 'autoescuela.examen'
    _description = 'Examen de autoescuela'
    # Código del examen (nombre interno), de solo lectura
    # copy=False → cuando se duplica el registro no se copia este valor
    name = fields.Char(string="Código del examen", readonly=True, copy=False, default='Autogenerado')
    # Fecha del examen
    fecha = fields.Date(string="Fecha examen")
    # N a N con autoescuela (mismas columnas que en el modelo Autoescuela)
    autoescuela_ids = fields.Many2many('autoescuela.autoescuela', 'autoescuela_examen_rel', 'examen_id','autoescuela_id', string="Autoescuelas asociadas")
    # N (exámenes) a 1 (alumno) → este campo indica “este examen es de este alumno”
    # (aunque también tengas Many2many desde Alumno, aquí podrías guardar
    # el alumno “principal” o el que se está editando directamente)
    alumno_id = fields.Many2one('autoescuela.alumno', string="Alumno")
    # Moneda usada en el precio del examen
    # self.env.ref busca el registro base.EUR(moneda euro)
    moneda_id = fields.Many2one('res.currency', string="Moneda", default=lambda self: self.env.ref('base.EUR'))
    # Campo monetario, enlazado a la moneda especificada en "moneda_id"
    precio = fields.Monetary(string="Precio", currency_field='moneda_id')
    # Número de clases que ha dado el alumno antes del examen
    clases = fields.Integer(string="Número de clases")
    # Tipo de carnet al que corresponde el examen (B, A2, C1…)
    carnet = fields.Char(string="Tipo de carnet", help="Ejemplo: B, A2, C1...")
    # Indica si el examen se ha aprobado o no
    aprobado = fields.Boolean(string="Aprobado", default=False)

