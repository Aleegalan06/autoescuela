# -*- coding: utf-8 -*-
{
    'name': "Autoescuela",
    'summary': "Gestión de autoescuelas, profesores, alumnos y exámenes",
    'description': """
    Módulo de gestión de autoescuelas para la práctica UT03.
    """,
    'author': "Tu nombre / vuestro grupo",
    'website': "https://github.com/tuusuario/autoescuela",
    'category': 'Education',
    'version': '1.0',
    'application': True,
    'depends': ['base'],
    'data': [
        'security/autoescuela_security.xml',
        'security/ir.model.access.csv',
        'data/autoescuela_sequence.xml',
        'views/autoescuela_menus.xml',
        'views/autoescuela_autoescuela_view.xml',
        'views/autoescuela_profesor_view.xml',
        'views/autoescuela_alumno_view.xml',
        'views/autoescuela_examen_view.xml',
        'reports/autoescuela_autoescuela_report.xml',
        'reports/autoescuela_profesor_report.xml',
        'reports/autoescuela_alumno_report.xml',
        'reports/autoescuela_examen_report.xml',
    ],
    'demo': [
        # 'demo/demo.xml',
    ],
}


