from guizero import App, Text, info, Box, PushButton
from random import randint
app = App("gián điệp.core", width=546, height= 587)
box_text = Box(app, width=900, height=50)
text = Text(box_text, "Gián điệp đang nằm ở đây?", size=22, color="blue")
box = Box(app, width=546, height=540, layout="grid", border=True)
x= 0
y = 0
limit = 5
ranx = randint(0, 2)
rany = randint(0, 2)
def gian_diep(z, c, n):
    global ranx, rany, limit
    if z == ranx and c == rany:
        n.text = ""
        n.image = "roland.png"
        n.width = 176
        n.height = 173
        n.bg="#696969"
        info("thong bao", "Chúc mừng bạn đã tìm được gián điệp")
        app.destroy()
    else:
        info("thong bao", "Ôi no, không phải là vị trí của gián điệp")
        n.image = "sai.jpg"
        n.width = 176
        n.height = 173
        n.disable()
        limit -= 1
        if limit <= 0:
            info("thong bao", "bạn đã để đủ thời gian cho gián điệp trốn thoát")
            app.destroy()
for i in range(3):
    for j in range(3):
        push = PushButton(box, image="invite.jpg" ,width=176, height=173, grid=[i, j], command= gian_diep, args=[i, j])
        push.update_command(gian_diep, [i, j, push])
app.display()