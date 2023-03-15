import csv
from email.mime import image
import random
import PySimpleGUI as sg

with open('StudentData.csv', 'r') as f:
    reader = csv.reader(f)
    l = [row for row in reader]
f.close()

csvdict = {"num":0, "myouzi":1, "name":2, "romaji":3, "weaponname":4, "school":5, "grade":6, "age":7, "birthday":8, "hobby1":9, "hobby2":10, "hobby3":11}

qnumber = random.randrange(1, 84, 1)

frame1 = sg.Frame('', [ [sg.Button("ヘイローを表示")],
                        [sg.Image(filename="halo\defaultHalo.png", key="-halo-")],
                        [sg.Text(" ", font=("IPAゴシック", 24))],
                        [sg.Button("武器名を表示"), sg.Button("固有武器を表示")],
                        [sg.Text("??????????", key="-weponname-", text_color="Black", font=("IPAゴシック", 18))],
                        [sg.Image(filename="weapon\defaultWeapon.png", key="-weapon-")]
                        ], size=(400, 700), element_justification="c")

frame2 = sg.Frame('', [
                        [sg.Button("学校名を表示")],
                        [sg.Text("??????????", key="-school-", text_color="Black", font=("IPAゴシック", 24))],
                        [sg.Text(" ", font=("IPAゴシック", 36))],
                        [sg.Button("学年を表示"), sg.Button("年齢を表示")],
                        [sg.Text("???", key="-grade-", text_color="Black", font=("IPAゴシック", 24)), sg.Text("???", key="-age-", text_color="Black", font=("IPAゴシック", 24))],
                        [sg.Text(" ", font=("IPAゴシック", 36))],
                        [sg.Button("誕生日を表示")],
                        [sg.Text("?????????", key="-birthday-", text_color="Black", font=("IPAゴシック", 24))],
                        [sg.Text(" ", font=("IPAゴシック", 36))],
                        [sg.Button("趣味を表示")],
                        [sg.Text("?????", key="-hobby1-", text_color="Black", font=("IPAゴシック", 24))],
                        [sg.Text("?????", key="-hobby2-", text_color="Black", font=("IPAゴシック", 24))],
                        [sg.Text("?????", key="-hobby3-", text_color="Black", font=("IPAゴシック", 24))],
                        [sg.Text(" ", font=("IPAゴシック", 36))],
                        [sg.Button("苗字を表示"), sg.Button("名前を表示")],
                        [sg.Text("???", key="-myouzi-", text_color="Black", font=("IPAゴシック", 24)), sg.Text("???", key="-name-", text_color="Black", font=("IPAゴシック", 24))]
                        ], size=(400, 700), element_justification="c")

layout = [ [frame1, frame2],
            [sg.Button("答えを表示"), sg.Button("次の問題へ")] ]

window = sg.Window("トリニティでテスト勉強！", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "終了":
        break
    if event == "ヘイローを表示":
        window["-halo-"].update(filename="halo\\" + l[qnumber][csvdict["romaji"]] + "Halo.png")
    if event == "固有武器を表示":
        window["-weapon-"].update(filename="weapon\\" + l[qnumber][csvdict["romaji"]] + "Weapon.png")
    if event == "武器名を表示":
        window["-weponname-"].update(l[qnumber][csvdict["weaponname"]])
    if event == "学校名を表示":
        window["-school-"].update(l[qnumber][csvdict["school"]])
    if event == "学年を表示":
        window["-grade-"].update(l[qnumber][csvdict["grade"]] + "年生")
    if event == "年齢を表示":
        window["-age-"].update(l[qnumber][csvdict["age"]] + "歳")
    if event == "誕生日を表示":
        window["-birthday-"].update(l[qnumber][csvdict["birthday"]])
    if event == "趣味を表示":
        window["-hobby1-"].update(l[qnumber][csvdict["hobby1"]])
        window["-hobby2-"].update(l[qnumber][csvdict["hobby2"]])
        window["-hobby3-"].update(l[qnumber][csvdict["hobby3"]])
    if event == "苗字を表示":
        window["-myouzi-"].update(l[qnumber][csvdict["myouzi"]])
    if event == "名前を表示":
        window["-name-"].update(l[qnumber][csvdict["name"]])
    if event == "答えを表示":
        window["-halo-"].update(filename="halo\\" + l[qnumber][csvdict["romaji"]] + "Halo.png")
        window["-weapon-"].update(filename="weapon\\" + l[qnumber][csvdict["romaji"]] + "Weapon.png")
        window["-myouzi-"].update(l[qnumber][csvdict["myouzi"]])
        window["-name-"].update(l[qnumber][csvdict["name"]])
        window["-weponname-"].update(l[qnumber][csvdict["weaponname"]])
        window["-school-"].update(l[qnumber][csvdict["school"]])
        window["-grade-"].update(l[qnumber][csvdict["grade"]] + "年生")
        window["-age-"].update(l[qnumber][csvdict["age"]] + "歳")
        window["-birthday-"].update(l[qnumber][csvdict["birthday"]])
        window["-hobby1-"].update(l[qnumber][csvdict["hobby1"]])
        window["-hobby2-"].update(l[qnumber][csvdict["hobby2"]])
        window["-hobby3-"].update(l[qnumber][csvdict["hobby3"]])
        window["-myouzi-"].update(l[qnumber][csvdict["myouzi"]])
        window["-name-"].update(l[qnumber][csvdict["name"]])
    if event == "次の問題へ":
        window["-halo-"].update(filename="halo\defaultHalo.png")
        window["-weapon-"].update(filename="weapon\defaultWeapon.png")
        window["-weponname-"].update("??????????")
        window["-school-"].update("??????????")
        window["-grade-"].update("???")
        window["-age-"].update("???")
        window["-birthday-"].update("?????????")
        window["-hobby1-"].update("?????")
        window["-hobby2-"].update("?????")
        window["-hobby3-"].update("?????")
        window["-myouzi-"].update("???")
        window["-name-"].update("???")
        qnumber = random.randrange(1, 84, 1)

window.close()