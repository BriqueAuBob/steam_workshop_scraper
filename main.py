from Steam.User import User
from Steam.WorkshopItems import WorkshopItems

name = input("Steam profile URL? (only the name)")
url = name

user = User(name)
print(user.getUsername(), "\n", user.getSummary())

workshop = WorkshopItems(name)
items = workshop.getWorkshopItems()

print(items)