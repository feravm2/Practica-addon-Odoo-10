from odoo import models, fields, api, _

class modif_action_cancel(models.Model):
    _inherit = "sale.order"

    @api.multi
    def action_cancel(self):
        print "Hello User -----------------"
        super(modif_action_cancel,self).action_cancel()

    