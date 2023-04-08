from odoo import api, fields, models, _
from odoo.exceptions import UserError


class material(models.Model):
    _name = 'material'
    _description = 'Materials Registration'
        
    name = fields.Char('Name', index=True, required=True, translate=True)
    code = fields.Char('Code', index=True, required=True)
    type = fields.Selection([
        ('fabric', 'Fabric'),
        ('jeans', 'Jeans'),
        ('cotton', 'Cotton'),], string='Type', default='cotton', required=True)
    buy_price = fields.Float(
        'Buy Price', company_dependent=True, required=True,
        default=100.0, digits='Product Price')
    supplier_id = fields.Many2one('res.partner', string='Supplier', required=True)
    product_qty = fields.Float(string='Quantity', digits='Product Unit of Measure', required=False)
    product_uom = fields.Many2one('uom.uom', string='Unit of Measure')
    
    @api.model
    def create(self, vals):
        if vals.get('buy_price') < 100:
            raise UserError(_('The Buy Price must be greater than Rp100,-'))
        else:
            return super(material, self).create(vals)   
    
    def write(self, vals):
        for rec in self:
            if vals.get('buy_price') < 100:
                raise UserError(_('The Buy Price must be greater than Rp100,-'))
        return super(material, self).write(vals)   
    
