from django.contrib.auth.models import User
from adventure.models import Player, Room
import csv

# Room.objects.all().delete()

# def RoomMaker():
#   with open('names.csv', 'r') as room_names:
#     names = csv.DictReader(room_names)
#     for row in names:
#       room = Room(row)
#       room.save()

# RoomMaker()

rooms = open("names.txt", "r")
room_names = rooms.read().split("\n")
descriptions = open("descriptions.txt", "r")
room_descriptions = descriptions.read().split("\n")

list = []
dict = {}

# for room_name in room_names:
#   room = Room(title=room_name)
#   room.save()

for name in room_names:
  dict[name] = Room(title=name, description="A generic room")

for room in dict:
  list.append(dict[room])

for i in range(len(list)):
  list[i].save()

for i in range(len(list) - 1):
  list[i].connectRooms(list[i + 1], "n")

for i in range(len(list)):
  list[i].connectRooms(list[i - 1], "s")

r_outside = Room(title="Outside Cave Entrance", description="North of you, the cave mount beckons")

r_foyer = Room(title="Foyer", description="""Dim light filters in from the south. Dusty
passages run north and east.""")

r_overlook = Room(title="Grand Overlook", description="""A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""")

r_narrow = Room(title="Narrow Passage", description="""The narrow passage bends here from west
to north. The smell of gold permeates the air.""")

r_treasure = Room(title="Treasure Chamber", description="""You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")

r_outside.save()
r_foyer.save()
r_overlook.save()
r_narrow.save()
r_treasure.save()

# Link rooms together
r_outside.connectRooms(r_foyer, "n")
r_foyer.connectRooms(r_outside, "s")

r_foyer.connectRooms(r_overlook, "n")
r_overlook.connectRooms(r_foyer, "s")

r_foyer.connectRooms(r_narrow, "e")
r_narrow.connectRooms(r_foyer, "w")

r_narrow.connectRooms(r_treasure, "n")
r_treasure.connectRooms(r_narrow, "s")

players=Player.objects.all()
for p in players:
  p.currentRoom=r_outside.id
  p.save()

