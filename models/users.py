# coding:utf-8

from odoo import models,fields

class haoyi_users(models.Model):
		_inherit='res.users'

		city = fields.Many2one('haoyi.city','city')

