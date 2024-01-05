import flet as ft

def main(page: ft.Page):
    page.title = "Simple Greetings App!"

    first_name = ft.TextField(label="first name", autofocus=True)
    last_name = ft.TextField(label="last name")

    greetings = ft.Column()

    def btn_click(e):
        greetings.controls.append(ft.Text(f"Hello {first_name.value} {last_name.value}!"))
        first_name.value = ""
        last_name.value = ""
        first_name.focus()
        page.update()

    hello = ft.ElevatedButton("Say Hello!", on_click=btn_click)

    page.add(
        first_name,
        last_name,
        hello,
        greetings,
    )

ft.app(target=main)
