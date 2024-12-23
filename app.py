import flet as ft
import os

def main(page: ft.Page):

    page.title = "Profile Screen"
    page.padding = 0
    page.scroll = "adaptive"
    page.bgcolor = "#F8F9FA"

    images_path = os.path.join(os.getcwd(), "static", "images")

  
    profile_header = ft.Container(
    content=ft.Column(
        [
            
            ft.Row(
                [
                    
                    ft.Row(
                        [
                            ft.Icon(
                                name=ft.Icons.ARROW_BACK,  
                                size=24,
                                color="black",  
                            ),
                            ft.Text(
                                "Profile",
                                size=18,
                                weight="bold",
                            ),
                        ],
                        alignment="start", 
                        vertical_alignment="center",
                    ),
                    
                    ft.Icon(
                        name=ft.Icons.MORE_VERT,  
                        size=24,
                        color="black",  
                    ),
                ],
                alignment="spaceBetween",  
                vertical_alignment="center",
            ),
            
            ft.Container(
                content=ft.Image(
                    src=os.path.join(images_path, "profile.jpg"),
                    width=100,
                    height=100,
                    fit=ft.ImageFit.COVER,
                    border_radius=50,
                ),
                alignment=ft.alignment.center,
            ),
            
            ft.Container(
                content=ft.Image(
                    src=os.path.join(images_path, "Group 33832.png"),  
                    width=80,  
                    fit=ft.ImageFit.CONTAIN,
                ),
                alignment=ft.alignment.center,
            ),
            
            ft.Row(
                [
                    ft.Text("CJ Agpaoa", size=20, weight="bold"),
                    ft.Icon(ft.Icons.VERIFIED, color="#1DA1F2", size=18),
                ],
                alignment="center",
            ),
            
            ft.Container(
                content=ft.Image(
                    src=os.path.join(images_path, "Group 33817.png"),
                    width=150,  
                    fit=ft.ImageFit.CONTAIN,
                ),
                alignment=ft.alignment.center,
            ),
            
            ft.Container(
                content=ft.Image(
                    src=os.path.join(images_path, "Group 33839.png"),
                    width=200,  
                    fit=ft.ImageFit.CONTAIN,
                ),
                alignment=ft.alignment.center,
            ),
            
            ft.Row(
                [
                    ft.Container(
                        content=ft.Image(
                            src=os.path.join(images_path, "action_1.png"),
                            width=120,  
                            fit=ft.ImageFit.CONTAIN,
                        ),
                    ),
                    ft.Container(
                        content=ft.Image(
                            src=os.path.join(images_path, "Actions.png"),
                            width=120,  
                            fit=ft.ImageFit.CONTAIN,
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
                    
                    ft.Container(
                        content=ft.Image(
                            src=os.path.join(images_path, "Group 33791.png"),
                            fit=ft.ImageFit.CONTAIN,
                        ),
                        on_click=lambda _: print("Friend list clicked"),
                    ),
                ],
                alignment="spaceBetween",
            ),
            ft.Row(
                spacing=10,
                controls=[
                    ft.Container(
                        content=ft.Image(
                            src=os.path.join(images_path, "friendOne.jpg"),
                            width=50,
                            height=50,
                            fit=ft.ImageFit.COVER,
                            border_radius=25,
                        ),
                    ),
                    ft.Container(
                        content=ft.Image(
                            src=os.path.join(images_path, "friendTwo.jpg"),
                            width=50,
                            height=50,
                            fit=ft.ImageFit.COVER,
                            border_radius=25,
                        ),
                    ),
                    ft.Container(
                        content=ft.Image(
                            src=os.path.join(images_path, "friendThree.jpg"),
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
                    ft.Container(
                        content=ft.Image(
                            src=os.path.join(images_path, "Group 33791.png"),
                            fit=ft.ImageFit.CONTAIN,
                        ),
                        on_click=lambda _: print("Events list clicked"),
                    ),
                ],
                alignment="spaceBetween",
            ),
            ft.Container(
                content=ft.Row(
                    [
                        ft.Container(
                            content=ft.Image(
                                src=os.path.join(images_path, "Group 33741.png"),
                                fit=ft.ImageFit.COVER,
                                width=350,  
                                height=200,  
                            ),
                            alignment=ft.alignment.center,  
                            padding=ft.padding.all(5),  
                        ),
                    ],
                    alignment="start",  
                    spacing=10,  
                ),
                padding=ft.padding.all(10),  
            ),
        ],
        spacing=10, 
    ),
    padding=ft.padding.all(10),  
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
                        content=ft.Image(
                            src=os.path.join(images_path, "Frame 18781.png"),
                            fit=ft.ImageFit.CONTAIN,
                        ),
                    
                    ),
                    ft.Container(
                        content=ft.Image(
                            src=os.path.join(images_path, "Frame 18782.png"),
                            fit=ft.ImageFit.CONTAIN,
                        ),
                       
                        
                    ),
                    ft.Container(
                        content=ft.Image(
                            src=os.path.join(images_path, "Frame 18783.png"),
                            fit=ft.ImageFit.CONTAIN,
                        ),
                      
                        
                    ),
                    ft.Container(
                        content=ft.Image(
                            src=os.path.join(images_path, "Frame 18785.png"),
                            fit=ft.ImageFit.CONTAIN,
                        ),
                      
                        
                    ),
                    ft.Container(
                        content=ft.Image(
                            src=os.path.join(images_path, "Frame 18784.png"),
                            fit=ft.ImageFit.CONTAIN,
                        ),
                    
                      
                    ),
                    ft.Container(
                        content=ft.Image(
                            src=os.path.join(images_path, "Frame 18786.png"),
                            fit=ft.ImageFit.CONTAIN,
                        ),
                      
                        
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
