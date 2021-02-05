from odoo import models, fields, api, _

class res_partner (models.Model):
    _inherit = 'res.partner'

    description = fields.Char(string=_("Description"))
    test_value = fields.Selection([('active', 'Pagado'),('inactive','Adeudo')], default = "active", required = True)
    notify_email = fields.Selection([('active', 'Ninguno'),('inactive','Solo por msn'),('draf','Solo por Chat')], default = "active", required = True)

    