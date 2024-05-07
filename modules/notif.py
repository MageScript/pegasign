from plyer import notification


def notify(title, message):
    icon = "media/pegasign.ico"
    notification.notify(
        title = title,
        message = message,
        app_icon = icon,
        timeout = 10 
    )
