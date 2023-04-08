{
    'name': "Materials Registration",
    'version': "0.1",
    'license': "LGPL-3",
    'author': "Adita Putri Puspaningrum",
    'website': "",
    'category': "Tools",
    'summary': "Register the material to be sold",
    'depends': [
                'base',
                'uom'
                ],
    'data': [
            'security/admin_group.xml',
            'security/ir.model.access.csv',
            'views/material.xml',
            'data/res_users_data.xml',
            ],
    'images': [],
    'sequence': 1,
    'installable': True,
    #"auto_install": True,
}
