# Equipment Maintenance - Odoo 18 Module

A custom Odoo module developed to efficiently manage company equipment, handle maintenance requests, and track maintenance history. This project demonstrates full-stack Odoo development skills, including ORM, custom SQL views, role-based access control (RBAC), and front-end development using the Odoo Web Library (OWL).

## 🚀 Key Features

* **Equipment Management:** Track equipment with hierarchical categories and real-time statuses (In Use, Maintenance, Written Off).
* **Maintenance Workflow:** Interactive Kanban board for managing maintenance requests (Draft ➔ In Progress ➔ Done ➔ Cancelled).
* **Automated History Tracking:** Automatically generates read-only history records upon request completion, calculating actual maintenance duration.
* **Interactive OWL Dashboard:** A modern client-side dashboard built with JavaScript (OWL) displaying real-time statistics (Total Equipment, Open Requests, Overdue Requests).
* **Advanced Analytics:** Custom PostgreSQL View (`_auto = False`) providing complex data aggregation, visualized through interactive Pivot and Graph views.
* **Role-Based Access Control (Security):** * **Employee:** Can view all data but only create/manage their own requests.
  * **Manager:** Full CRUD access to all records and configuration.

## 🛠️ Tech Stack

* **Backend:** Python 3, Odoo 18 ORM
* **Database:** PostgreSQL (including raw SQL queries for Views)
* **Frontend:** XML, JavaScript (OWL - Odoo Web Library), Bootstrap
* **Infrastructure:** Docker, Docker Compose

## 📦 Installation & Setup

1. Clone this repository 
```
git clone https://github.com/rewuq/odoo-equipment-maintenance
cd odoo-equipment-maintenance```
2. Start the environment: 
```
docker-compose up -d
```
3. Access the Application: Open your browser and navigate to http://localhost:8069.
4. Initial Setup:
   * Create a new database.
   * **Important:** Check the "Demo Data" box during creation to properly test the roles and access rights.
   * Log in with your admin credentials.
5. Activate the Module:
   * Go to the Apps menu.
   * Remove the default Apps filter in the search bar.
   * Search for Equipment Maintenance and click Activate.

## 👥 Users & Roles (Testing)
To test the security rules, it is recommended to create two users:
* **Manager User:** Assign the `Manager` role in the Equipment Maintenance category.
* **Employee User:** Assign the `Employee` role. Observe how the "History" editing is blocked and request visibility is filtered.

---
**Author:** Kateryna Fedorova
*Junior Python Developer*
