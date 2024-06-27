import csv
import tkinter as tk
import random

with open('data/StudentData.csv', 'r') as f:
    reader = csv.reader(f)
    l = [row for row in reader]
f.close()

student_max = len(l)-1
csvdict = {"myouzi":0, "name":1, "weaponname":2, "school":3, "grade":4, "age":5, "birthday":6, "hobby1":7, "hobby2":8, "hobby3":9}


class TrinityExamPrep:
    def __init__(self, master):
        self.master = master
        master.title("トリニティでテスト勉強！")

        self.student_index = random.randint(0, student_max)

        frame_left = tk.Frame(master,height=670,width=400,relief="raised",bd=3)
        frame_left.place(x=10, y=10)

        frame_mid = tk.Frame(master,height=670,width=420,relief="raised",bd=3)
        frame_mid.place(x=420, y=10)

        frame_right = tk.Frame(master,height=670,width=420,relief="raised",bd=3)
        frame_right.place(x=850, y=10)

        # art
        self.art_file = tk.PhotoImage(file = "data/art/default.png")
        self.art_image = tk.Canvas(frame_left, width=350, height=630)
        self.art_image.create_image(175, 315, image=self.art_file)
        self.art_image.place(x=200, y=315, anchor="center")

        self.art_button = tk.Button(frame_left, text="立ち絵", font=("", 12), command=self.answer_art)
        self.art_button.place(x=200, y=640, anchor="center")

        # Halo
        self.halo_file = tk.PhotoImage(file = "data/halo/default.png")
        self.halo_image = tk.Canvas(frame_mid, width=350, height=350)
        self.halo_image.create_image(175, 175, image=self.halo_file)
        self.halo_image.place(x=200, y=175, anchor="center")

        self.halo_button = tk.Button(frame_mid, text="ヘイロー", font=("", 12), command=self.answer_halo)
        self.halo_button.place(x=200, y=360, anchor="center")

        # UE
        self.weapon_file = tk.PhotoImage(file = "data/weapon/default.png")
        self.weapon_image = tk.Canvas(frame_mid, width=380, height=200)
        self.weapon_image.create_image(190, 100, image=self.weapon_file)
        self.weapon_image.place(x=200, y=540, anchor="center")

        self.weapon_name = tk.Label(frame_mid, text="???", font=("", 24))
        self.weapon_name.place(x=200, y=420, anchor="center")

        self.weapon_name_button = tk.Button(frame_mid, text="武器名", font=("", 12), command=self.answer_weapon_name)
        self.weapon_name_button.place(x=250, y=640, anchor="center")

        self.weapon_image_button = tk.Button(frame_mid, text="武器", font=("", 12), command=self.answer_weapon)
        self.weapon_image_button.place(x=150, y=640, anchor="center")

        # school
        self.school = tk.Label(frame_right, text="???", font=("", 24))
        self.school.place(x=205, y=30, anchor="center")

        self.school_button = tk.Button(frame_right, text="所属学園", font=("", 12), command=self.answer_school)
        self.school_button.place(x=200, y=70, anchor="center")

        # name
        self.family_name = tk.Label(frame_right, text="???", font=("", 24))
        self.family_name.place(x=190, y=230, anchor="e")
        self.first_name = tk.Label(frame_right, text="???", font=("", 24))
        self.first_name.place(x=210, y=230, anchor="w")

        self.family_name_button = tk.Button(frame_right, text="苗字", font=("", 12), command=self.answer_family_name)
        self.family_name_button.place(x=195, y=270, anchor="e")
        self.first_name_button = tk.Button(frame_right, text="名前", font=("", 12), command=self.answer_first_name)
        self.first_name_button.place(x=205, y=270, anchor="w")

        # grade & age
        self.grade = tk.Label(frame_right, text="???", font=("", 24))
        self.grade.place(x=190, y=130, anchor="e")
        self.age = tk.Label(frame_right, text="???", font=("", 24))
        self.age.place(x=210, y=130, anchor="w")

        self.grade_button = tk.Button(frame_right, text="学年", font=("", 12), command=self.answer_grade)
        self.grade_button.place(x=195, y=170, anchor="e")
        self.age_button = tk.Button(frame_right, text="年齢", font=("", 12), command=self.answer_age)
        self.age_button.place(x=205, y=170, anchor="w")

        # birthday
        self.birthday = tk.Label(frame_right, text="???", font=("", 24))
        self.birthday.place(x=200, y=330, anchor="center")

        self.birthday_button = tk.Button(frame_right, text="誕生日", font=("", 12), command=self.answer_birthday)
        self.birthday_button.place(x=200, y=370, anchor="center")

        # hobby
        self.hobby1 = tk.Label(frame_right, text="???", font=("", 24))
        self.hobby1.place(x=200, y=450, anchor="center")
        self.hobby2 = tk.Label(frame_right, text="???", font=("", 24))
        self.hobby2.place(x=200, y=500, anchor="center")
        self.hobby3 = tk.Label(frame_right, text="???", font=("", 24))
        self.hobby3.place(x=200, y=550, anchor="center")

        self.hobby_button = tk.Button(frame_right, text="趣味", font=("", 12), command=self.answer_hobby)
        self.hobby_button.place(x=200, y=600, anchor="center")

        # misc
        self.next_button = tk.Button(master, text="次へ", font=("", 12), command=self.next_student)
        self.next_button.place(x=20, y=685)

        self.next_button = tk.Button(master, text="答え", font=("", 12), command=self.answer_all)
        self.next_button.place(x=110, y=685)
