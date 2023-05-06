from odoo.exceptions import UserError

from odoo import fields, models, _
from ..models.get_partners import get_random_users


class RandomPartner(models.TransientModel):
    _name = 'random.partner'
    _description = 'Random Partner'

    size = fields.Integer(string='Qty of Partner to generate', default=2)
    partner_type = fields.Selection(string='Company Type',
        selection=[('person', 'Individual'), ('company', 'Company')], default='person')

    def generate_partners(self):
        try:
            users = get_random_users(self.size)
            if self.size <= 1:
                raise UserError(_("The number of partner to generate must be greater than 1."))
            if users.status_code == 200:
                get_json_users = users.json()
                for user in get_json_users:
                    self.env['res.partner'].create({
                        'company_type': self.partner_type,
                        'name': user.get('first_name') + ' ' + user.get('last_name'),
                        'email': user.get('email'),
                        'phone': user.get('phone_number'),
                        'mobile': user.get('phone_number'),
                        'function': user['employment'].get('title'),
                        'city': user['address'].get('city'),
                        'country_id': self.env['res.country'].search_read([('name', '=', user['address'].get('country'))])[0].get('id'),
                        'street': user['address'].get('street_name'),
                        'street2': user['address'].get('street_address'),
                        'zip': user['address'].get('zip_code')
                    })
                return {
                    'warning': {
                        'title': _('Successful Generation'),
                        'message': _('The Generation has been done correctly!! :)')}
                }
        except Exception as e:
            raise UserError(_("An Error occur : %s", e))
