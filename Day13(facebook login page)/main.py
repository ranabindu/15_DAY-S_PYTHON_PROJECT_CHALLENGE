from tkinter import *



class facebookLogin(Tk):
	def __init__(self):
		super().__init__()
		'''self.width, self.height = self.winfo_screenwidth(), self.winfo_screenheight()
		self.geometry('%dx%d+0+0' % (self.width,self.height))
		self.resizable(False, False)'''
		self.attributes("-fullscreen", True) 


		'''self.scrollBar= Scrollbar(self, orient = 'horizontal')
		self.scrollBar.pack(side = BOTTOM, fill = X)
		self.v = Scrollbar(self)
		self.v.pack(side = RIGHT, fill = Y)'''


	def Label(self):
		self.canvas = Canvas(self,width=420,height=378,bg="#fffcfc")
		self.canvas.place(x=849,y=175)


		self.canvas.create_line(28, 260, 400, 260)
		# upperbar
		self.title=Label(self,text="facebook",font="Arial 43 bold",fg="#427bff")
		self.title.place(x=230,y=210)

		self.facebooktagline1=Label(self,text="Facebook helps you connect and share",font="Leelawadee 20 ",fg="black")
		self.facebooktagline1.place(x=230,y=290)
		
		self.facebooktagline2=Label(self,text="with the people in your life.",font="Leelawadee 20 ",fg="black")
		self.facebooktagline2.place(x=230,y=323)


		self.bannerpic= PhotoImage(file='E:/sadow/python projects/Facebook Login Page/upperbar.png')

		self.banner=Label(self,image=self.bannerpic)               
		self.banner.place(x=0,y = 0)

	def Entry(self):
		self.username = Entry(self, width=30,font="Courier ",highlightthickness=1)
		self.username.insert(10, 'Username or Phonenumber')
		self.username.place(x=880,y=207,height=50)


		self.password = Entry(self, width=30,font="Courier",highlightthickness=1)
		self.password.insert(10, 'Password')
		self.password.place(x=880,y=267,height=50)




	def button(self):
		self.buttonImage=PhotoImage(file="E:/sadow/python projects/Facebook Login Page/button.png")
		self.button=Button(self,image=self.buttonImage,command=self.loginFunction,border=0)
		self.button.place(x=870,y=330)

		self.forgotpass=Button(self,text="Forgotten password?",command=self.loginFunction,border=0,bg="white",fg="blue",font="Leelawadee 10")
		self.forgotpass.place(x=1000,y=400)


		self.newaccbuttonImage=PhotoImage(file="E:/sadow/python projects/Facebook Login Page/newaccountbutton.png")
		self.newaccbutton=Button(self,image=self.newaccbuttonImage,command=self.loginFunction,border=0)
		self.newaccbutton.place(x=950,y=460)


	def loginFunction(self):
		pass


if __name__=="__main__":
	windows=facebookLogin()
	windows.Label()
	windows.Entry()
	windows.button()
	windows.mainloop()