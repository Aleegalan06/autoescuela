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
        'security/ir.model.access.csv',
        'views/templates.xml',
        'views/views.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}


