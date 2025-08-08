import pandas as pd
import smtplib
from email.message import EmailMessage

# === Configuration ===
EXCEL_FILE_PATH = 'ton_fichier.xlsx'  # Mets ici le chemin de ton fichier
EMAIL_SENDER = 'ton.email@example.com'
EMAIL_PASSWORD = 'ton_mot_de_passe_ou_mot_de_passe_app'
EMAIL_RECEIVER = 'destinataire@example.com'
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

def excel_has_data(filepath):
    try:
        xl = pd.ExcelFile(filepath)
        for sheet in xl.sheet_names:
            df = xl.parse(sheet)
            if not df.empty:
                return True
        return False
    except Exception as e:
        print(f"Erreur de lecture Excel : {e}")
        return False

def send_email():
    msg = EmailMessage()
    msg['Subject'] = 'Fichier Excel non vide'
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECEIVER
    msg.set_content("Le fichier Excel contient des données.")

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
            smtp.starttls()
            smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
            smtp.send_message(msg)
            print("Email envoyé.")
    except Exception as e:
        print(f"Erreur envoi mail : {e}")

# === Exécution principale ===
if excel_has_data(EXCEL_FILE_PATH):
    send_email()
else:
    print("Fichier vide – aucun mail envoyé.")
