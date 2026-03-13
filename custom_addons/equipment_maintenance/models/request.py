from odoo import models, fields, api
from datetime import datetime

class MaintenanceRequest(models.Model):
    _name = 'maintenance.request'
    _description = 'Заявка на обслуговування'

    # Автоматична генерація номера заявки
    name = fields.Char(string='Номер заявки', required=True, copy=False, readonly=True, default='Нова')
    
    # Основні поля згідно з ТЗ
    equipment_id = fields.Many2one('maintenance.equipment', string='Обладнання', required=True)
    user_id = fields.Many2one('res.users', string='Відповідальний')
    description = fields.Text(string='Опис проблеми')
    priority = fields.Selection([
        ('0', 'Низький'),
        ('1', 'Середній'),
        ('2', 'Високий'),
        ('3', 'Критичний')
    ], string='Пріоритет', default='0')
    
    request_date = fields.Date(string='Дата створення', default=fields.Date.context_today)
    schedule_date = fields.Date(string='Планова дата виконання')

    # Поля для обчислення тривалості виконання
    date_start = fields.Datetime(string='Фактичний початок')
    date_end = fields.Datetime(string='Фактичне завершення')
    duration = fields.Float(string='Тривалість (годин)', compute='_compute_duration', store=True)

    # Workflow (статуси)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ], string='Статус', default='draft')

    # 1. Автоматична генерація номера при створенні
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'Нова') == 'Нова':
                # Викликаємо генератор послідовностей Odoo
                vals['name'] = self.env['ir.sequence'].next_by_code('maintenance.request') or 'Нова'
        return super().create(vals_list)

    # 2. Обчислення тривалості виконання
    @api.depends('date_start', 'date_end')
    def _compute_duration(self):
        for rec in self:
            if rec.date_start and rec.date_end:
                diff = rec.date_end - rec.date_start
                rec.duration = diff.total_seconds() / 3600.0 # Переводимо секунди в години
            else:
                rec.duration = 0.0

    # 3. Контроль переходів між статусами (Методи для кнопок в інтерфейсі)
    def action_in_progress(self):
        for rec in self:
            rec.state = 'in_progress'
            rec.date_start = fields.Datetime.now() # Фіксуємо час початку

    def action_done(self):
        for rec in self:
            rec.state = 'done'
            rec.date_end = fields.Datetime.now() # Фіксуємо час завершення
            
            # Автоматичне створення запису в історії після завершення
            self.env['maintenance.history'].create({
                'equipment_id': rec.equipment_id.id,
                'description': rec.description,
                'user_id': rec.user_id.id,
                'date_start': rec.date_start,
                'date_end': rec.date_end,
                'duration': rec.duration,
            })

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancelled'