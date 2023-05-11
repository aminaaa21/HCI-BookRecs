from tkinter import *
from functools import partial
from PIL import Image, ImageTk


def home_page_window():
	# create the new window
	root = Tk()  
	root.geometry('330x560')  
	root.title('BookRecs: Home Page')

def sign_up_window():
    # create the new window
	root = Tk()  
	root.geometry('330x560')  
	root.title('BookRecs: Sign up')

	profile_image = Image.open("pfp.png")
	# Create a label widget and set its image
	profile_photo = ImageTk.PhotoImage(profile_image)
	profile_label = Label(root, image=profile_photo)
	profile_label.grid(row=0, column=0, sticky="ne")

	# Load the image file
	image = Image.open("bookrecs logo.png")
	resized_image = image.resize((150, 88))
	# Create a label widget and set its image
	photo = ImageTk.PhotoImage(resized_image)

	label = Label(root, image=photo)
	label.grid(row=0, column=0, columnspan=3, padx=20, pady=20)
	root.grid_columnconfigure(1, weight=1)
	root.grid_columnconfigure(2, weight=1)

	nameLabel = Label(root, text="Full Name", font=("Times New Roman", 11, "bold"))
	nameLabel.grid(row=1, column=0, columnspan=3, padx=5, pady=(20, 0)) 

	nameEntry = Entry(root, textvariable=nameLabel)
	nameEntry.grid(row=2, column=0, columnspan=3, padx=5, pady=5)    
	
	ageLabel = Label(root, text="Age", font=("Times New Roman", 11, "bold"))
	ageLabel.grid(row=3, column=0, columnspan=3, padx=5, pady=(20, 0))  

	ageEntry = Entry(root, textvariable=ageLabel)
	ageEntry.grid(row=4, column=0, columnspan=3, padx=5, pady=5)  

	emailLabel = Label(root, text="Email", font=("Times New Roman", 11, "bold"))
	emailLabel.grid(row=5, column=0, columnspan=3, padx=5, pady=(20, 0))  

	emailEntry = Entry(root, textvariable=emailLabel)
	emailEntry.grid(row=6, column=0, columnspan=3, padx=5, pady=5)    

	#password label and password entry box
	passwordLabel = Label(root,text="Password", font=("Times New Roman", 11, "bold"))
	passwordLabel.grid(row=7, column=0, columnspan=3, padx=5, pady=(20, 0))  

	passwordEntry = Entry(root, textvariable=passwordLabel, show='*')
	passwordEntry.grid(row=8, column=0, columnspan=3, padx=5, pady=5)   

	verify_passwordLabel = Label(root,text="Verify Password", font=("Times New Roman", 11, "bold"))
	verify_passwordLabel.grid(row=9, column=0, columnspan=3, padx=5, pady=(20, 0))  

	verify_passwordEntry = Entry(root, textvariable=verify_passwordLabel, show='*')
	verify_passwordEntry.grid(row=10, column=0, columnspan=3, padx=5, pady=5)  
	#validateLogin = partial(validateLogin, root, passwordLabel)

	#login button
	signupButton = Button(root, text="Sign Up", font=("Times New Roman", 11, "bold"),fg='white', bg="mediumseagreen", command=lambda:[root.destroy(), preference_window()]) #, command=validateLogin
	signupButton.grid(row=11, column=0, columnspan=3, padx=20, pady=20)    

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

