#!/usr/bin/python3
import random

secintro = ["News:", "Breaking:", "Breaking News:", "ABSOLUTELY INCREDIBLE:", "News:", "Breaking:", "Breakings News:"]
sec0point5 = ["Nude", "Drunk", "Sexy smexy", "Dope", "Missing", "Local", "Gross", "Heroic", "Feminine", "Extremely buff", "Fat", "Dumb", "Intellectual"]
sec1 = ["Soyboy", "Gym instructor", "Smartphone reseller", "Ministry of Foreign affairs", "Ministry of Defense", "Organization", "Movie Maker", "CEO", "Pre schooler", "Florida Man", "Florida woman", "Elementary school teacher", "President Obama", "Reddit fag", "Bill Gates", "Capitan", "Femboy", "Vladimir, son of Vladimir", "Police Officer", "Tomboy", "Scientist", "Jeffery Epstein", "Brazilian", "Parent"]
sec2 = ["sold to", "slips on", "believed to be", "identified by", "*****", "yanks", "rips apart", "internationalizes", "destroys", "goes to", "sucks", "entertains", "gives meth to his", "goes off at", "falls off", "radicalizes", "finds", "hits", "eats", "cooks", "discovers", "abuses", "destabilizes"]
sec2point5 = ["tasty", "cute", "destructive", "colonized", "fucked up", "big", "beutiful", "manly", "famous", "seducive", "cucked", "astonishing", "faulty"]
sec3 = ["homicide victim", "wife", "toy", "bakery", "sand castle", "e-scooter", "soy farm", "chicken tendies", "bitcoin mine", "shithole", "tank", "southerner", "pre schooler", "lobster", "mac 'n cheese", "building", "plate", "skeleton"]
secmark = [".", "...", "!", "??!"]
secses = ["Gone wrong!", "Gone sexual!", "0/10 wouldn't recommend.", "Try it out yourself today."]

if random.randint(0,2)==1: print(secintro[random.randint(0,len(secintro)-1)], end=" ")
if random.randint(0,4)==1: print(sec0point5[random.randint(0,len(sec0point5)-1)], end=" ")
print(sec1[random.randint(0, len(sec1)-1)], end=" ")
print(sec2[random.randint(0, len(sec2)-1)], end=" ")
if random.randint(0,1)==1: print(sec2point5[random.randint(0,len(sec2point5)-1)], end=" ")
print(sec3[random.randint(0, len(sec3)-1)] + secmark[random.randint(0, len(secmark)-1)], end=" ")
if random.randint(0,2)==1: print(secses[random.randint(0, len(secses)-1)])
else: print()
