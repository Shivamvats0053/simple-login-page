import flet as ft

def main(page: ft.Page):
    page.title = "Login Page"

    email = ft.TextField(label="Email")

    password = ft.TextField(
        label="Password",
        password=True
    )

    api_result = ft.Text("")

    def login(e):
        api_result.value = "API Called Successfully"
        page.update()

    login_button = ft.ElevatedButton(
        "Login",
        on_click=login
    )

    page.add(
        email,
        password,
        login_button,
        api_result
    )

ft.app(target=main)