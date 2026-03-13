from odoo import models, fields, tools

class EquipmentMaintenanceReport(models.Model):
    _name = 'maintenance.report'
    _description = 'Аналітика по обладнанню (SQL View)'
    _auto = False  # Вимикаємо автоматичне створення таблиці ORM

    # Описуємо поля, які поверне наш SQL-запит
    equipment_id = fields.Many2one('maintenance.equipment', string='Обладнання', readonly=True)
    request_count = fields.Integer(string='Кількість заявок', readonly=True)
    avg_duration = fields.Float(string='Середній час виконання (год)', readonly=True)

    def init(self):
        # Видаляємо старий view, якщо він існував, щоб записати новий
        tools.drop_view_if_exists(self.env.cr, self._table)
     
        self.env.cr.execute("""
            CREATE OR REPLACE VIEW %s AS (
                SELECT 
                    e.id AS id, 
                    e.id AS equipment_id,
                    COUNT(r.id) AS request_count,
                    AVG(NULLIF(r.duration, 0)) AS avg_duration
                FROM maintenance_equipment e
                LEFT JOIN maintenance_request r ON r.equipment_id = e.id
                GROUP BY e.id
            )
        """ % (self._table,))