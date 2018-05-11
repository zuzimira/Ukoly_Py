
from pomocne_funkce import ukazuji_slovo, vyhodnot, tiskni_sibenici, kontrola_vstupu, vyber_slova
import random


def test_ukazuji_slovo():
    assert ukazuji_slovo('O', 'POLENO','_ _ _ _ _ _ ') == ('_ O _ _ _ O ', 'P*LEN*')
    assert ukazuji_slovo('A', 'APOLENA', '_ _ _ _ _ _ ')[0].count('A') == 2
    assert ukazuji_slovo('O', 'BRADA', '_ _ _ _ _ ') == ('_ _ _ _ _ ', 'BRADA')
    assert ukazuji_slovo('A', 'APATYKA', '_ _ _ _ _ _ ')[0].count('A') != 1

def test_vyhodnot():
    assert vyhodnot('_ _ _ _ _ _ _ _ _ _ ', 10) == 'prohra'
    assert vyhodnot('_ _ _ _ _ _ _ _ _ _ ', 9) == 'pokracujeme'
    assert vyhodnot ('POLENO', 6) != 'pokracujeme'


def test_tiskni():
    assert tiskni_sibenici(1) == '~~~~~~~'
    


def test_kontrola_vstupu():
    assert kontrola_vstupu('p') == True
    assert kontrola_vstupu('pp') == False
    assert kontrola_vstupu('/') == False
    assert kontrola_vstupu('č') == True

slova =  ["PARAPSYCHOLOGIE", "HROMDOPOLICE", "POSTAVA", "BRADAVICE", "BRONTOSAURUS", "KONIKLEC"]

def test_vyber_slova():  # muze selhat
    vybery = [vyber_slova(slova) for i in range(200)]
    assert vybery.count("PARAPSYCHOLOGIE") > 10
    assert vybery.count("HROMDOPOLICE") > 10
    assert vybery.count("POSTAVA") > 10
    assert vybery.count("BRADAVICE") > 10
    assert vybery.count("BRONTOSAURUS") > 10
    assert vybery.count("KONIKLEC") > 10
    for i in range(100):
        assert vyber_slova(slova ) in slova
