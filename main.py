import flet
from scripts.appbar import create_appbar
from scripts.singlecard import create_Image
from scripts.card import create_cards
from scripts.virtcard import create_vert_card
def main(page:flet.Page):
    page.title = "الحج والعمرة"
    page.window.width=370
    page.window.height=810
    page.bgcolor ="#2c2c2c"
    page.theme_mode=flet.ThemeMode.DARK
    page.padding=0
    page.vertical_alignment=flet.MainAxisAlignment.CENTER
    page.horizontal_alignment=flet.CrossAxisAlignment.CENTER
    page.window.resizable=False
    page.window.maximizable=False
    page.window.minimizable=False
    page.scroll=flet.ScrollMode.AUTO
    

    
    page.add (
        create_appbar(),
        create_Image(),
        flet.Text("Family Resturant food",color=flet.Colors.AMBER),
        create_cards(),
        create_vert_card ()
    )





    page.update()

flet.app(target=main)
