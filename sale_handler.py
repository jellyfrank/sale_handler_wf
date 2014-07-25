#-*- coding:utf-8 -*-

from openerp.osv import osv,fields
from openerp import netsvc

class sale_handler(osv.osv):
	_name="sale.handler"

	_columns={
            'partner_id':fields.many2one('res.partner',"Parnter",domain=[('is_company','=',True),('customer','=',True)]),
            'text':fields.text('Additional Infomation'),
			'state':fields.selection([('new','New'),('purchase','Purchase Processing'),('stock','Stock Processing'),('account','Account Processing'),('done','Done'),],'State',readonly=True),
            }

				

	
	def sh_new(self,cr,uid,ids,context=None):
		self.write(cr,uid,ids,{'state':'new'})

        def sh_purchase(self,cr,uid,ids,context=None):
            self.write(cr,uid,ids,{'state':'purchase'})
            
        def sh_stock(self,cr,uid,ids,context=None):
            self.write(cr,uid,ids,{'state':'stock'})

        def sh_account(self,cr,uid,ids,context=None):
            self.write(cr,uid,ids,{'state':'account'})

        def sh_done(self,cr,uid,ids,context=None):
            self.write(cr,uid,ids,{'state':'done'})

	def btn_purchase(self,cr,uid,ids,context=None):
		wf_service = netsvc.LocalService('workflow')
		wf_service.trg_validate(uid,'sale.handler',ids[0],'sh_purchase',cr)

        def btn_stock(self,cr,uid,ids,context=None):
            	wf_service = netsvc.LocalService('workflow')
		wf_service.trg_validate(uid,'sale.handler',ids[0],'sh_stock',cr)

        def btn_account(self,cr,uid,ids,context=None):
            	wf_service = netsvc.LocalService('workflow')
		wf_service.trg_validate(uid,'sale.handler',ids[0],'sh_account',cr)

        def btn_done(self,cr,uid,ids,context=None):
            	wf_service = netsvc.LocalService('workflow')
		wf_service.trg_validate(uid,'sale.handler',ids[0],'sh_done',cr)
sale_handler()
