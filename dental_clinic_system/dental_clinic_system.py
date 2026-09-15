import reflex as rx
from .pages.home import home
from .pages.auth import auth

class State(rx.State):
    """The app state."""
    pass

app = rx.App()
app.add_page(home, route="/")
app.add_page(auth, route="/auth")
