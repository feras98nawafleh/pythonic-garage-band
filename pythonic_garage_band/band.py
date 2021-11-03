# from abc import ABC, abstractmethod

# class Musician:
#     def __init__(self, name):
#         self.name = name
#     def __str__(self):
#       return self.name

#     def __repr__(self):
#       return self.name

# class Band(Musician):
#   instanceMembers = [] 
#   def __init__(self, name, member):
#     self.name = name
#     self.member = member
#     self.instanceMembers.append(self)

#   def play_solos(self):
#     solos = [i.play_solo() for i in self.members]
#     return solos
  
#   def __str__(self):
#     return self.name

#   def __repr__(self):
#     return self.name

#   @classmethod
#   def to_list(cls):
#       bands = [i.name for i in cls.instanceMembers]
#       return bands
  
#   @abstractmethod
#   def get_instrument(self):
#     pass

# class Guitarist(Musician):
#   def get_instrument(self):
#     return "guitar"

#   def __init__(self, name):
#       super().__init__(name)

#   def __str__(self):
#       return f"My name is {self.name} and I play guitar"

#   def __repr__(self):
#     return f"Guitarist instance. Name = {self.name}"
  
#   def play_solo():
#     return "face melting guitar solo"

# class Drummer(Musician):
#     def get_instrument(self):
#       return "drums"

#     def __str__(self):
#       return f"My name is {self.name} and I play drums"

#     def __repr__(self):
#       return f"Drummer instance. Name = {self.name}"
    
#     def play_solo():
#       return "rattle boom crash"

# class Bassist(Musician):
#     def get_instrument(self):
#       return "bass"

#     def __str__(self):
#       return f"My name is {self.name} and I play bass"
    
#     def __repr__(self):
#       return f"Bassist instance. Name = {self.name}"

#     def play_solo():
#       return "bom bom buh bom"
    
  
from abc import abstractmethod


class Musician:
    def __init__(self, name):
        self.name = name

    def __repr__(self): 
        return "| %s |" % self.name  

    def __str__(self):
        return "| %s |" % self.name
        
class Band(Musician):
    instances = []
    
    def __init__(self, name, members):
        self.name = name
        self.members = members
        self.instances.append(self)

    def play_solos(self):
        solo = [i.play_solo() for i in self.members]
        return solo

    def __str__(self):
        return '%s' % self.name

    def __repr__(self):
        return '%s' % self.name

    @classmethod
    def to_list(cls):
        bands = [i.name for i in cls.instances]
        return bands
    
    @classmethod
    def to_list(cls):
        return cls.instances

    def __repr__(self):
        return "| %s |" % self.name

    def __str__(self):
        return "| %s |" % self.name               


class Guitarist(Musician):
    def __str__(self):
        return "My name is %s and I play guitar" % self.name
    def __repr__(self):
        return "Guitarist instance. Name = %s" % self.name
     
    def get_instrument(self):
        return "guitar"
    def play_solo(self):
        return "face melting guitar solo"

class Drummer(Musician):
    def __str__(self):
        return "My name is %s and I play drums" % self.name
    
    def __repr__(self):
        return  "Drummer instance. Name = %s"% self.name
   
    def get_instrument(self):
        return "drums"
    def play_solo(self):
        return "rattle boom crash"

class Bassist(Musician):
    def __str__(self):
        return "My name is %s and I play bass" % self.name
    def __repr__(self):
        return "Bassist instance. Name = %s"% self.name
    def get_instrument(self):
        return "bass"
    def play_solo(self):
        return "bom bom buh bom"