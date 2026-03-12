from odoo import models, fields, api
from odoo.exceptions import UserError

class Equipment(models.Model):
    _name = 'maintenance.equipment'
    _description = 'Обладнання'

    # Зберігання основної інформації [cite: 11]
    name = fields.Char(string='Назва', required=True)
    serial_number = fields.Char(string='Серійний номер')
    commission_date = fields.Date(string='Дата введення в експлуатацію')
    
    # Відповідальний (зв'язок з базовою таблицею користувачів) [cite: 11]
    user_id = fields.Many2one('res.users', string='Відповідальний')
    
    # Прив’язка до категорії обладнання (цю модель створимо наступною) [cite: 12]
    category_id = fields.Many2one('maintenance.category', string='Категорія')
    
    # Контроль зміни статусу [cite: 15]
    state = fields.Selection([
        ('in_use', 'В експлуатації'),
        ('maintenance', 'На обслуговуванні'),
        ('written_off', 'Списано')
    ], string='Стан', default='in_use')

    # Відображення пов’язаних заявок [cite: 13]
    request_ids = fields.One2many('maintenance.request', 'equipment_id', string='Заявки')
    
    # Обчислюване поле: кількість активних заявок [cite: 14]
    active_request_count = fields.Integer(string='Кількість активних заявок', compute='_compute_active_request_count')

    @api.depends('request_ids.state')
    def _compute_active_request_count(self):
        for record in self:
            active_requests = record.request_ids.filtered(lambda r: r.state in ['draft', 'in_progress'])
            record.active_request_count = len(active_requests)

    # Заборона видалення, якщо є пов’язані заявки [cite: 16]
    def unlink(self):
        for record in self:
            if record.request_ids:
                raise UserError('Неможливо видалити обладнання, яке має пов’язані заявки на обслуговування!')
        return super(Equipment, self).unlink()