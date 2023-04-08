from datetime import timedelta

from odoo.tests.common import SavepointCase
from odoo.tests import Form


class TestMaterial(SavepointCase):
    @classmethod
    def setUpClass(cls):
        super(TestMaterial, cls).setUpClass()
        cls.supplier = cls.env['res.partner'].create({'name': 'Supplier 1'})
        cls.material_fabric = cls.env['material'].create({
            'name': 'Material A',
            'type': 'fabric',
            'code': 'FAB',
            'buy_price': 75000,
            'supplier_id': cls.supplier,
        })
        cls.material_jeans = cls.env['material'].create({
            'name': 'Material B',
            'type': 'jeans',
            'code': 'JN',
            'buy_price': 105000,
            'supplier_id': cls.supplier,
        })
        cls.material_cotton = cls.env['material'].create({
            'name': 'Product C',
            'type': 'cotton',
            'code': 'CTN',
            'buy_price': 60500,
            'supplier_id': cls.supplier,
        })
        cls.uom_unit = cls.env.ref('uom.product_uom_unit')
