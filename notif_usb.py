import subprocess
import sys
import shlex

def envoyer_notification(titre, message, tag="python_notif"):
    titre_echap = shlex.quote(titre)
    message_echap = shlex.quote(message)
    tag_echap = shlex.quote(tag)

    cmd = [
        "adb", "shell", "cmd", "notification", "post",
        "-S", "bigtext",
        "-t", titre_echap,
        tag_echap,
        message_echap,
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)

def main():
    print("notification")
    titre = input("Titre: ").strip()
    message = input("Contenu: ").strip()

    envoyer_notification(titre, message)

if __name__ == "__main__":
    main()