def preference_window(): # my testing 
	#window
	root = Tk()  
	root.geometry('330x560')  
	root.title('BookRecs: preferance window')
	# profile image on the corner

	profile_image = Image.open("pfp.png")
	# Create a label widget and set its image
	profile_photo = ImageTk.PhotoImage(profile_image)
	profile_label = Label(root, image=profile_photo)
	profile_label.grid(row=0, column=0, sticky= 'nw')

	# adding the three bars on the top
	image = Image.open("three-bars-icon-28.jpg")
	resized_image = image.resize((100, 50))
	# Create a label widget and set its image
	bars = ImageTk.PhotoImage(resized_image)

	label = Label(root, image=bars)
	label.grid(row=0, column= 2, sticky = "ne" )

	
    
	#sapcer, made from empty label 
	spacer_Label = Label(root, text="                     ", font=("Times New Roman", 10, "bold"))
	spacer_Label.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky= 'nw')


	# Create a label widget for the text
	text_label = Label(root, text="Good day! What do you like to read?", font=("Times New Roman", 12, "bold"))
	text_label.grid(row=2, column=0, columnspan=2, padx= 5, pady= 5)

    # question1 label and entry box
	question1_Label = Label(root, text="Which genre do you like to read?", font=("Times New Roman", 10, "bold"))
	question1_Label.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky= 'nw')

	question1_Entry = Entry(root, textvariable=question1_Label)
	question1_Entry.grid(row=4, column=0, columnspan=4, padx=5, pady=5, sticky='nw')  

	# qusetion2 label and entry box
	question2_Label = Label(root,text="Do you have a specific topic you want to read about?", font=("Times New Roman", 10, "bold"))
	question2_Label.grid(row=5, column=0, columnspan=4, padx=5, pady=5,sticky='nw')

	question2_Entry = Entry(root, textvariable=question2_Label)
	question2_Entry.grid(row=6, column=0,columnspan=4, padx=5, pady=5, sticky= 'nw') 
	 
	# qusetion3 label and entry box
	question2_Label = Label(root,text="Do you have a specific book in mind?", font=("Times New Roman", 10, "bold"))
	question2_Label.grid(row=7, column=0, columnspan=4, padx=5, pady=5,sticky= 'nw')

	question2_Entry = Entry(root, textvariable=question2_Label)
	question2_Entry.grid(row=8, column=0,columnspan=4, padx=5, pady=5,sticky= 'nw')  
	
    #sapcer, made from empty label 
	spacer_Label = Label(root, text="                     ", font=("Times New Roman", 10, "bold"))
	spacer_Label.grid(row=9, column=0, columnspan=2, padx=5, pady=5, sticky= 'nw')

	# suggestion label
	suggest_Label = Label(root,text="Here are some suggestions,", font=("Times New Roman", 10, "bold"))
	suggest_Label.grid(row=10, column=0, columnspan=4, padx=5, pady=5,sticky='nw')
	#line = preference_window.create_line(50, 50, 200, 200, fill= 'black', width= 2)

   
    #adding the suggested book 1 
	image = Image.open("book cover 1.jpeg")
	resized_image = image.resize((70, 100))
	#Create a label widget and set its image
	photo1 = ImageTk.PhotoImage(resized_image)

	label = Label(root, image=photo1)
	label.grid(row=12,column=0)

	# adding the name of book 1
	book1_name = Label(root,text="Autism in the family", font=("Times New Roman", 9, "bold"))
	book1_name.grid(row= 17, column=0, padx=5, pady=5)

	buy_book_button = Button(root, text="Buy Book", font=("Times New Roman", 11), fg='white',bg="green", command=lambda:[root.destroy(), reading_window()])
	buy_book_button.grid(row=18, column=0, padx=4, pady= 4)

	#adding the suggested book 2
	image = Image.open("book cover 2.jpeg")
	resized_image = image.resize((70, 100))
	#Create a label widget and set its image
	photo2 = ImageTk.PhotoImage(resized_image)

	label = Label(root, image=photo2)
	label.grid(row=12,column=1, columnspan=2)

	buy_book_button = Button(root, text="Buy Book", font=("Times New Roman", 11), fg='white',bg="green")
	buy_book_button.grid(row=18, column=1, padx=4, pady= 4) 
	
	# adding the name of book 2
	book1_name = Label(root,text="                           Autism", font=("Times New Roman", 9, "bold"))
	book1_name.grid(row= 17, column=1, padx=5, pady=5)

	#adding the search icon                             #STILL NOT WORKING
	#image = Image.open("search.png")
	#resized_image = image.resize((20, 20))
	#Create a label widget and set its image
	#photo1 = ImageTk.PhotoImage(resized_image)

	#label = Label(root, image=photo1)
	#label.grid(row=24,column=0)

	#adding the heart icon                                #STILL NOT WORKING
	#image = Image.open("heart-black-shape-for-valentines.png")
	#resized_image = image.resize((20, 20))
	#Create a label widget and set its image
	#photo1 = ImageTk.PhotoImage(resized_image)

	#label = Label(root, image=photo1)
	#label.grid(row=24,column=1)

	

	# creating a white box at the bottom  
	#box = Label(root,width = 50, height = 100, bg = "white" )
	#box.grid(row=30, column=0, columnspan=5, padx=5, pady=5)

	
	root.mainloop()


