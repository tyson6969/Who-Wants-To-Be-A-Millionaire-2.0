from tkinter import *
# import pygame

#pygame.init()
root = Tk()
root.title("Who wants to be a millionaire 2.0")
root.geometry("1352x652+0+0")
root.configure(bg="black")
#==================================================================questions====================================================================
questions_list = [
    "What does HTML stand for?",
    "Which programming language is mainly used for web styling?",
    "What is the main purpose of a firewall?",
    "What does 'phishing' mean in cybersecurity?",
    "Which of these is a strong password?",
    "What does CPU stand for?",
    "Which language is best known for ethical hacking and scripting?",
    "What is an IP address used for?",
    "Which operating system is most commonly used by hackers?",
    "What does VPN stand for?",
    "Which tool is used to find security weaknesses legally?",
    "What is open-source software?",
    "What does encryption do?",
    "Which of these is NOT a programming language?",
    "What is two-factor authentication (2FA)?"
]

first_options = [
    "HyperText Markup Language",
    "CSS",
    "To block unauthorized access",
    "Stealing data using fake emails",
    "P@ssw0rd123!",
    "Central Processing Unit",
    "Python",
    "Identifying a device on a network",
    "Linux",
    "Virtual Private Network",
    "Penetration testing tools",
    "Software with publicly available code",
    "Protects data by scrambling it",
    "HTML",
    "Using two methods to verify identity"
]

second_options = [
    "HighText Machine Language",
    "JavaScript",
    "To speed up the internet",
    "Sending spam messages",
    "123456",
    "Computer Power Unit",
    "C++",
    "Storing files online",
    "Windows",
    "Verified Public Network",
    "Antivirus software",
    "Software you must pay for",
    "Deletes data permanently",
    "HTTP",
    "Using two passwords"
]

third_options = [
    "Hyperlinks and Text Markup Language",
    "HTML",
    "To create viruses",
    "Guessing passwords",
    "password",
    "Control Processing Unit",
    "Java",
    "Tracking website visits",
    "macOS",
    "Visual Protocol Network",
    "Game engines",
    "Software with hidden code",
    "Makes data faster",
    "Python",
    "Using a fingerprint only"
]

fourth_options = [
    "Home Tool Markup Language",
    "Python",
    "To design websites",
    "Monitoring network traffic",
    "qwerty",
    "Core Processing Unit",
    "Assembly",
    "Sending emails",
    "Android",
    "Virtual Public Network",
    "Hacking tools for crime",
    "Illegal software",
    "Compresses data",
    "Photoshop",
    "Logging in once"
]

# Correct answers (optional)
correct_answers = [
    1,  # HyperText Markup Language
    1,  # CSS
    1,  # To block unauthorized access
    1,  # Stealing data using fake emails
    1,  # P@ssw0rd123!
    1,  # Central Processing Unit
    1,  # Python
    1,  # Identifying a device on a network
    1,  # Linux
    1,  # Virtual Private Network
    1,  # Penetration testing tools
    1,  # Software with publicly available code
    1,  # Protects data by scrambling it
    4,  # Photoshop
    1   # Using two methods to verify identity
]



#=========================================================frames=============================================================================

mainframe = Frame(root, bg="black")
mainframe.grid()

mainframe1 = Frame(root, bg="black", bd =20,width=900, height=600)
mainframe1.grid(row = 0, column=0)

mainframe2 = Frame(root, bg="black", bd =20,width=452, height=600)
mainframe2.grid(row = 0, column=1)

mainframe1a = Frame(mainframe1, bg="black", bd =20,width=900, padx=130 , height=200)
mainframe1a.grid(row = 0, column=0)
mainframe1b = Frame(mainframe1, bg="black", bd =20,width=900, height=200)
mainframe1b.grid(row = 1, column=0)
mainframe1c = Frame(mainframe1, bg="black", bd =20,width=900, height=200)
mainframe1c.grid(row = 2, column=0)


