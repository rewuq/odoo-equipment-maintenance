from odoo import models, fields, api
from odoo.exceptions import UserError

class MaintenanceHistory(models.Model):
    _name = 'maintenance.history'
    _description = 'Історія обслуговування'

    # Зберігає: посилання на обладнання
    equipment_id = fields.Many2one('maintenance.equipment', string='Обладнання', required=True, readonly=True)
    
    # Опис виконаних робіт
    description = fields.Text(string='Опис виконаних робіт', readonly=True)
    
    # Відповідального
    user_id = fields.Many2one('res.users', string='Відповідальний', readonly=True)
    
    # Дату початку та завершення
    date_start = fields.Datetime(string='Дата початку', readonly=True)
    date_end = fields.Datetime(string='Дата завершення', readonly=True)
    
    # Фактичну тривалість
    duration = fields.Float(string='Фактична тривалість (годин)', readonly=True)

    # Не може редагуватися після створення (тільки перегляд) 
    def write(self, vals):
        raise UserError('Записи в історії обслуговування є остаточними і не можуть бути змінені!')

    # Заборонимо також видалення для повної надійності (бо це логічно для історії)
    def unlink(self):
        raise UserError('Записи в історії обслуговування не можна видаляти!')