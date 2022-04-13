#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Module(s) de la librairie par défaut de Python
import random

#Module(s) de Pypi
import tkinter as tk

#Module(s) de l'application
#...

class Password():
    
    def __init__(self,password_length : int = 20, gen_code : int = 15) -> None:
        self.password = ""
        
        self.lower_alpha_list = list("abcdefghijklmnopqrstuvwxyz")
        self.upper_alpha_list = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.symbol_list = list("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
        self.number_list = list("1234567890")
        
        self.temp_element_list = [self.lower_alpha_list, 
                                  self.upper_alpha_list, 
                                  self.symbol_list,
                                  self.number_list]
        
        self.password_length = password_length
        
        self.gen_list = self._decryptGenCode(gen_code)
        
        self.element_list = self._createElementList()

    def getGenList(self) -> list[str]:
        return self.gen_list
    
    def getElementList(self) -> list[list[str]]:
        return self.element_list
    
    def getPassword(self) -> str:
        return self.password
    
    def reinitialisePassword(self) -> None:
        self.password = ""
        
    def _decryptGenCode(self, gen_code : int) -> list[str]:
        result = list(bin(gen_code))[2:]
        
        while len(result) < 4:
            result.insert(0,"0")
            
        if result == ["0", "0", "0", "0"]:
            result = ["1", "1", "1", "1"]
            
        return result
    
    def _createElementList(self) -> list[list[str]]:
        return [
            self.temp_element_list[i]
            for i, c in enumerate(self.gen_list)
            if int(c)
        ]
        
    def createPassword(self) -> None:   
        self.reinitialisePassword()
             
        for _ in range(self.password_length):
            self.password += random.choice(random.choice(self.element_list))
            
        self._checkPassword()    
    
    def _checkPassword(self) -> None:
        for el in self.element_list:
            for char in el:
                if char in self.password:
                    break
          
            else:      
                self.createPassword()
                
    def printPassword(self, entry : tk.Entry) -> None:
        self.createPassword()
        entry.delete(0, tk.END)
        entry.insert(0, self.password)
    