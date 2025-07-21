import re

# n je broj elemenata ploce
def generirajPlocu(n):
    ploca_el = [1] * n
    return ploca_el
    
def rijesena(ploca):
    if sum(ploca) == 1:
        return True
    return False

def nerijesena(ploca):
    # izrazi koji za koje je dokazano da rjesenje ne postoji (Moore i Eppstien)
    izraz1 = '1000+1'
    izraz2 = '00100'
    string_pl = ''.join([str(element) for element in ploca])
    if(re.search(izraz1, string_pl) or re.search(izraz2, string_pl)):
        return True
    return False

def napraviPotez(ploca, potez):
    pozicija, smjer = potez
    p = [element for element in ploca]
    if(smjer == 'desno'):
        p[pozicija] = 0
        p[pozicija + 1] = 0
        p[pozicija + 2] = 1
    elif(smjer == 'lijevo'):
        p[pozicija] = 0
        p[pozicija - 1] = 0
        p[pozicija - 2] = 1  
    return p

def rijesi(ploca):
    if(rijesena(ploca)):
        return True
    elif(nerijesena(ploca)):
        return False

    potezi = []
    for i in range(len(ploca)):
        if(i < (len(ploca) - 2)):
            if(ploca[i] and ploca[i + 1] and not ploca[i + 2]):
                potezi.append((i, 'desno'))
        if(i > 1):
            if(ploca[i] and ploca[i - 1] and not ploca[i - 2]):
                potezi.append((i, 'lijevo'))

    for potez in potezi:
        novaPloca = napraviPotez(ploca, potez)
        if rijesi(novaPloca):
            return True
        continue
    return False

def broji(ploca):
    poz = []
    for i in range(len(ploca)):
        b = [element for element in ploca]
        b[i] = 0
        if rijesi(b):
            poz.append(i + 1)
    return poz


def jd_pasijans(n):
    return (broji(generirajPlocu(n)))

#najmanje moguce rjesenje
n = 3
print('Za n = 3 pocetne prazne pozicije se nalaze na indexima: ', jd_pasijans(n))

n = 4
print('Za n = 4 pocetne prazne pozicije se nalaze na indexima: ', jd_pasijans(n))

# za nizove cija je duljina neparan broj nema rjesenja
n = 5
print('Za n = 5 pocetne prazne pozicije se nalaze na indexima: ', jd_pasijans(n))

n = 6
print('Za n = 6 pocetne prazne pozicije se nalaze na indexima: ', jd_pasijans(n))

n = 18
print('Za n = 18 pocetne prazne pozicije se nalaze na indexima: ', jd_pasijans(n))
























        
        
    
        
