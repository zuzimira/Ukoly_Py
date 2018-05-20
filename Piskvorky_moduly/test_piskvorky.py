
import pytest
from piskvorky import vyhodnot
from ai import nahodny_tah, utocim, tah_pocitace

def test_vyhodnot_pozitivni():        #pozitivni
    assert vyhodnot('--xxx--')=='x'

def test_vyhodnot_negativni():        #negativni
    assert vyhodnot('--ooo--')!='x'

def test_nahodny_tah_pozitivni():        #pozitivni
    assert nahodny_tah("---xooxoxoxoxx-xoxoxoxoxxoxoxox---",'o') == 14
    assert nahodny_tah("----ooxx---",'o') == 3
    assert nahodny_tah("---xoxoxo-oxxoxox---",'o') == 9
    assert nahodny_tah('-xoxoxxooxxooxxooxox','o') == 0
def test_nahodny_tah_negativni():  #negativni
    assert nahodny_tah("-xoxoxoxox-xxoxoxxox",'o')!= 0
def test_nahodny_tah_negativni1():
    assert nahodny_tah("---xoxoxox-xxoxoxxox",'o')> 2


def test_utocim_pozitivni() :
    assert utocim('--o---o--','o')== 4  #pozitivni

def test_utocim_negativni() :
    assert utocim("-----o--",'o')!= 0  #negativni

def test_tah_pocitace_delka_pole() :   #pozitivni
    assert tah_pocitace("o-o--------------------xx","o")== "ooo--------------------xx"
    assert tah_pocitace("o-o--xx","o")== "ooo--xx"
    assert tah_pocitace("-oxxoxoxxoxoxxooxxoo") == "ooxxoxoxxoxoxxooxxoo"
def test_tah_pocitace_delka_pole_negativni() : #VYVOLANI VYJIMKY
    assert tah_pocitace("", "o")== 'o'
def test_tah_pocitace_delka_pole_negativni1() : #VYVOLANI VYJIMKY
    assert tah_pocitace("xoxoxoxox", "o")== "xoxoxoxoxo"



def test_tah_pocitace1() :  #negativni
    assert tah_pocitace("o-o----xx","o")!= "o-o---oxx"


def test_tah_pocitace2() : #pozitivni
    assert tah_pocitace("x-o-----------------",'o') in ("x-oo----------------", "xoo-----------------")

def test_tah_pocitace3() :  #negativni
    assert tah_pocitace("x----o--------------","o")!= "xo---o--------------"

def test_tah_pocitace_spatne4() :   #negativni
    assert tah_pocitace("x-o-------x---------",'o')|= "xoo-------x---------"

def test_tah_pocitace_spatne5() :   #pozitivni
    assert tah_pocitace("---xoxoxoxoxoxox----",'o')== "---xoxoxoxoxoxoxo---"
