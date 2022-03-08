# -*- coding: utf-8 -*-
{
    "name" : "Customer Email CC BCC in Odoo",
    "author": "Edge Technologies",
    "version" : "12.0.1.0",
    "category" : "Email",
    'summary': 'App for send Email to customer with CC and BCC',
    "description": """
                """,
    "license" : "OPL-1",
    "depends" : ['mail', 'account'],
    "data": [
        'security/ir.model.access.csv',
        'data/res_config_settings_data.xml',
        'views/res_config_settings_views.xml',
        'views/mail_mail_view.xml',
        'wizard/mail_compose_message_view.xml',
        'wizard/account_invoice_send_views.xml',
         ],
    "auto_install": False,
    "price": 15,
    "currency": 'EUR',
    "installable": True,
    "live_test_url":'https://youtu.be/mdTlVXc0FOg',
    "images":["static/description/main_screenshot.png"],
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
