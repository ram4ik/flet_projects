import flet as ft

def main(page: ft.Page):
    page.title = "ToDo App"

    def button_clicked(e):
        page.add(ft.Checkbox(label=input_text.value))

    input_text = ft.TextField(hint_text="What do you want to do today...", width=350)
    add_button = ft.ElevatedButton(text="Add", on_click=button_clicked)

    page.add(
        ft.Row(controls=[
                input_text,
                add_button,
            ]
        )
    )

ft.app(target=main)
