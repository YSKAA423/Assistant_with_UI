import tkinter
import customtkinter as ctk
import speech_recognition as sr
import requests as r
import threading
from PIL import Image
import pyttsx3

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.after(201, lambda :app.iconbitmap(r"C:\Users\yasee\OneDrive\Desktop\pythonProject\Assets\voice.ico"))
app.title("Voice Assistant")
app.geometry("500x300")

conversation_history = []


def listen_in_background():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio_data = recognizer.listen(source)

    try:
        text = recognizer.recognize_sphinx(audio_data)
        update_conversation(f"User: {text}")
        send_command_to_flask(text)
    except sr.UnknownValueError:
        print("Pardon me, I did not understand what you said.")
    except sr.RequestError as e:
        print(f"Error: {e}")


def update_conversation(new_line):
    global conversation_history
    conversation_history.append(new_line)
    full_conversation = "\n".join(conversation_history)
    print(full_conversation)  # Debug print statement
    Conversation_textbox.configure(state='normal')  # Enable editing
    Conversation_textbox.delete("1.0", tkinter.END)  # Clear the textbox
    Conversation_textbox.insert(tkinter.END, full_conversation)  # Insert updated conversation
    Conversation_textbox.configure(state='disabled')  # Disable editing



def send_command_to_flask(text):
    try:

        response = r.post('http://127.0.0.1:5000/process_text', json={'command': text})
        response_data = response.json()

        if response:
            status = '<....>'
            update_status(status)
            update_conversation(f"Assistant: {response_data['response']}")
            play_audio_response(response_data['response'])
            status = 'Standby'
            update_status(status)
        else:
            status = 'Standby'
            update_status(status)




    except Exception as e:
        print(f"error: {e}")


def play_audio_response(response_text):
    engine = pyttsx3.init()
    engine.say(response_text)
    engine.runAndWait()


def update_status(status):
    Status_label.configure(text=status)


def delete_conversation_history():
    global conversation_history
    conversation_history = []
    Conversation_textbox.configure(state='normal')  # Enable editing
    Conversation_textbox.delete("1.0", tkinter.END)  # Clear the textbox
    Conversation_textbox.configure(state='disabled')  # Disable editing


def submit_text():
    text = textbox.get("1.0", "end-1c")
    print(f"Submitted Text: {text}")
    update_conversation(f"User: {text}")
    send_command_to_flask(text)

def download_csv():
    try:
        response = r.get('http://127.0.0.1:5000/download_csv')
        with open('interactions.csv', 'wb') as f:
            f.write(response.content)
        print("CSV downloaded successfully.")
    except Exception as e:
        print(f"Error downloading CSV: {e}")

def start_listening():
    threading.Thread(target=listen_in_background).start()


tabview = ctk.CTkTabview(master=app, width=500, height=700)
tabview.pack(padx=20, pady=20)

tabview.add("Assistant")
tabview.add("Stats")

tabview.set("Assistant")


mic_image = ctk.CTkImage(light_image=Image.open(r"C:\Users\yasee\OneDrive\Desktop\pythonProject\Assets\MIC.png"), size=(15, 15))
speak_button = ctk.CTkButton(tabview.tab("Assistant"),
                       text='',
                       width=50,
                       height=50,
                       corner_radius=100000,
                       hover_color='green',
                       command=start_listening,
                       image=mic_image)
speak_button.place(relx=0.8999, rely=0.5, anchor=tkinter.CENTER)

textbox = ctk.CTkTextbox(master=tabview.tab('Assistant'),
                         width=350,
                         height=60,
                         wrap='word',
                         activate_scrollbars=True)

textbox.place(relx=0.4, rely=0.92, anchor=tkinter.CENTER)
# textbox.insert("0.0", "Type here instead")


submit_button = ctk.CTkButton(tabview.tab("Assistant"),
                              text='Submit',
                              height=30,
                              width=70,
                              command=submit_text)

submit_button.place(relx=0.9, rely=0.8, anchor=tkinter.CENTER)

reset_button = ctk.CTkButton(tabview.tab("Assistant"),
                             text='Reset',
                             height=10,
                             width=10,
                             command=delete_conversation_history)

reset_button.place(relx=0.9, rely=0.95, anchor=tkinter.CENTER)

download_image = ctk.CTkImage(light_image=Image.open(r"C:\Users\yasee\OneDrive\Desktop\pythonProject\Assets\download.icns"), size=(15, 15))
Download_button = ctk.CTkButton(tabview.tab("Assistant"),
                                text='Chats',
                                fg_color='gray',
                                height=5,
                                width=5,
                                corner_radius= 10000,
                                command=download_csv,
                                image=download_image)

Download_button.place(relx=0.9, rely=0.07, anchor=tkinter.CENTER)




Status_label = ctk.CTkLabel(master=tabview.tab('Assistant'),
                            text="Standby",
                            width=30,
                            height=30,
                            text_color='black',
                            fg_color='green',
                            corner_radius=30)

Status_label.place(relx=0.9, rely=0.25, anchor=tkinter.CENTER)



Conversation_textbox = ctk.CTkTextbox(master=tabview.tab('Assistant'),
                                      width=350,
                                      height=150,
                                      fg_color='grey',
                                      corner_radius=40,
                                      activate_scrollbars=True,
                                      )

Conversation_textbox.configure(state='disabled')
Conversation_textbox.place(relx=0.4, rely=0.38, anchor=tkinter.CENTER)
Conversation_textbox.tag_add('left', 1.0, 'end')

app.mainloop()
