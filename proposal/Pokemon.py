class Person:
  def __init__(mon, name, type1, type2, health, atk, defence, spc, sdef, spd):
    
    mon.type = type1, type2
    mon.name = name
    mon.health = health
    mon.atk = atk
    mon.defence = defence
    mon.spc = spc
    mon.sdef = sdef
    mon.spd = spd
    mon.all = name, type1, type2, health, atk, defence, spc, sdef, spd

  def printtype(mon):
    print(mon.type)



alcremie = Person("Alcremie", "fairy","none", 100, 90, 150, 120, 110, 200)
carvine = Person("Carvine","grass", "none", "200", 180, 150,203, 100, 150)
print(alcremie.all)