def reading_window(): # my testing 
	#window
	root = Tk()  
	root.geometry('330x560')  
	root.title('BookRecs: Reading window')
	# profile image on the corner

	profile_image = Image.open("pfp.png")
	# Create a label widget and set its image
	profile_photo = ImageTk.PhotoImage(profile_image)
	profile_label = Label(root, image=profile_photo)
	profile_label.grid(row=0, column=0, sticky= 'nw')

	# adding the three bars on the top
	image = Image.open("three-bars-icon-28.jpg")
	resized_image = image.resize((100, 50))
	# Create a label widget and set its image
	bars = ImageTk.PhotoImage(resized_image)

	label = Label(root, image=bars)
	label.grid(row=0, column= 2, sticky = "ne" )

	
    


	# the name of the book
	text_label = Label(root, text="Autism in the family        ", font=("Times New Roman", 12, "bold"))
	text_label.grid(row=1, column=0, columnspan=3)

    #the name of the book
	name_Label = Label(root, text="Caring and Coping Together     ", font=("Times New Roman", 10, "bold"))
	name_Label.grid(row=2, column=0, columnspan=3)

	#adding chapter1 reading                            #STILL NOT WORKING
	image = Image.open("Bchapter1.png")
	resized_image = image.resize((200, 400))
	#Create a label widget and set its image
	photo1 = ImageTk.PhotoImage(resized_image)

	label = Label(root, image=photo1)
	label.grid(row=24,column=1)

	#creating the comment button 
	
	commentButton = Button(root, text="comment", font=("Times New Roman", 11), fg='white', bg="dark green", command=lambda:[root.destroy(), comment_window()])
	commentButton.grid(row=27, column=0, columnspan=2)  

	libraryButton = Button(root, text="library", font=("Times New Roman", 11), fg='white', bg="dark green")
	libraryButton.grid(row=27, column=1, columnspan=2) 
	

	# creating a white box at the bottom  
	#box = Label(root,width = 50, height = 100, bg = "white" )
	#box.grid(row=30, column=0, columnspan=5, padx=5, pady=5)

	
	root.mainloop()

def comment_window(): # my testing
	#window
	root = Tk()  
	root.geometry('330x560')  
	root.title('BookRecs: Comments window')
	# profile image on the corner

	profile_image = Image.open("pfp.png")
	# Create a label widget and set its image
	profile_photo = ImageTk.PhotoImage(profile_image)
	profile_label = Label(root, image=profile_photo)
	profile_label.grid(row=0, column=0, sticky= 'nw')

	# adding the three bars on the top
	image = Image.open("three-bars-icon-28.jpg")
	resized_image = image.resize((100, 50))
	# Create a label widget and set its image
	bars = ImageTk.PhotoImage(resized_image)

	label = Label(root, image=bars)
	label.grid(row=0, column= 2, sticky = "ne" )

	
    


	# the name of the book
	text_label = Label(root, text="Autism in the family        ", font=("Times New Roman", 12, "bold"))
	text_label.grid(row=1, column=0, columnspan=3)

    #the name of the book
	name_Label = Label(root, text="Caring and Coping Together     ", font=("Times New Roman", 10, "bold"))
	name_Label.grid(row=2, column=0, columnspan=3)

	#adding chapter1 reading                            #STILL NOT WORKING
	image = Image.open("comment section example.png")
	resized_image = image.resize((200, 400))
	#Create a label widget and set its image
	photo1 = ImageTk.PhotoImage(resized_image)

	label = Label(root, image=photo1)
	label.grid(row=24,column=1)

	#creating the comment button 
	
	profileButton = Button(root, text="profile", font=("Times New Roman", 11), fg='white', bg="dark green", command=lambda:[root.destroy(), profile_window()])
	profileButton.grid(row=27, column=0, columnspan=2)  

	libraryButton = Button(root, text="library", font=("Times New Roman", 11), fg='white', bg="dark green")
	libraryButton.grid(row=27, column=1, columnspan=2) 
	

	# creating a white box at the bottom  
	#box = Label(root,width = 50, height = 100, bg = "white" )
	#box.grid(row=30, column=0, columnspan=5, padx=5, pady=5)

	
	root.mainloop()

