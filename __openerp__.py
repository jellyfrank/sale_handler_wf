# -*- coding:utf-8 -*-
##############################################################################
#
#    OpenERP, Designed For QingDao Xiangjie Company
#    Powered By Rainsoft(QingDao) Author:Kevin Kong 2014 (kfx2007@163.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
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
{
        "name":"销售结款流程",
        "version":"1.0",
        "description":u"""
销售结款流程
===============================================================
由销售人员发起结款请求,经采购\物流人员审核后转交财务,由财务结款,结款完成后此客户方可继续下单.

        """,
        "author":"Kevin Kong",
        "depends":["base","sale","purchase","account","stock"],
        "update_xml":["sh_workflow.xml","security/sale_handler_security.xml","security/ir.model.access.csv","sale_handler_view.xml"],
        "installable":True,
        "category":"Others"
}
