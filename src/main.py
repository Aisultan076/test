import flet as ft
from database import Database

db = Database()

def main(page: ft.Page):
    page.title = "Контакты"
    page.vertical_alignment = ft.MainAxisAlignment.START

    name_field = ft.TextField(label="Имя")
    phone_field = ft.TextField(label="Телефон")
    note_field = ft.TextField(label="Пометка")

    contact_table = ft.Column()

    def load_contacts():
        contact_table.controls.clear()
        contacts = db.get_all_contacts()
        for contact in contacts:
            contact_id, name, phone, note = contact
            row = ft.Row([
                ft.Text(name, width=150),
                ft.Text(phone, width=120),
                ft.Text(note, width=150),
                ft.IconButton(icon=ft.Icons.DELETE, on_click=lambda e, id=contact_id: delete_contact(id)),
            ])
            contact_table.controls.append(row)
        page.update()

    def add_contact(e):
        name = name_field.value
        phone = phone_field.value
        note = note_field.value
        if name and phone:
            db.add_contact(name, phone, note)
            name_field.value = ""
            phone_field.value = ""
            note_field.value = ""
            load_contacts()

    def delete_contact(contact_id):
        db.delete_contact(contact_id)
        load_contacts()

    def clear_all(e):
        db.clear_all_contacts()
        load_contacts()

    add_button = ft.ElevatedButton("Добавить", on_click=add_contact)
    clear_button = ft.ElevatedButton("Очистить всё", on_click=clear_all, bgcolor=ft.colors.RED_300)

    page.add(
        name_field,
        phone_field,
        note_field,
        ft.Row([add_button, clear_button]),
        ft.Text("Список контактов:", style="headlineSmall"),
        contact_table
    )

    load_contacts()

ft.app(target=main)
