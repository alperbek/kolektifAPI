# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from rich.console import Console

from flask import request

konsol = Console(log_path=False)

def hata(yazi):
   konsol.print(yazi, style="bold red")
def bilgi(yazi):
   konsol.print(yazi, style="blue")
def basarili(yazi):
   konsol.print(yazi, style="bold green")
def onemli(yazi):
   konsol.print(yazi, style="bold cyan")
def soru(soru):
   return konsol.input(f"[bold yellow]{soru}[/]")
def logVer():
    konsol.log(f"[green]IP Bilgisi :[/] [bold red]{request.remote_addr}[/]  [blue]--[/]  [green]GET :[/] [bold yellow]{request.host_url[:-1]}{request.full_path}[/]", highlight=False)


# import logging
# from rich.logging import RichHandler

# logging.basicConfig(
#     level="NOTSET", format="%(message)s", datefmt="[%X]", handlers=[RichHandler()]
# )

# log = logging.getLogger("rich")

# from flask.logging import default_handler

# log.addHandler(default_handler)