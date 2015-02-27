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

{
    'name': 'Remise globale',
    'version': '1.0',
    'author': 'SYSMART  - info@sysmart.com',
    'website': 'http://www.sysmart.ma/',
    'category': 'stock',
    'description' : """ Remise globale """,
    'depends': ['sale','account'],
    'data': ['remise_globale_view.xml'],
}