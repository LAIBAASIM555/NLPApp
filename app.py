from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import API

class NLPApp:

    def __init__(self):
        # Create db object
        self.dbo = Database()
        self.apio = API()

        # Root window configuration
        self.root = Tk()
        self.root.title('NLPApp')
        self.root.iconbitmap('favicon.ico')
        self.root.geometry('400x650')
        self.root.configure(bg='#E1DFF7')

        self.login_gui()

        self.root.mainloop()

    def login_gui(self):
        self.clear()

        # App heading
        heading = Label(self.root, text='🔍 NLPApp', bg='#E1DFF7', fg='#6A5ACD')
        heading.pack(pady=(30, 20))
        heading.configure(font=('Helvetica', 28, 'bold'))

        # Email input
        label1 = Label(self.root, text='📧 Enter Email', bg='#E1DFF7', fg='#333333')
        label1.pack(pady=(10, 5))
        label1.configure(font=('Helvetica', 12, 'bold'))

        self.email_input = Entry(self.root, width=40, font=('Helvetica', 12), bg='#F0F0F0', relief='flat')
        self.email_input.pack(pady=(5, 10), ipady=5)

        # Password input
        label2 = Label(self.root, text='🔒 Enter Password', bg='#E1DFF7', fg='#333333')
        label2.pack(pady=(10, 5))
        label2.configure(font=('Helvetica', 12, 'bold'))

        self.password_input = Entry(self.root, width=40, font=('Helvetica', 12), bg='#F0F0F0', show='*', relief='flat')
        self.password_input.pack(pady=(5, 10), ipady=5)

        # Login button
        login_btn = Button(self.root, text='Login', width=20, height=2, command=self.perform_login, bg='#6A5ACD', fg='white', relief='flat')
        login_btn.pack(pady=(20, 10))
        login_btn.configure(font=('Helvetica', 12, 'bold'))

        # Register redirect
        label3 = Label(self.root, text='Not a member?', bg='#E1DFF7', fg='#333333')
        label3.pack(pady=(20, 5))

        redirect_btn = Button(self.root, text='Register Now', command=self.register_gui, bg='#A9A9F5', fg='#6A5ACD', relief='flat')
        redirect_btn.pack(pady=(5, 10))
        redirect_btn.configure(font=('Helvetica', 12))

    def register_gui(self):
        self.clear()

        # App heading
        heading = Label(self.root, text='🔍 NLPApp', bg='#E1DFF7', fg='#6A5ACD')
        heading.pack(pady=(30, 20))
        heading.configure(font=('Helvetica', 28, 'bold'))

        # Name input
        label0 = Label(self.root, text='👤 Enter Name', bg='#E1DFF7', fg='#333333')
        label0.pack(pady=(10, 5))
        label0.configure(font=('Helvetica', 12, 'bold'))

        self.name_input = Entry(self.root, width=40, font=('Helvetica', 12), bg='#F0F0F0', relief='flat')
        self.name_input.pack(pady=(5, 10), ipady=5)

        # Email input
        label1 = Label(self.root, text='📧 Enter Email', bg='#E1DFF7', fg='#333333')
        label1.pack(pady=(10, 5))
        label1.configure(font=('Helvetica', 12, 'bold'))

        self.email_input = Entry(self.root, width=40, font=('Helvetica', 12), bg='#F0F0F0', relief='flat')
        self.email_input.pack(pady=(5, 10), ipady=5)

        # Password input
        label2 = Label(self.root, text='🔒 Enter Password', bg='#E1DFF7', fg='#333333')
        label2.pack(pady=(10, 5))
        label2.configure(font=('Helvetica', 12, 'bold'))

        self.password_input = Entry(self.root, width=40, font=('Helvetica', 12), bg='#F0F0F0', show='*', relief='flat')
        self.password_input.pack(pady=(5, 10), ipady=5)

        # Register button
        register_btn = Button(self.root, text='Register', width=20, height=2, command=self.perform_registration, bg='#6A5ACD', fg='white', relief='flat')
        register_btn.pack(pady=(20, 10))
        register_btn.configure(font=('Helvetica', 12, 'bold'))

        # Login redirect
        label3 = Label(self.root, text='Already a member?', bg='#E1DFF7', fg='#333333')
        label3.pack(pady=(20, 5))

        redirect_btn = Button(self.root, text='Login Now', command=self.login_gui, bg='#A9A9F5', fg='#6A5ACD', relief='flat')
        redirect_btn.pack(pady=(5, 10))
        redirect_btn.configure(font=('Helvetica', 12))

    def clear(self):
        for widget in self.root.pack_slaves():
            widget.destroy()

    def perform_registration(self):
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.add_data(name, email, password)

        if response:
            messagebox.showinfo('Success', 'Registration successful. You can login now')
        else:
            messagebox.showerror('Error', 'Email already exists')

    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.search(email, password)

        if response:
            messagebox.showinfo('Success', 'Login successful')
            self.home_gui()
        else:
            messagebox.showerror('Error', 'Incorrect email/password')

    def home_gui(self):
        self.clear()

        # App heading
        heading = Label(self.root, text='🔍 NLPApp', bg='#6A5ACD', fg='white')
        heading.pack(pady=(30, 20))
        heading.configure(font=('Helvetica', 28, 'bold'))

        # Feature buttons
        sentiment_btn = Button(self.root, text='😊 Sentiment Analysis', width=30, height=2, command=self.sentiment_gui, bg='#A9A9F5', fg='#6A5ACD', relief='flat')
        sentiment_btn.pack(pady=(10, 10))

        ner_btn = Button(self.root, text='📝 Named Entity Recognition', width=30, height=2, command=self.ner_gui, bg='#A9A9F5', fg='#6A5ACD', relief='flat')
        ner_btn.pack(pady=(10, 10))

        emotion_btn = Button(self.root, text='❤️ Emotion Prediction', width=30, height=2, command=self.emotion_gui, bg='#A9A9F5', fg='#6A5ACD', relief='flat')
        emotion_btn.pack(pady=(10, 10))

        # Logout button
        logout_btn = Button(self.root, text='🔓 Logout', command=self.login_gui, bg='#DCDCDC', fg='#6A5ACD', relief='flat')
        logout_btn.pack(pady=(20, 10))

    def sentiment_gui(self):
        self.clear()

        # Sentiment Analysis Heading
        heading = Label(self.root, text='🔍 NLPApp', bg='#6A5ACD', fg='white')
        heading.pack(pady=(30, 20))
        heading.configure(font=('Helvetica', 28, 'bold'))

        heading2 = Label(self.root, text='😊 Sentiment Analysis', bg='#E1DFF7', fg='#333333')
        heading2.pack(pady=(10, 10))
        heading2.configure(font=('Helvetica', 18))

        # Text Input for Analysis
        label1 = Label(self.root, text='Enter the text', bg='#E1DFF7', fg='#333333')
        label1.pack(pady=(10, 5))

        self.sentiment_input = Entry(self.root, width=50, font=('Helvetica', 12), bg='#F0F0F0', relief='flat')
        self.sentiment_input.pack(pady=(5, 10), ipady=5)

        # Analyze Button
        sentiment_btn = Button(self.root, text='Analyze Sentiment', command=self.do_sentiment_analysis, bg='#6A5ACD', fg='white', relief='flat')
        sentiment_btn.pack(pady=(10, 10))

        # Result Label
        self.sentiment_result = Label(self.root, text='', bg='#E1DFF7', fg='#333333')
        self.sentiment_result.pack(pady=(20, 10))

    def do_sentiment_analysis(self):
        text = self.sentiment_input.get()
        sentiment = self.apio.get_sentiment(text)  # Implement this method in your API class

        self.sentiment_result.config(text=f'Sentiment: {sentiment}')

    def ner_gui(self):
        self.clear()

        # NER Heading
        heading = Label(self.root, text='🔍 NLPApp', bg='#6A5ACD', fg='white')
        heading.pack(pady=(30, 20))
        heading.configure(font=('Helvetica', 28, 'bold'))

        heading2 = Label(self.root, text='📝 Named Entity Recognition', bg='#E1DFF7', fg='#333333')
        heading2.pack(pady=(10, 10))
        heading2.configure(font=('Helvetica', 18))

        # Text Input for NER
        label1 = Label(self.root, text='Enter the text for NER', bg='#E1DFF7', fg='#333333')
        label1.pack(pady=(10, 5))

        self.ner_input = Entry(self.root, width=50, font=('Helvetica', 12), bg='#F0F0F0', relief='flat')
        self.ner_input.pack(pady=(5, 10), ipady=5)

        # Analyze Button
        ner_btn = Button(self.root, text='Perform NER', command=self.do_ner_detection, bg='#6A5ACD', fg='white', relief='flat')
        ner_btn.pack(pady=(10, 10))

        # Result Label
        self.ner_result = Label(self.root, text='', bg='#E1DFF7', fg='#333333')
        self.ner_result.pack(pady=(20, 10))

    def do_ner_detection(self):
        text = self.ner_input.get()
        entities = self.apio.get_entities(text)  # Implement this method in your API class

        self.ner_result.config(text=f'Entities: {entities}')

    def emotion_gui(self):
        self.clear()

        # Emotion Detection Heading
        heading = Label(self.root, text='🔍 NLPApp', bg='#6A5ACD', fg='white')
        heading.pack(pady=(30, 20))
        heading.configure(font=('Helvetica', 28, 'bold'))

        heading2 = Label(self.root, text='❤️ Emotion Prediction', bg='#E1DFF7', fg='#333333')
        heading2.pack(pady=(10, 10))
        heading2.configure(font=('Helvetica', 18))

        # Text Input for Emotion Detection
        label1 = Label(self.root, text='Enter the text for Emotion Detection', bg='#E1DFF7', fg='#333333')
        label1.pack(pady=(10, 5))

        self.emotion_input = Entry(self.root, width=50, font=('Helvetica', 12), bg='#F0F0F0', relief='flat')
        self.emotion_input.pack(pady=(5, 10), ipady=5)

        # Analyze Button
        emotion_btn = Button(self.root, text='Detect Emotion', command=self.do_emotion_detection, bg='#6A5ACD', fg='white', relief='flat')
        emotion_btn.pack(pady=(10, 10))

        # Result Label
        self.emotion_result = Label(self.root, text='', bg='#E1DFF7', fg='#333333')
        self.emotion_result.pack(pady=(20, 10))

    def do_emotion_detection(self):
        text = self.emotion_input.get()
        emotions = self.apio.get_emotions(text)  # Implement this method in your API class

        self.emotion_result.config(text=f'Emotions: {emotions}')

if __name__ == '__main__':
    app = NLPApp()
