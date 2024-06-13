import sys
from models.material import Material
from models.supplier import Supplier
from models.project import Project

def print_menu():
    print("Material Management System")
    print("1. Add Material")
    print("2. View All Materials")
    print("3. View Material by ID")
    print("4. Update Material")
    print("5. Delete Material")
    print("6. Add Supplier")
    print("7. View All Suppliers")
    print("8. View Supplier by ID")
    print("9. Update Supplier")
    print("10. Delete Supplier")
    print("11. Add Project")
    print("12. View All Projects")
    print("13. View Project by ID")
    print("14. Update Project")
    print("15. Delete Project")
    print("16. Exit")

def add_material():
    name = input("Enter name: ")
    quantity = int(input("Enter quantity: "))
    supplier = input("Enter supplier: ")
    project = input("Enter project: ")
    material = Material(name, quantity, supplier, project)
    material.add_material()
    print("Material added successfully.")

def view_all_materials():
    materials = Material.get_materials()
    for material in materials:
        print(material)

def view_material_by_id():
    id = int(input("Enter material ID: "))
    material = Material.get_material(id)
    if material:
        print(material)
    else:
        print("Material not found.")

def update_material():
    id = int(input("Enter material ID to update: "))
    name = input("Enter new name: ")
    quantity = int(input("Enter new quantity: "))
    supplier = input("Enter new supplier: ")
    project = input("Enter new project: ")
    Material.update_material(id, name, quantity, supplier, project)
    print("Material updated successfully.")

def delete_material():
    id = int(input("Enter material ID to delete: "))
    Material.remove_material(id)
    print("Material deleted successfully.")

def add_supplier():
    name = input("Enter supplier name: ")
    material = input("Enter material supplied: ")
    supplier = Supplier(name, material)
    supplier.add_supplier()
    print("Supplier added successfully.")

def view_all_suppliers():
    suppliers = Supplier.get_suppliers()
    for supplier in suppliers:
        print(supplier)

def view_supplier_by_id():
    id = int(input("Enter supplier ID: "))
    supplier = Supplier.get_supplier(id)
    if supplier:
        print(supplier)
    else:
        print("Supplier not found.")

def update_supplier():
    id = int(input("Enter supplier ID to update: "))
    name = input("Enter new name: ")
    material = input("Enter new material: ")
    Supplier.update_supplier(id, name, material)
    print("Supplier updated successfully.")

def delete_supplier():
    id = int(input("Enter supplier ID to delete: "))
    Supplier.remove_supplier(id)
    print("Supplier deleted successfully.")

def add_project():
    name = input("Enter project name: ")
    material = input("Enter material for project: ")
    project = Project(name, material)
    project.add_project()
    print("Project added successfully.")

def view_all_projects():
    projects = Project.get_projects()
    for project in projects:
        print(project)

def view_project_by_id():
    id = int(input("Enter project ID: "))
    project = Project.get_project(id)
    if project:
        print(project)
    else:
        print("Project not found.")

def update_project():
    id = int(input("Enter project ID to update: "))
    name = input("Enter new name: ")
    material = input("Enter new material: ")
    Project.update_project(id, name, material)
    print("Project updated successfully.")

def delete_project():
    id = int(input("Enter project ID to delete: "))
    Project.remove_project(id)
    print("Project deleted successfully.")

def main():
    Material.create_table()
    Supplier.create_table()
    Project.create_table()
    while True:
        print_menu()
        choice = input("Enter choice: ")
        if choice == '1':
            add_material()
        elif choice == '2':
            view_all_materials()
        elif choice == '3':
            view_material_by_id()
        elif choice == '4':
            update_material()
        elif choice == '5':
            delete_material()
        elif choice == '6':
            add_supplier()
        elif choice == '7':
            view_all_suppliers()
        elif choice == '8':
            view_supplier_by_id()
        elif choice == '9':
            update_supplier()
        elif choice == '10':
            delete_supplier()
        elif choice == '11':
            add_project()
        elif choice == '12':
            view_all_projects()
        elif choice == '13':
            view_project_by_id()
        elif choice == '14':
            update_project()
        elif choice == '15':
            delete_project()
        elif choice == '16':
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
