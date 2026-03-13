from odoo import models, fields, api

class EquipmentCategory(models.Model):
    _name = 'maintenance.category'
    _description = 'Категорія обладнання'

    # Зберігання основної інформації
    name = fields.Char(string='Назва категорії', required=True)
    description = fields.Char(string='Опис категорії', required=True)

    # Ієрархія (батьківська категорія) 
    parent_id = fields.Many2one('maintenance.category', string='Батьківська категорія', index=True)
    child_ids = fields.One2many('maintenance.category', 'parent_id', string='Підкатегорії')
    
    # Невидимий зв'язок з обладнанням (потрібен для підрахунку)
    equipment_ids = fields.One2many('maintenance.equipment', 'category_id', string='Обладнання')
    
    # Відображення кількості обладнання в категорії 
    equipment_count = fields.Integer(string='Кількість обладнання', compute='_compute_equipment_count')

    @api.depends('equipment_ids')
    def _compute_equipment_count(self):
        for record in self:
            record.equipment_count = len(record.equipment_ids)