#========================================================defs==============================================================================

def change_img_50_50() :
 canvas = Canvas(mainframe1a, width=180, height=80, bg="black", bd=0, highlightthickness=0)
 canvas.grid(row=0, column=0)
 canvas.delete("all")
 image50_50x = PhotoImage(file="jpge50x.png")
 canvas.create_image(90, 40, image=image50_50x)
 canvas.image = image50_50x

def change_img_aud() :
 canvas1 = Canvas(mainframe1a, width=180, height=80, bg="black", bd=0, highlightthickness=0)
 canvas1.grid(row=0, column=1)
 canvas1.delete("all")
 imageaudx = PhotoImage(file="jpgepeoplex.png")
 canvas1.create_image(90, 40, image=imageaudx)
 canvas1.image = imageaudx

def change_img_phone() :
 canvas2 = Canvas(mainframe1a, width=180, height=80, bg="black", bd=0, highlightthickness=0)
 canvas2.grid(row=0, column=2)
 canvas2.delete("all")
 imagephonex = PhotoImage(file="jpgePhonex.png")
 canvas2.create_image(90, 40, image=imagephonex)
 canvas2.image = imagephonex
                    
def millionpictures1():
 canvas = Canvas(mainframe2, width=380, height=600, bg="black", bd=0, highlightthickness=0)
 canvas.grid(row=0, column=0)
 canvas.delete("all")
 image = PhotoImage(file="Picture1.png")
 canvas.create_image(215, 300, image=image)
 canvas.image = image

def millionpictures2():
 canvas = Canvas(mainframe2, width=380, height=600, bg="black", bd=0, highlightthickness=0)
 canvas.grid(row=0, column=0)
 canvas.delete("all")
 image = PhotoImage(file="Picture2.png")
 canvas.create_image(215, 300, image=image)
 canvas.image = image

def millionpictures3():
 canvas = Canvas(mainframe2, width=380, height=600, bg="black", bd=0, highlightthickness=0)
 canvas.grid(row=0, column=0)
 canvas.delete("all")
 image = PhotoImage(file="Picture3.png")
 canvas.create_image(215, 300, image=image)
 canvas.image = image

def millionpictures4():
 canvas = Canvas(mainframe2, width=380, height=600, bg="black", bd=0, highlightthickness=0)
 canvas.grid(row=0, column=0)
 canvas.delete("all")
 image = PhotoImage(file="Picture4.png")
 canvas.create_image(215, 300, image=image)
 canvas.image = image

def millionpictures5():
 canvas = Canvas(mainframe2, width=380, height=600, bg="black", bd=0, highlightthickness=0)
 canvas.grid(row=0, column=0)
 canvas.delete("all")
 image = PhotoImage(file="Picture5.png")
 canvas.create_image(215, 300, image=image)
 canvas.image = image

def millionpictures6():
 canvas = Canvas(mainframe2, width=380, height=600, bg="black", bd=0, highlightthickness=0)
 canvas.grid(row=0, column=0)
 canvas.delete("all")
 image = PhotoImage(file="Picture6.png")
 canvas.create_image(215, 300, image=image)
 canvas.image = image

def millionpictures7():
 canvas = Canvas(mainframe2, width=380, height=600, bg="black", bd=0, highlightthickness=0)
 canvas.grid(row=0, column=0)
 canvas.delete("all")
 image = PhotoImage(file="Picture7.png")
 canvas.create_image(215, 300, image=image)
 canvas.image = image

def millionpictures8():
 canvas = Canvas(mainframe2, width=380, height=600, bg="black", bd=0, highlightthickness=0)
 canvas.grid(row=0, column=0)
 canvas.delete("all")
 image = PhotoImage(file="Picture8.png")
 canvas.create_image(215, 300, image=image)
 canvas.image = image

