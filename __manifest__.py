# -*- coding: utf-8 -*-

{
    'name': 'HelpDesk v0.1',
    'version': '1.0',
    'sequence': -100, #//shows up first on the app list the lower it is
    'category': 'Productivity',
    'author': 'EDI',
    'description': """
        Client Support """,
    'depends':[],
    'data': [
        'security/ir.model.access.csv', 
        'views/view.xml',
    ],
    'installable': True,
    'application': True, #//declaring this an installable and usable stand-alone app
    'auto_install' : False,
}
