# -*- coding:utf-8 -*-

from openerp.osv import osv,fields
from openerp.tools.translate import _

class sh_sale(osv.osv):
		_name="sale.order"
		_inherit="sale.order"

		def onchange_partner_id(self,cr,uid,ids,part,context=None):
				processing_ids = self.pool.get('sale.handler').search(cr,uid,[('partner_id','=',part),('state','in',('new','purchase','stock','account'))])
				if len(processing_ids):
					res={}
					#raise osv.except_osv(_('Error!'),u'此客户处于结款状态,不能下订单,请联系财务人员完成结款工作后重试!')
					value={
									'title':u'错误',
									'message':'此客户处于结款期间,不能创建新的订单,如需要,请联系相关财务人员完成结款后再试!'
									}
					res={'warning':value,'value':{'partner_id':''}}
					return res 
				else:
					return super(sh_sale,self).onchange_partner_id(cr,uid,ids,part,context=context)
