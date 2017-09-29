#coding:utf-8

from odoo import models,fields

class haoyi_city(models.Model):
		_name='haoyi.city'

		name = fields.Char('name')
		state = fields.Many2one('res.country.state','state')



class haoyi_district(models.Model):
		_name="haoyi.district"

		name = fields.Char('name')
		city = fields.Many2one('haoyi.city',"city")

