#!/usr/bin/env python
# coding: utf-8

# ## Wiederholung Properties und Inheritance
# 
# ### Bsp. 04.1
# Vervollständigen Sie nachfolgende Klasse `Robot` mit dem Ziel der *Blacklist*-Überprüfung. Generell gilt: Wird beim Instanziieren keine Name angegeben oder ist dieser in der Blacklist `_fobidden_names` angeführt, gilt es den *Default*-Namen *Marvin* zuzuweisen. In allen anderen Fällen ist der Name gemäß Argument zu setzen.    

# In[9]:


_forbidden_names = ["Charly", "Alan"]

class Robot:
    def __init__(self, name="Marvin"):
        if name in _forbidden_names:
            self.name = "Marvin"
        else:
            self.name = name
        
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        if name in _forbidden_names:
            print(f"Can't change name to {name} because it is forbidden")
        else:
            self.name = name
            print(f"Successfully changed name to {name}")


# **Testszenarien**: Zeigen Sie die Funktionsweise anhand nachfolgender Tests!

# In[10]:


r = Robot()
r.get_name()
# Output: 'Marvin'


# In[10]:


r2=Robot("Alan")
r2.get_name()
# Output: 'Marvin'


# In[11]:


r3=Robot("Markus")
r3.get_name()
# Output: 'Markus'


# ### Bsp. 04.2
# Durch den Einsatz der *Decorators* `@property` und `@...setter` kann man, wie es in Python üblich ist, via Attribut zugreifen - also "pythonsich". Adaptieren Sie den Code vom ersten Bsp.:

# In[ ]:


_forbidden_names = ["Charly", "Alan"]

class Robot:
    def __init__(self, name="Marvin"):
        if name in _forbidden_names:
            self.name = "Marvin"
        else:
            self.name = name
        
    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self, name):
        if name in _forbidden_names:
            print(f"Can't change name to {name} because it is forbidden")
        else:
            self.name = name
            print(f"Successfully changed name to {name}")


# **Testszenario**:

# In[ ]:


r = Robot("R2D2")
print(r.name)
r.name="D2R2"
print(r.name)


# ### Bsp. 04.3 - Inheritance
# Gegen ist die Klasse Robot mit folgender Implementierung:

# In[2]:


class Robot():
    
    def __init__(self, name="Marvin"):
        self.name=name
    
    
    def say_hello(self):
        return f"Hello, I'm {self.name}"


# `say_hello` liefert folgenden Output:

# In[3]:


r3 = Robot()
r3.say_hello()


# Die Klasse `MedicalRobot` ist von `Robot` abgeleitet und ergänzt diese um die Methode `heal`, die einen beliebigen Namen als Argument übernimmt und ausgibt.

# In[4]:


class MedicalRobot(Robot):
    
    def heal(self, name):
        return f"{name} is healed now, or maybe not!"


# Überschreiben Sie in der Klasse `MedicalRobot` die Methode `say_hello` mit dem Ziel, dass nachfolgende Tests das definierte Ergebnis liefern.

# In[11]:


class MedicalRobot(Robot):
    
    def heal(self, x):
        return f"{x} is healed now, or maybe not!"
    
    def say_hello(self):
        return f"Hello, I'm {self.name}, your personal nurse!"


# **Tests**:

# In[12]:


mr = MedicalRobot("Kelvin")
print(mr.say_hello())
# Output: Hello, I'm Kelvin, your personal nurse!


# In[ ]:




