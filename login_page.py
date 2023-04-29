from tkinter import *
from functools import partial
from PIL import Image, ImageTk


def sign_up_window():
    # create the new window
	root = Tk()  
	root.geometry('330x560')  
	root.title('BookRecs: Sign up')

	# Load the image file
	image = Image.open("bookrecs logo.png")
	resized_image = image.resize((150, 88))
	# Create a label widget and set its image
	photo = ImageTk.PhotoImage(resized_image)

	label = Label(root, image=photo)
	label.grid(row=0,column=0, columnspan=2)
	
	nameLabel = Label(root, text="Full Name", font=("Times New Roman", 11, "bold"))
	nameLabel.grid(row=1, column=0, padx=5, pady=5)

	nameEntry = Entry(root, textvariable=nameLabel)
	nameEntry.grid(row=2, column=0, padx=5, pady=5)  
	
	ageLabel = Label(root, text="Age", font=("Times New Roman", 11, "bold"))
	ageLabel.grid(row=3, column=0, padx=5, pady=5)

	ageEntry = Entry(root, textvariable=ageLabel)
	ageEntry.grid(row=4, column=0, padx=5, pady=5)  

	emailLabel = Label(root, text="Email", font=("Times New Roman", 11, "bold"))
	emailLabel.grid(row=5, column=0, padx=5, pady=5)

	emailEntry = Entry(root, textvariable=emailLabel)
	emailEntry.grid(row=6, column=0, padx=5, pady=5)  

	#password label and password entry box
	passwordLabel = Label(root,text="Password", font=("Times New Roman", 11, "bold"))
	passwordLabel.grid(row=7, column=0, padx=5, pady=5)

	passwordEntry = Entry(root, textvariable=passwordLabel, show='*')
	passwordEntry.grid(row=8, column=0, padx=5, pady=5)  

	verify_passwordLabel = Label(root,text="Verify Password", font=("Times New Roman", 11, "bold"))
	verify_passwordLabel.grid(row=9, column=0, padx=5, pady=5)

	verify_passwordEntry = Entry(root, textvariable=passwordLabel, show='*')
	verify_passwordEntry.grid(row=10, column=0,padx=5, pady=5) 
	#validateLogin = partial(validateLogin, root, passwordLabel)

	#login button
	loginButton = Button(root, text="Log In", font=("Times New Roman", 11, "bold"),fg='white', bg="mediumseagreen") #, command=validateLogin)
	loginButton.grid(row=11, column=0 ,padx=15, pady=10)  


    # run the new window
	root.mainloop()


def login_window():
	#window
	root = Tk()  
	root.geometry('330x560')  
	root.title('BookRecs: Log in')

	# Load the image file
	image = Image.open("bookrecs logo.png")
	resized_image = image.resize((300, 166))
	# Create a label widget and set its image
	photo = ImageTk.PhotoImage(resized_image)

	label = Label(root, image=photo)
	label.grid(row=0,column=0, columnspan=2)

	# Create a label widget for the text
	text_label = Label(root, text="Log In", font=("Times New Roman", 22, "bold"))
	text_label.grid(row=1, column=0, columnspan=2, padx= 5, pady= 5)

	emailLabel = Label(root, text="Email", font=("Times New Roman", 11, "bold"))
	emailLabel.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

	emailEntry = Entry(root, textvariable=emailLabel)
	emailEntry.grid(row=3, column=0, columnspan=2, padx=5, pady=5)  

	#password label and password entry box
	passwordLabel = Label(root,text="Password", font=("Times New Roman", 11, "bold"))
	passwordLabel.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

	passwordEntry = Entry(root, textvariable=passwordLabel, show='*')
	passwordEntry.grid(row=5, column=0,columnspan=2, padx=5, pady=5)  

	#validateLogin = partial(validateLogin, root, passwordLabel)

	#login button
	loginButton = Button(root, text="Log In", font=("Times New Roman", 11, "bold"),fg='white', bg="mediumseagreen") #, command=validateLogin)
	loginButton.grid(row=6, column=0, columnspan=2 ,padx=15, pady=10)  

	forgotButton = Button(root, text="Forgot password?", font=("Times New Roman", 11), fg='blue')
	forgotButton.grid(row=7, column=0, columnspan=2) 

	noaccount_label = Label(root, text="Don't have an account?", font=("Times New Roman", 11, "bold"))
	noaccount_label.grid(row=8, column=0, columnspan=2, padx= 5, pady= 5)

	signupButton = Button(root, text="Sign up", font=("Times New Roman", 11), fg='blue', command=lambda:[root.destroy(), sign_up_window()])
	signupButton.grid(row=9, column=0, columnspan=2) 

	social_label = Label(root, text="Or use one of your social profiles", font=("Times New Roman", 11, "bold"))
	social_label.grid(row=10, column=0, columnspan=2, padx= 5, pady= 5)

	twitterButton = Button(root, text="Twitter", font=("Times New Roman", 11), fg='white', bg="deep sky blue")
	twitterButton.grid(row=11, column=0)  

	facebookButton = Button(root, text="Facebook", font=("Times New Roman", 11), fg='white', bg="navy")
	facebookButton.grid(row=11, column=1, columnspan=2) 

	root.mainloop()


login_window()