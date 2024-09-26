import flet as ft
from io import BytesIO
import base64

def main(page: ft.Page):

    def open_qr_dialog(e):
        # 加载本地图片并将其转换为 base64 编码
        with open("/Users/alphabet/Documents/project/GUI/firstgui/assets/example.jpeg", "rb") as image_file:
            img_base64 = base64.b64encode(image_file.read()).decode('utf-8')

        # 创建弹出对话框显示图片
        dialog = ft.AlertDialog(
            title=ft.Text("二维码"),
            content=ft.Image(src="../assets/example.jpeg"),
            actions=[ft.TextButton("关闭", on_click=lambda e: close_dialog(dialog))],
        )
        # page.dialog = dialog
        page.overlay.append(dialog)
        dialog.open = True
        page.update()

        def close_dialog(dialog):
            dialog.open = False
            page.update()

    # 添加按钮
    page.add(ft.ElevatedButton("显示二维码", on_click=open_qr_dialog))

ft.app(target=main)
