#Βιβλιοθηκη
from tkinter import *
#Συναρτηση
def toCelsius():
    fahrenheit = float(temperature.get())
    celsius = round((fahrenheit - 32) * 5.0/9.0 ,2)
    result["text"] = f"Οι {fahrenheit} βαθμοι Φαραναιτ ειναι{celsius} βαθμοι κελσιου"

def toFahrreinheit():
    celsius = float(temperature.get())
    fahrenheit = round(9.0/5.0 *celsius + 32 ,2)
    result["text"] = f"Οι {celsius} βαθμοι κελσιου ειναι {fahrenheit} βαθμοι Φαραναιτ "

#Δημηιουργια Παραθυρου window = root
root = Tk()
root.title("Γιωργος Dev")
root.geometry("1280x720")
#Δημιουργια Κειμενου
label = Label(root, text="Μετατροπη σε μοναδες Celsius/Fahrenheit")
label.pack()

#Δημιουργια εισαγωγης θερμοκρασιας

temperature=Entry(root)
temperature.pack()
#Αποτελεσμα συναρτησης
result = Label(text="")
result.pack()

#Τα κουμπια για ενεργοποιηση προγραμματος

btn1 = Button(root, text ="Μετατροπη σε βαλθμους Κελσιου", command=toCelsius)
btn2 = Button(root, text="Μετατροπη σε βαθμους Φαραναιτ", command=toFahrreinheit )
btn1.pack()
btn2.pack()

#Ο τροπος για να μενει το παραθυρο σταθερα ανοιχτο
root.mainloop()