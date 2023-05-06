{
    'name': 'Partner Generator',
    'version': '1.0.0',
    'summary': 'This app allows to generate unlimited of  partner',
    'description': 'This app allows to generate unlimited of  partner',
    'category': 'Human Resources/Contracts',
    'author': 'Cabrel Tchomte',
    'website': 'Website',
    'license': 'LGPL-3',
    'depends': ['contacts'],
    'data': ['wizard/random_partner_form_wizard.xml',
             'views/random_partner_view.xml',
             'security/ir.model.access.csv'],
    'images': ['static/description/img1.png', 'static/description/img2.png'],
    'installable': True,
    'auto_install': False
}