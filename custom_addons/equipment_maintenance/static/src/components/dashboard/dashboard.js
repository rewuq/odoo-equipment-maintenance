/** @odoo-module */
import { Component, useState, onWillStart } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";

export class EquipmentDashboard extends Component {
    setup() {
        // Підключаємо сервіс ORM для виконання запитів до бази даних
        this.orm = useService("orm");
        
        // Створюємо реактивний стан (state) для наших лічильників
        this.state = useState({
            equipmentCount: 0,
            openRequestsCount: 0,
            overdueRequestsCount: 0,
        });

        // onWillStart виконується до того, як компонент з'явиться на екрані
        onWillStart(async () => {
            await this.fetchData();
        });
    }

    async fetchData() {
        // 1. Загальна кількість обладнання (пустий масив = без фільтрів)
        this.state.equipmentCount = await this.orm.searchCount("maintenance.equipment", []);

        // 2. Кількість відкритих заявок (статус draft або in_progress)
        this.state.openRequestsCount = await this.orm.searchCount("maintenance.request", [
            ["state", "in", ["draft", "in_progress"]]
        ]);

        // 3. Кількість прострочених заявок
        // Отримуємо поточну дату у форматі YYYY-MM-DD
        const today = new Date().toISOString().split('T')[0];
        
        this.state.overdueRequestsCount = await this.orm.searchCount("maintenance.request", [
            ["state", "in", ["draft", "in_progress"]],
            ["schedule_date", "<", today]
        ]);
    }
}

// Вказуємо ім'я XML-шаблону, який ми створимо для цього компонента
EquipmentDashboard.template = "equipment_maintenance.DashboardTemplate";

// Реєструємо наш компонент як Client Action, щоб Odoo могла його викликати через меню
registry.category("actions").add("equipment_maintenance.dashboard_action", EquipmentDashboard);