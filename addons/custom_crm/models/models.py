# -*- coding: utf-8 -*-
from odoo import models, fields, api
import datetime


class visit(models.Model):
    _name = 'custom_crm.visit' # Model name
    _description = 'Visit' # Model description

    name = fields.Char(string='Descripción') # Field name suele pintarse en el formulario en el encabezado de la vista
    customer = fields.Many2one(string='Cliente', comodel_name='res.partner') # Field customer
    date = fields.Datetime(string='Fecha')
    type = fields.Selection([('P', 'Presencial'), ('W', 'WhatsApp'), ('T', 'Telefónico')], string='Tipo', required=True)
    done = fields.Boolean(string='Realizada', readonly=True)
    image = fields.Binary(string='Imagen') # para la vista kanban

    def button_toggle_state(self):
        self.done = not self.done

    def f_create(self):
        """ Create a new record """
        visit = {
            "name": "ORM test",
            "customer": 1,
            "date": str(datetime.date(2020, 8, 6)),
            "type": "P",
            "done": False
        }
        print(visit)
        self.env['custom_crm.visit'].create(visit) # self.env['custom_crm.visit'] es un metodo que crea un objeto de la clase visit
    
    def f_search_update(self):
        """ Search and update a record """
        visit = self.env['custom_crm.visit'].search([('name', '=', 'ORM test')]) # pasa una lista de tuplas con los criterios de busqueda
        # print("search: ", visit, visit.name)
        visit_bis = self.env['custom_crm.visit'].browse([8]) # browse es para buscar por id

        visit.write({'name': 'ORM test updated'}) # update

    def f_delete(self):
        """ Delete a record """
        visit = self.env['custom_crm.visit'].search([('name', '=', 'ORM test updated')])
        # visit = self.env['custom_crm.visit'].browse([8])
        visit.unlink()

# class custom_crm(models.Model):
#     _name = 'custom_crm.custom_crm'
#     _description = 'custom_crm.custom_crm'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
