# -*- coding: utf-8 -*-
{
    'name': "Autoescuela",
    'summary': "Gestión de autoescuelas, profesores, alumnos y exámenes",
    'description': """
    Módulo de gestión de autoescuelas para la práctica UT03.
    """,
    'author': "Miguel Angel Guardia, David Resino, Alejandro Galan",
    'website': "https://github.com/Aleegalan06/autoescuela",
    'category': 'Education',
    'version': '1.0',
    'application': True,
    'depends': ['base'],
    'data': [
        'security/autoescuela_groups.xml',
        'security/ir.model.access.csv',
        'views/autoescuela_views.xml',
        'views/profesor_views.xml',
        'views/alumno_views.xml',
        'views/examen_views.xml',
        'views/templates.xml',
        'views/autoescuela_menus.xml',

    ],
    'demo': [
        'demo/demo.xml',
    ],
}


