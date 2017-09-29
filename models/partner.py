# coding:utf-8


from odoo import models,fields

class haoyi_partner(models.Model):
		_inherit='res.partner'

		city = fields.Many2one('haoyi.city','city')
		district = fields.Many2one('haoyi.district','district')