#-------------------------------------------------------------
# show answers
    def answer_art(self):
        filename = "data/art/" + l[self.student_index][csvdict["name"]] + ".png"
        self.art_file = tk.PhotoImage(file = filename)
        self.art_image.create_image(175,315,image=self.art_file)

    def answer_halo(self):
        filename = "data/halo/" + l[self.student_index][csvdict["name"]] + ".png"
        self.halo_file = tk.PhotoImage(file = filename)
        self.halo_image.create_image(175,175,image=self.halo_file)

    def answer_weapon(self):
        filename = "data/weapon/" + l[self.student_index][csvdict["name"]] + ".png"
        self.weapon_file = tk.PhotoImage(file = filename)
        self.weapon_image.create_image(190,100,image=self.weapon_file)

    def answer_school(self):
        self.school.config(text=l[self.student_index][csvdict["school"]])

    def answer_grade(self):
        if l[self.student_index][csvdict["grade"]].isdecimal():
            text = l[self.student_index][csvdict["grade"]] + "年生"
        else:
            text = l[self.student_index][csvdict["grade"]]

        self.grade.config(text=text)

    def answer_age(self):
        if l[self.student_index][csvdict["age"]].isdecimal():
            text = l[self.student_index][csvdict["age"]] + "歳"
        else:
            text = l[self.student_index][csvdict["age"]]

        self.age.config(text=text)

    def answer_weapon_name(self):
        if len(l[self.student_index][csvdict["weaponname"]]) > 13:
            self.weapon_name.config(text=l[self.student_index][csvdict["weaponname"]], font=("", 18))
        else:
            self.weapon_name.config(text=l[self.student_index][csvdict["weaponname"]], font=("", 24))

    def answer_family_name(self):
        self.family_name.config(text=l[self.student_index][csvdict["myouzi"]])

    def answer_first_name(self):
        self.first_name.config(text=l[self.student_index][csvdict["name"]])

    def answer_birthday(self):
        self.birthday.config(text=l[self.student_index][csvdict["birthday"]])

    def answer_hobby(self):
        self.hobby1.config(text=l[self.student_index][csvdict["hobby1"]])
        self.hobby2.config(text=l[self.student_index][csvdict["hobby2"]])
        self.hobby3.config(text=l[self.student_index][csvdict["hobby3"]])


    def answer_all(self):
        self.answer_art()
        self.answer_halo()
        self.answer_weapon()
        self.answer_weapon_name()
        self.answer_school()
        self.answer_age()
        self.answer_grade()
        self.answer_family_name()
        self.answer_first_name()
        self.answer_birthday()
        self.answer_hobby()

# reset
    def next_student(self):
        self.art_file = tk.PhotoImage(file = "data/art/default.png")
        self.art_image.create_image(175,315,image=self.art_file)
        self.halo_file = tk.PhotoImage(file = "data/halo/default.png")
        self.halo_image.create_image(175,175,image=self.halo_file)
        self.weapon_file = tk.PhotoImage(file = "data/weapon/default.png")
        self.weapon_image.create_image(190,100,image=self.weapon_file)
        self.weapon_name.config(text="???")
        self.family_name.config(text="???", font=("", 24))
        self.first_name.config(text="???")
        self.school.config(text="???")
        self.grade.config(text="???")
        self.age.config(text="???")
        self.birthday.config(text="???")
        self.hobby1.config(text="???")
        self.hobby2.config(text="???")
        self.hobby3.config(text="???")

        self.student_index = random.randint(0, student_max)


if __name__ == "__main__":
    root = tk.Tk()
    root.minsize(1280, 720)
    root.resizable(False, False)
    app = TrinityExamPrep(root)
    iconphoto = tk.PhotoImage(file = "data/icon.png")  
    root.iconphoto(False, iconphoto)
    root.mainloop()
