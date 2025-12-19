import flet as ft 
from db import main_db
from datetime import datetime

def main (page:ft.Page):
    page.title = 'Список покупок'
    page.theme_mode = ft.ThemeMode.LIGHT
    product_list = ft.Column(spacing=15)

    filter_type = 'all'

    def load_product():
        product_list.controls.clear()
        for product_id, product_text, buyed in main_db.get_product(filter_type):
            product_list.controls.append(create_product_row(product_id=product_id, product_text=product_text, buyed=buyed))
        page.update()

    def create_product_row(product_id, product_text, buyed):

        checkbox = ft.Checkbox(value=bool(buyed), on_change=lambda e: toogle_product(product_id, e.control.value))


        def delete_product(_):
            main_db.delete_product(product_id)
            load_product()
            product_field.update()
            page.update()

        delete_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=delete_product)

        product_field = ft.TextField(value=product_text, expand=True)

        return ft.Row([checkbox, product_field, delete_button])

    def toogle_product(product_id, is_buyed):
        print(f'{product_id} - {int(is_buyed)}')
        main_db.update_products(product_id=product_id, buyed=int(is_buyed))
        load_product()
    
    def add_product(_):
        if product_input.value and len(product_input.value) <= 100: 
            product = product_input.value
            product_id = main_db.add_product(product)
            product_list.controls.append(create_product_row(product_id=product_id, product_text=product, buyed=None))
            print(f'Запись сохранена!, ID задачи -  {product_id}')
            product_input.value = None

        else: 
            product_input.error_text = 'Поле не должно быть пустым и превышать 100 символов'
            print('Поле не должно быть пустым и превышать 100 символов')
        page.update()

    product_input = ft.TextField(label="Введите продукт", expand=True, on_submit=add_product)
    product_input_button = ft.IconButton(icon=ft.Icons.SEND, on_click=add_product)

    def set_filter(filter_value):
         nonlocal filter_type
         filter_type = filter_value
         load_product()


    filter_buttons = ft.Row([
        ft.ElevatedButton('Все товары', on_click=lambda e: set_filter('all'), icon=ft.Icons.ALL_INBOX, icon_color=ft.Colors.YELLOW),
        ft.ElevatedButton('Некупленные', on_click=lambda e: set_filter('not_buyed'), icon=ft.Icons.WATCH_LATER, icon_color=ft.Colors.RED),
        ft.ElevatedButton('Купленные', on_click=lambda e: set_filter('buyed'), icon=ft.Icons.CHECK_BOX, icon_color=ft.Colors.GREEN)
    ],alignment=ft.MainAxisAlignment.SPACE_AROUND )

    main_objects = ft.Row([product_input, product_input_button])

    page.add(main_objects, filter_buttons, product_list)
    load_product()





if __name__ == '__main__':
    main_db.init_db()
    ft.app(target=main)

    
