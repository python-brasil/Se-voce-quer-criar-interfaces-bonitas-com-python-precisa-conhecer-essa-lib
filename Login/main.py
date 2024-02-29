from customtkinter import *
from PIL import Image

app = CTk()
app.geometry("600x480")
app.title('Python Brasil Gestão de estoque')
app.resizable(0,0)

side_img_data = Image.open("side-img.png")
email_icon_data = Image.open("email-icon.png")
password_icon_data = Image.open("password-icon.png")
google_icon_data = Image.open("google-icon.png")

side_img = CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(300, 480))
email_icon = CTkImage(dark_image=email_icon_data, light_image=email_icon_data, size=(20,20))
password_icon = CTkImage(dark_image=password_icon_data, light_image=password_icon_data, size=(17,17))
google_icon = CTkImage(dark_image=google_icon_data, light_image=google_icon_data, size=(17,17))

CTkLabel(master=app, text="", image=side_img).pack(expand=True, side="left")

frame = CTkFrame(master=app, width=300, height=480, fg_color="#ffffff")
frame.pack_propagate(0)
frame.pack(expand=True, side="right")

CTkLabel(master=frame, text="Seja Bem Vindo!", text_color="#387eb8", anchor="w", justify="left", font=("Arial Bold", 24)).pack(anchor="w", pady=(50, 5), padx=(25, 0))
CTkLabel(master=frame, text="Entre com sua conta", text_color="#7E7E7E", anchor="w", justify="left", font=("Arial Bold", 12)).pack(anchor="w", padx=(25, 0))

CTkLabel(master=frame, text="  Email:", text_color="#387eb8", anchor="w", justify="left", font=("Arial Bold", 14), image=email_icon, compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))
CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#387eb8", border_width=1, text_color="#000000").pack(anchor="w", padx=(25, 0))

CTkLabel(master=frame, text="  Password:", text_color="#387eb8", anchor="w", justify="left", font=("Arial Bold", 14), image=password_icon, compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 0))
CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#387eb8", border_width=1, text_color="#000000", show="*").pack(anchor="w", padx=(25, 0))

CTkButton(master=frame, text="Login", fg_color="#387eb8", hover_color="#235176", font=("Arial Bold", 12), text_color="#ffffff", width=225).pack(anchor="w", pady=(40, 0), padx=(25, 0))
CTkButton(master=frame, text="Continue With Google", fg_color="#EEEEEE", hover_color="#EEEEEE", font=("Arial Bold", 9), text_color="#387eb8", width=225, image=google_icon).pack(anchor="w", pady=(20, 0), padx=(25, 0))


app.mainloop()