def millionpictures9():
 canvas = Canvas(mainframe2, width=380, height=600, bg="black", bd=0, highlightthickness=0)
 canvas.grid(row=0, column=0)
 canvas.delete("all")
 image = PhotoImage(file="Picture9.png")
 canvas.create_image(215, 300, image=image)
 canvas.image = image

def millionpictures10():
 canvas = Canvas(mainframe2, width=380, height=600, bg="black", bd=0, highlightthickness=0)
 canvas.grid(row=0, column=0)
 canvas.delete("all")
 image = PhotoImage(file="Picture10.png")
 canvas.create_image(215, 300, image=image)
 canvas.image = image

def millionpictures11():
 canvas = Canvas(mainframe2, width=380, height=600, bg="black", bd=0, highlightthickness=0)
 canvas.grid(row=0, column=0)
 canvas.delete("all")
 image = PhotoImage(file="Picture11.png")
 canvas.create_image(215, 300, image=image)
 canvas.image = image

def millionpictures12():
 canvas = Canvas(mainframe2, width=380, height=600, bg="black", bd=0, highlightthickness=0)
 canvas.grid(row=0, column=0)
 canvas.delete("all")
 image = PhotoImage(file="Picture12.png")
 canvas.create_image(215, 300, image=image)
 canvas.image = image

def millionpictures13():
 canvas = Canvas(mainframe2, width=380, height=600, bg="black", bd=0, highlightthickness=0)
 canvas.grid(row=0, column=0)
 canvas.delete("all")
 image = PhotoImage(file="Picture13.png")
 canvas.create_image(215, 300, image=image)
 canvas.image = image

def millionpictures14():
 canvas = Canvas(mainframe2, width=380, height=600, bg="black", bd=0, highlightthickness=0)
 canvas.grid(row=0, column=0)
 canvas.delete("all")
 image = PhotoImage(file="Picture14.png")
 canvas.create_image(215, 300, image=image)
 canvas.image = image

def millionpictures15():
 canvas = Canvas(mainframe2, width=380, height=600, bg="black", bd=0, highlightthickness=0)
 canvas.grid(row=0, column=0)
 canvas.delete("all")
 image = PhotoImage(file="Picture15.png")
 canvas.create_image(215, 300, image=image)
 canvas.image = image




#========================================================images==============================================================================


centerImage = PhotoImage(file= 'center.png')
logocenter = Label(mainframe1b, image=centerImage, bg="black", width=300, height=200 ,border=0)
logocenter.grid()

imagelifeline50_50 = PhotoImage(file= 'jpge50.png')
lifeline50_50 = Button(mainframe1a, image=imagelifeline50_50, bg="black", width=180, height=80 ,border=0, command=change_img_50_50, bd=0)
lifeline50_50.grid(row=0, column=0,)

imagelifelineaud = PhotoImage(file= 'jpgePeople.png')
lifelineaud = Button(mainframe1a, image=imagelifelineaud, bg="black", width=180, height=80 ,border=0, command=change_img_aud)
lifelineaud.grid(row=0, column=1,)

imagelifelinecall = PhotoImage(file= 'jpgePhone.png')
lifelinecall = Button(mainframe1a, image=imagelifelinecall, bg="black", width=180, height=80 ,border=0, command=change_img_phone)
lifelinecall.grid(row=0, column=2)

moneyimage = PhotoImage(file= 'Picture0.png')
money = Label(mainframe2, image=moneyimage, bg="black", width=380, height=600, border=0)
money.grid(row=0, column=0)

layimage = PhotoImage(file= 'lay.png')
lay = Label(mainframe1c, image=layimage, bg="black", border=0)
lay.grid(row=0, column=0)
#==================================================================questions====================================================================

questionarea = Text(mainframe1c, font=('arial', 18, "bold"), width=30, height=2, wrap=WORD, bg="black", fg="white", bd=0)
questionarea.place(x=70, y=10, )
questionarea.insert(END, questions_list[0])
questionarea.tag_configure("center", justify=CENTER, )
questionarea.tag_add("center", "1.0", END)

