import flet as ft
import os

def main(page: ft.Page):
    page.title = "Profile Screen"
    page.padding = 0
    page.scroll = "adaptive"
    page.bgcolor = "#F8F9FA"
    
    images_path = "static/images"

    profile_header = ft.Container(
        content=ft.Column(
            [
                ft.Container(
                    content=ft.Image(
                        src=images_path + "/home-image.jpg",
                        width=100,  
                        height=100,  
                        fit=ft.ImageFit.COVER,  
                        border_radius=50,  
                    ),
                    alignment=ft.alignment.center,
                ),
                ft.Row(
                    [
                        ft.Text("CJ Agpaoa", size=20, weight="bold"),
                        ft.Icon(ft.icons.VERIFIED, color="#1DA1F2", size=18),
                    ],
                    alignment="center",
                ),
                ft.Container(
                    content=ft.Text(
                        "Boston, USA",
                        size=14,
                        color="#6C757D",
                        text_align="center",
                    ),
                    alignment=ft.alignment.center,
                ),
                ft.Row(
                    [
                        ft.Text("350 Following", size=14, color="#6C757D"),
                        ft.Text(" • ", size=14, color="#6C757D"),
                        ft.Text("647 Followers", size=14, color="#6C757D"),
                    ],
                    alignment="center",
                ),
                ft.Row(
                    [
                        ft.ElevatedButton(
                            "Make Event",
                            style=ft.ButtonStyle(
                                bgcolor="#00A1FF",
                                shape=ft.RoundedRectangleBorder(radius=8),
                                padding=ft.Padding(20, 10, 20, 10),
                                color="white",
                            ),
                        ),
                        ft.OutlinedButton(
                            "Edit Profile",
                            style=ft.ButtonStyle(
                                side=ft.BorderSide(1, "#00A1FF"),
                                shape=ft.RoundedRectangleBorder(radius=8),
                                padding=ft.Padding(20, 10, 20, 10),
                            ),
                        ),
                    ],
                    alignment="center",
                    spacing=20,
                ),
            ],
            spacing=10,
            alignment="center",
        ),
        padding=15,
        alignment=ft.alignment.center,
    )

    friend_list_section = ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Text("Friend List", size=16, weight="bold"),
                        ft.TextButton("See all", on_click=lambda _: print("Friend list")),
                    ],
                    alignment="spaceBetween",
                ),
                ft.Row(
                    spacing=10,
                    controls=[
                        ft.Container(
                            content=ft.Image(
                                src=images_path + "/friendOne.jpg",  
                                width=50,  
                                height=50,  
                                fit=ft.ImageFit.COVER,  
                                border_radius=25,  
                            ),
                        ),
                        ft.Container(
                            content=ft.Image(
                                src=images_path + "/friendTwo.jpg",  
                                width=50,  
                                height=50,  
                                fit=ft.ImageFit.COVER,
                                border_radius=25,  
                            ),
                        ),
                        ft.Container(
                            content=ft.Image(
                                src=images_path + "/friendThree.jpg",  
                                width=50,  
                                height=50,  
                                fit=ft.ImageFit.COVER,
                                border_radius=25,  
                            ),
                        ),
                    ],
                    alignment="start",
                ),
            ],
        ),
        padding=15,
    )

    event_section = ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Text("Events", size=16, weight="bold"),
                        ft.TextButton("See all", on_click=lambda _: print("Events list")),
                    ],
                    alignment="spaceBetween",
                ),
                ft.Container(
                    content=ft.Row(
                        [
                            ft.Container(
                                content=ft.Row(
                                    [
                                        ft.Image(
                                            src=images_path + "/Event.png",  
                                            fit="cover",
                                            width=80,
                                            height=80,
                                        ),
                                        ft.Column(
                                            [
                                                ft.Text(
                                                    "Circuit Mega Festival - 2024",
                                                    weight="bold",
                                                    size=14,
                                                ),
                                                ft.Text("Makati City", size=12, color="#6C757D"),
                                            ],
                                            alignment="start",
                                            spacing=5,
                                        ),
                                    ],
                                    spacing=10,
                                ),
                                border_radius=8,
                                bgcolor="#FFFFFF",
                                padding=10,
                                shadow=ft.BoxShadow(blur_radius=4, spread_radius=1, color="#00000022"),
                            ),
                            ft.Container(
                                content=ft.Row(
                                    [
                                        ft.Image(
                                            src=images_path + "/EventTwo.jpg",  
                                            fit="cover",
                                            width=80,
                                            height=80,
                                        ),
                                        ft.Column(
                                            [
                                                ft.Text(
                                                    "Summer Beach Party - 2024",
                                                    weight="bold",
                                                    size=14,
                                                ),
                                                ft.Text("Boracay, Philippines", size=12, color="#6C757D"),
                                            ],
                                            alignment="start",
                                            spacing=5,
                                        ),
                                    ],
                                    spacing=10,
                                ),
                                border_radius=8,
                                bgcolor="#FFFFFF",
                                padding=10,
                                shadow=ft.BoxShadow(blur_radius=4, spread_radius=1, color="#00000022"),
                            ),
                        ],
                        spacing=20,
                    ),
                    padding=15,
                ),
            ],
            spacing=10,
        ),
        padding=15,
    )

    bio_section = ft.Container(
        content=ft.Column(
            [
                ft.Text("My Bio", size=16, weight="bold"),
                ft.Row(
                    controls=[
                        ft.Text(
                            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
                            size=14,
                            color="#6C757D",
                            overflow="ellipsis",
                            width=240,
                        ),
                        ft.TextButton("Read More", on_click=lambda _: print("Read more clicked")),
                    ],
                    alignment="start",
                    wrap=True,
                    spacing=10,
                ),
            ],
            spacing=10,
        ),
        padding=15,
    )

    interest_section = ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Text("My Interests", size=16, weight="bold"),
                        ft.IconButton(icon=ft.icons.EDIT, icon_size=18),
                    ],
                    alignment="spaceBetween",
                ),
                ft.Row(
                    wrap=True,
                    spacing=10,
                    controls=[
                        ft.Container(
                            content=ft.Text("Online Games", color="white"),
                            padding=10,
                            border_radius=15,
                            bgcolor="#FF6347",
                        ),
                        ft.Container(
                            content=ft.Text("Concert", color="white"),
                            padding=10,
                            border_radius=15,
                            bgcolor="#FFD700",
                        ),
                        ft.Container(
                            content=ft.Text("Music", color="white"),
                            padding=10,
                            border_radius=15,
                            bgcolor="#32CD32",
                        ),
                        ft.Container(
                            content=ft.Text("Art", color="white"),
                            padding=10,
                            border_radius=15,
                            bgcolor="#8A2BE2",
                        ),
                        ft.Container(
                            content=ft.Text("Movie", color="white"),
                            padding=10,
                            border_radius=15,
                            bgcolor="#00BFFF",
                        ),
                        ft.Container(
                            content=ft.Text("Coffee", color="white"),
                            padding=10,
                            border_radius=15,
                            bgcolor="#FF4500",
                        ),
                    ],
                ),
            ],
            spacing=5,
        ),
        padding=15,
    )

    bottom_nav = ft.Container(
        content=ft.Row(
            [
                ft.IconButton(icon=ft.icons.HOME, on_click=lambda _: print("Home clicked")),
                ft.IconButton(icon=ft.icons.FAVORITE, on_click=lambda _: print("Heart clicked")),
                ft.IconButton(icon=ft.icons.MESSAGE, on_click=lambda _: print("Message clicked")),
                ft.IconButton(icon=ft.icons.LOCATION_ON, on_click=lambda _: print("Location clicked")),
                ft.IconButton(icon=ft.icons.ACCOUNT_CIRCLE, on_click=lambda _: print("Profile clicked")),
            ],
            alignment="spaceAround",
        ),
        bgcolor="white",
        padding=10,
        shadow=ft.BoxShadow(blur_radius=10, color="#00000022"),
    )

    page.add(
        ft.Column(
            [
                profile_header,
                friend_list_section,
                event_section,
                bio_section,
                interest_section,
                bottom_nav, 
            ],
            spacing=10,
        )
    )

ft.app(target=main)
