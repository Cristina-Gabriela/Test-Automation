# import notification as notification
# from gi.repository import Notify
# Notify.init("App Name")
# Notify.Notification.new("Hi").show()
# Notify.uninit()
# notification.close()
# 
# Notify.init("Test App")
# 
# notification = Notify.Notification.new("Hi")
# 
# notification.set_urgency(0)
# notification.set_urgency(1)
# notification.set_urgency(2) # Highest priority
# 
# notification.show()

# from gi.repository import Notify
# Notify.init("Test Notifier")
# Notify.Notification.new("Hello !").show()

# import os
# os.system("Notify-send message")
#
# import subprocess
# subprocess.call(["notify-send","https://www.youtube.com/watch?v=USJWDS83Eec"])
#

from plyer import notification

title = "Hello Amazing people!"

message = "Thanks for reading ! Take care !"
notification.notify(title=title,
                    message=message,
                    app_icon=None,
                    timeout=50,
                    toast=False)
