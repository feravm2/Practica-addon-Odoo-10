# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError
from odoo.addons import decimal_precision as dp

class test(models.Model):
    _name = 'test.odoo'
    _inherit = ['mail.thread', 'ir.needaction_mixin']

    name = fields.Char(string=_("Title"))
    value = fields.Integer()
    value2 = fields.Float(compute="_valor_sinIVA", store=True)
    start_date = fields.Date(default=fields.Date.today)
    description = fields.Text()
    file_acepted = fields.Binary(string='Original Image')
    file_acepted2 = fields.Binary('FIle Upload')
    status = fields.Selection([('active', 'Activo'),('inactive','Inactivo')], default = "active", required = True)
    partner_id = fields.Many2one('res.partner', string="Cliente", index=True) 
    sale_ids = fields.Many2many('sale.order')
    total_sales = fields.Integer(compute = "count_sales", store = True )
    line_ids = fields.One2many('test.odoo.line', 'log_id')
    folio = fields.Char("Folio")
    rediction_bt = fields.Integer()
    float_value=fields.Float(string="Valor 6 decimales", digits=dp.get_precision('Payment Terms'))

    phone= fields.Char(related='partner_id.phone', readonly=True)
    

    @api.model
    def create(self, vals):
        vals['folio'] = self.env['ir.sequence'].next_by_code('test.odoo.solictud')
        result = super(test, self).create(vals)
        return result

    @api.depends('value')
    def _valor_sinIVA(self):
        self.value2 = float(self.value) * .84

    @api.depends('sale_ids')
    def count_sales(self):
        for rec in self:
            if (len(rec.sale_ids)>0):
                suma=0
                for sale in rec.sale_ids:
                    suma=suma+1
                rec.total_sales=suma

    @api.multi
    def set_open(self):
        self.write({"name": "Test item" })

    @api.multi
    def set_status(self):
        self.write({"status": "inactive" })

    @api.multi
    def set_template(self):
        for rec in self:
            if rec.partner_id.id:
                sale_ids = self.env['sale.order'].search([('partner_id','=',rec.partner_id.id)])
                rec.value = len(sale_ids)
                for sale in sale_ids:
                    for line in sale.order_line:
                        print line.product_id.name
            else:
                raise UserError(_('Please Select customer.'))

    @api.depends('sale_order')
    def set_cancel_orders(self):
        for rec in self:
            if rec.sale_ids:
                for sale in rec.sale_ids:
                    sale.action_cancel()
            else:
                raise UserError(_('Please create any orders.'))




class TestLog(models.Model):
    _name = 'test.odoo.line'
    _description = "Auditlog - Log (Detalles)"

    description_log = fields.Text(string=_("Descripcion"))
    valor_1= fields.Integer(string=_("Valor"))
    log_id = fields.Many2one('test.odoo', string="Log")

    