def profile_window():
	#window
	root = Tk()  
	root.geometry('330x560')  
	root.title('BookRecs: profile window')

	# Load the image file
	image = Image.open("pfp.png")
	resized_image = image.resize((100, 100))
	# Create a label widget and set its image
	photo = ImageTk.PhotoImage(resized_image)

	label = Label(root, image=photo)
	label.grid(row=2,column=0, columnspan=5)

	# Create a label widget for the name, points earned and total points
	text_label = Label(root, text="Steve Johnson", font=("Times New Roman", 22, "bold"))
	text_label.grid(row=3, column=0, columnspan=5)

	pointsLabel = Label(root, text="Points earned = 30", font=("Times New Roman", 11, "bold"))
	pointsLabel.grid(row=4, column=0, columnspan=5)

	totalpointsLabel = Label(root, text=" Total points = 60", font=("Times New Roman", 11, "bold"))
	totalpointsLabel.grid(row=5, column=0, columnspan=5)



	# The Quiz section -> 
	Quiz_Label = Label(root, text="Quiz", font=("Times New Roman", 13, "bold"))
	Quiz_Label.grid(row=6, column=0, columnspan=5,padx =5, pady= 5, sticky= "nw")
	quiz_Label = Label(root, text="Earn points to buy your next book?", font=("Times New Roman", 10, "bold"))
	quiz_Label.grid(row=7, column=0, columnspan=5, padx= 5, pady= 5,sticky= "nw")


	# question1 label and entry box
	question1_Label = Label(root, text="What is the name of the right side of the brain?", font=("Times New Roman", 10, "bold"))
	question1_Label.grid(row=8, column=0, columnspan=2, padx=5, pady=5, sticky= 'nw')

	question1_Entry = Entry(root, textvariable=question1_Label)
	question1_Entry.grid(row=9, column=0, columnspan=4, padx=5, pady=5, sticky='nw')  

	# qusetion2 label and entry box
	question2_Label = Label(root,text="How to deal with an autistic child?", font=("Times New Roman", 10, "bold"))
	question2_Label.grid(row=10, column=0, columnspan=4, padx=5, pady=5,sticky='nw')

	question2_Entry = Entry(root, textvariable=question2_Label)
	question2_Entry.grid(row=11, column=0,columnspan=4, padx=5, pady=5, sticky= 'nw') 
	 
	# qusetion3 label and entry box
	question2_Label = Label(root,text="What did the author major in?", font=("Times New Roman", 10, "bold"))
	question2_Label.grid(row=12, column=0, columnspan=4, padx=5, pady=5,sticky= 'nw')

	question2_Entry = Entry(root, textvariable=question2_Label)
	question2_Entry.grid(row=13, column=0,columnspan=4, padx=5, pady=5,sticky= 'nw')  

	#spacer, could not do an actual space ,,, MAYBE IF WE CAN FIX
	#question1_Label = Label(root, text="                     ", font=("Times New Roman", 10, "bold"))
	#question1_Label.grid(row=14, column=0, columnspan=2, padx=5, pady=5, sticky= 'nw')

	# submit button
	log_out_Button = Button(root, text="        Submit          ", font=("Times New Roman", 11), fg='white', bg="navy blue")
	log_out_Button.grid(row=15, column=0, columnspan=4)

	#spacer, jsut a test
	question1_Label = Label(root, text="                     ", font=("Times New Roman", 10, "bold"))
	question1_Label.grid(row=16, column=0, columnspan=2, padx=5, pady=5, sticky= 'nw')


	# log out and books
	log_out_Button = Button(root, text="Log out", font=("Times New Roman", 11), fg='white', bg="dark green", command=lambda:[root.destroy(), login_window()])
	log_out_Button.grid(row=17, column=0, columnspan=5, padx = 15, pady = 20)  

	# THIS ONE NOT SURE ABOUT, I can't seem to figure out the spacing on it :/
	#my_books_Button = Button(root, text="My Books", font=("Times New Roman", 11), fg='white', bg="dark green",command=lambda:[root.destroy(), reading_window()])
	#my_books_Button.grid(row=17, column=1, columnspan=2, padx= 15, pady = 20) 
	
	

	root.mainloop()
 
	

	


login_window()