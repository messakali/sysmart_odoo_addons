# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2013 SYSMART All Rights Reserved.
#                       www.sysmart.ma
#                       messakali@gmail.com
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


import openerp.addons.decimal_precision as dp

from openerp import models, fields, api

class sale_order(models.Model):
    _inherit = "sale.order"
    
    @api.one
    @api.depends('order_line.price_subtotal', 'order_line.tax_id.amount', 'discount_total')
    def _amount_all(self):
        self.amount_untaxed = sum (line.price_subtotal for line in self.order_line)
        if self.methode_reduction ==  'pourcentage':         
            self.amount_total_discount = round(self.amount_untaxed * ((self.discount_total or 0.0) / 100.0), 2)
        elif self.methode_reduction ==  'fixe': 
            self.amount_total_discount =  self.discount_total
        else:
            self.amount_total_discount = 0.0
        self.amount_total_remise = self.amount_untaxed - self.amount_total_discount
        self.amount_tax = self.amount_total_remise * 0.2
        self.amount_total = self.amount_total_remise + self.amount_tax
  
    discount_total= fields.Float('Remise', digits_compute=dp.get_precision('Account'),default=0)
    methode_reduction= fields.Selection([('fixe', u'Fixe'),('pourcentage', 'Pourcentage')], u'Méthode de réduction')
    amount_total_discount= fields.Float(compute='_amount_all', digits_compute=dp.get_precision('Account'), string='Remise' , store=True, readonly=True)
    amount_total= fields.Float(compute='_amount_all', digits_compute=dp.get_precision('Account'), string='Total', store=True, readonly=True, help="The total amount.")
    amount_untaxed= fields.Float(compute='_amount_all', digits_compute=dp.get_precision('Account'), string='Montant HT', store=True, readonly=True, help="The amount without tax.", track_visibility='always')
    amount_tax= fields.Float(string='TVA 20%',compute='_amount_all', digits_compute=dp.get_precision('Account'),  store=True, readonly=True, help="The tax amount.")
    amount_total_remise = fields.Float(compute='_amount_all', digits_compute=dp.get_precision('Account'), string='Montant HT avec Remise', store=True, readonly=True, help="Montant HT avec remise.")          
    
    @api.cr_uid_ids_context
    def button_dummy(self, cr, uid, ids, args, context=None):
        return True