LabelA=Label(mainframe1c, font=('arial', 16, 'bold'), text="A: ", bg='black', fg="white")
LabelA.place(x=40, y=109)
optionA=Button(mainframe1c, text=first_options[0], font=('arial',10,"bold"),bg="black", fg="white", bd=0, activebackground="black",activeforeground="white", cursor="hand2", wraplength=200)
optionA.place(x=70 , y=110)


LabelB=Label(mainframe1c, font=('arial', 16, 'bold'), text="B: ", bg='black', fg="white")
LabelB.place(x=310, y=109)
optionB=Button(mainframe1c, text=second_options[0], font=('arial',10,"bold"),bg="black", fg="white", bd=0, activebackground="black",activeforeground="white", cursor="hand2", wraplength=200)
optionB.place(x=350 , y=110)

LabelC=Label(mainframe1c, font=('arial', 16, 'bold'), text="C: ", bg='black', fg="white")
LabelC.place(x=40, y=195)
optionC=Button(mainframe1c, text=third_options[0], font=('arial',10,"bold"),bg="black", fg="white", bd=0, activebackground="black",activeforeground="white", cursor="hand2", wraplength=200)
optionC.place(x=70 , y=195)

LabelD=Label(mainframe1c, font=('arial', 16, 'bold'), text="D: ", bg='black', fg="white")
LabelD.place(x=310, y=195)
optionD=Button(mainframe1c, text=fourth_options[0], font=('arial',10,"bold"),bg="black", fg="white", bd=0, activebackground="black",activeforeground="white", cursor="hand2", wraplength=200)
optionD.place(x=350 , y=195)







#==================================================================text.label.button====================================================================
# txtquestions = Entry(mainframe1c, font=("arial",18,'bold'), bg="blue", fg="white", bd=5,width=44, justify=CENTER)
# txtquestions.grid(row=0, column=0, columnspan=4,pady = 4)

# lblquestA = Label(mainframe1c, font=("arial",14,'bold'), text='A: ' ,bg="black", fg="white", bd=5, justify=CENTER)
# lblquestA.grid(row=1, column=0, pady = 4, sticky=W)

# txtquestionsA = Button(mainframe1c, font=("arial",14,'bold'), bg="blue", fg="white", bd=0, width=17, height=2, justify=CENTER, activebackground="black", highlightbackground="black")
# txtquestionsA.grid(row=1, column=1, pady=4)

# lblQuestB = Label(mainframe1c, font=('arial', 14, 'bold'), text="B: ", bg='black', fg="white", justify=LEFT)
# lblQuestB.grid(row=1, column=2, sticky=W)

# txtQuestionB = Button(mainframe1c, font=('arial', 14, 'bold'), bg="blue", fg="white", bd=0, width=17, height=2, justify=CENTER, activebackground="black", highlightbackground="black")
# txtQuestionB.grid(row=1, column=3, pady=4)

# lblQuestC = Label(mainframe1c, font=('arial', 14, 'bold'), text="C: ", bg='black', fg="white", justify=LEFT)
# lblQuestC.grid(row=2, column=0, sticky=W)

# txtQuestionC = Button(mainframe1c, font=('arial', 14, 'bold'), bg="blue", fg="white", bd=0, width=17, height=2, justify=CENTER, activebackground="black", highlightbackground="black")
# txtQuestionC.grid(row=2, column=1, pady=4)

# lblQuestD = Label(mainframe1c, font=('arial', 14, 'bold'), text="D: ", bg='black', fg="white", justify=LEFT)
# lblQuestD.grid(row=2, column=2, sticky=W)

# txtQuestionD = Button(mainframe1c, font=('arial', 14, 'bold'), bg="blue", fg="white", bd=0, width=17, height=2, justify=CENTER, activebackground="black", highlightbackground="black")
# txtQuestionD.grid(row=2, column=3, pady=4)





root.mainloop()
