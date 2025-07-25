import flet as ft


def main(page: ft.Page):

    c = ft.Image(
        src="https://picsum.photos/200/300?1",
        width=200,
        height=300,
        offset=ft.Offset(-2, 0),
        animate_offset=ft.Animation(300, ft.AnimationCurve.BOUNCE_OUT),
    )

    def animate(e):
        c.offset = ft.Offset(0, 0)
        c.update()

    page.add(
        c,
        ft.ElevatedButton("Reveal the image!", on_click=animate),
    )


ft.app(main)
