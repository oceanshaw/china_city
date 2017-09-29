#coding:utf-8
import logging

from odoo import models,fields,api
import xlrd,base64
_logger = logging.getLogger(__name__)

class haoyi_region(models.Model):
	_name="haoyi.region"

	xls = fields.Binary(string='XLS File', required=True)

	@api.multi
	def import_xls(self):
		for wiz in self:
			excel = xlrd.open_workbook(file_contents=base64.decodestring(wiz.xls))
			sheets=excel.sheets()
			cty_id=0
			for sh in sheets:
				for row in range(1,sh.nrows):
					state = sh.cell(row,0).value
					city = sh.cell(row,1).value
					district = sh.cell(row,2).value

					#read state
					state_id = self.env['res.country.state'].search([('name','=',state)]).id
					#_logger.warning(states.id)
					if state_id:
						city_id = self.env['haoyi.city'].search([('name','=',city)]).id
						if city_id:
							district_id = self.env['haoyi.district'].search([('name','=',district)]).id
							if district_id:
								continue
							else:
								self.env['haoyi.district'].create({'name':district,'city':city_id})
						else:
							c_id=self.env['haoyi.city'].create({'name':city,'state':state_id}).id
							self.env['haoyi.district'].create({'name':district,'city':c_id})
					else:
						china_id = self.env['res.country'].search([('name','=','China')])
						if china_id:
							s_id = self.env['res.country.state'].create({'name':state,'country_id':china_id,'code':'0'}).id
							c_id=self.env['haoyi.city'].create({'name':city,'state':s_id}).id
							self.env['haoyi.district'].create({'name':district,'city':c_id})
						else:
							ch_id = self.env['res.country'].create({'name':'China'}).id
							s_id = self.env['res.country.state'].create({'name':state,'country_id':ch_id,'code':'0'}).id
							c_id=self.env['haoyi.city'].create({'name':city,'state':s_id}).id
							self.env['haoyi.district'].create({'name':district,'city':c_id})

																
							
