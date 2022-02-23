from odoo import api,fields,models


class ClientSupport(models.Model):
    _name = "client.support"
    _description = "Client Support"
    name = fields.Text('Your name', required=True)
    department = fields.Char('Your department', required=True)
    issue_category = fields.Selection([('cat1', 'Category 1'),
                                ('cat2', 'Category 2'), 
                                ('cat3', 'Category 3')], 
                                default='cat1',string="Issue Category",required=True)
    issue_priority = fields.Selection([('prio1', 'Priority 1'),
                                ('prio2', 'Priority 2'), 
                                ('prio3', 'Priority 3')], 
                                default='prio1',string="Issue Priority",required=True)
    issue_state = fields.Selection([('draft', 'Draft'),
                                    ('pending', 'Pending'),
                                    ('resolve', 'Resolved')],
                                default="draft", string="Issue State", required=True)
