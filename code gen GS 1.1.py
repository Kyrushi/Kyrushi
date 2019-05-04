# Note to self on future team checker:
# Make dictionary of pokemon names with types as defintiions
# Have it go through every type against both types on each pokemon
# Super Effective (O) = +1
# Neutral (-) = +0
# Resistant (X) = -1
# Full Resist = *0 (for that pokemon, not entire equasion)
# Add weakness totals together
# In the end display all weaknesses in numbers

BASE = '01'

Pokemon1 = []
Pokemon2 = []
Pokemon3 = []
Pokemon4 = []
Pokemon5 = []
Pokemon6 = []
Extra = []

#############
#Move Editor#
#############
ATTACK1_1 = '2CDA'
ATTACK1_2 = '2DDA'
ATTACK1_3 = '2EDA'
ATTACK1_4 = '2FDA'

ATTACK2_1 = '5CDA'
ATTACK2_2 = '5DDA'
ATTACK2_3 = '5EDA'
ATTACK2_4 = '5FDA'

ATTACK3_1 = '8CDA'
ATTACK3_2 = '8DDA'
ATTACK3_3 = '8EDA'
ATTACK3_4 = '8FDA'

ATTACK4_1 = 'BCDA'
ATTACK4_2 = 'BDDA'
ATTACK4_3 = 'BEDA'
ATTACK4_4 = 'BFDA'

ATTACK5_1 = 'ECDA'
ATTACK5_2 = 'EDDA'
ATTACK5_3 = 'EEDA'
ATTACK5_4 = 'EFDA'

ATTACK6_1 = '1CDB'
ATTACK6_2 = '1DDB'
ATTACK6_3 = '1EDB'
ATTACK6_4 = '1FDB'

###########
#Happiness#
###########
def HAPPY():
    print('Pokemon 1: 01FF45DA')
    print('Pokemon 2: 01FF75DA')
    print('Pokemon 3: 01FFA5DA')
    print('Pokemon 4: 01FFD5DA')
    print('Pokemon 5: 01FF05DB')
    print('Pokemon 6: 01FF35DB')

#########
#Pokerus#
#########
POKERUS1 = 'AA46DA'
POKERUS2 = 'AA76DA'
POKERUS3 = 'AAA6DA'
POKERUS4 = 'AAD6DA'
POKERUS5 = 'AA06DB'
POKERUS6 = 'AA36DB'

####################
#Hidden Power / IVs#
####################
HP = {'dark':     'FF',
      'dragon':   'FE',
      'ice':      'FD',
      'psychic':  'FC',
      'electric': 'EF',
      'grass':    'EE',
      'water':    'ED',
      'fire':     'EC',
      'steel':    'DF',
      'ghost':    'DE',
      'bug':      'DD',
      'rock':     'DC',
      'ground':   'CF',
      'poison':   'CE',
      'flying':   'CD',
      'fighting': 'CC'}

PIV1 = '3FDA'
PIV2 = '6FDA'
PIV3 = '9FDA'
PIV4 = 'CFDA'
PIV5 = 'FFDA'
PIV6 = '2FDB' #Physical IVs
 

SIV1 = 'FF40DA'
SIV2 = 'FF70DA'
SIV3 = 'FFA0DA'
SIV4 = 'FFD0DA'
SIV5 = 'FF00DB'
SIV6 = 'FF30DB' #Special IVs

#####
#EVs#
#####

def MAXSTATS():
    print('To save time typing code, switch pokemon to first slot one by one')
    print('01FF35DA')
    print('01FF36DA')
    print('01FF37DA')
    print('01FF38DA')
    print('01FF39DA')
    print('01FF3ADA')
    print('01FF3BDA')
    print('01FF3CDA')
    print('01FF3DDA')
    print('01FF3EDA')

###################
#(Sorta) Level 100#
###################

def MAXLEVEL():
    print('This code is only temperary. Use rare candy to assure the level stays.')
    print('Also note that you MUST have a full party or the game will crash.')
    print('016349DA')
    print('016379DA')
    print('0163A9DA')
    print('0163D9DA')
    print('016309DB')
    print('016339DB')
    print('')
    print('Rare Candy Code; Just in case. Will replace first item.')
    print('0120B8D5')
    print('0163B9D5')


Moves = {'_': '00',
         'fire punch': '07',
         'ice punch': '08',
         'thunder punch': '09',
         'guillotine': '0C',
         'swords dance': '0E',
         'sword': '0E',
         'wing attack': '11',
         'whirl wind': '12',
         'whirlwind': '12',
         'horn drill': '20',
         'body slam': '22',
         'twin needle': '29',
         'wrap': '23',
         'bite': '2C',
         'roar': '2E',
         'ember': '34',
         'flamethrower': '35',
         'mist': '36',
         'hydro pump': '38',
         'surf': '39',
         'ice beam': '3A',
         'blizzard': '3B',
         'drill peck': '41',
         'counter': '44',
         'seismic toss': '45',
         'toss': '45',
         'leech seed': '49',
         'seed': '49',
         'growth': '4A',
         'razor leaf': '4B',
         'solar beam': '4C',
         'solar': '4C',
         'stun spore': '4E',
         'sleep powder': '4F',
         'dragon rage': '52',
         'fire spin': '53',
         'thunderbolt': '55',
         'thunder wave': '56',
         'twave': '56',
         'thunder': '57',
         'earthquake': '59',
         'quake': '59',
         'toxic': '5C',
         'psychic': '5E',
         'hypnosis': '5F',
         'meditate': '60',
         'agility': '61',
         'quick attack': '62',
         'quick': '62',
         'night shade': '65',
         'shade': '65',
         'screech': '67',
         'recover': '69',
         'confuse ray': '6D',
         'confuse': '6D',
         'ray': '6D',
         'barrior': '70',
         'light screen': '71',
         'haze': '72',
         'reflect': '73',
         'mirror move': '77',
         'mirror': '77',
         'fire blast': '7E',
         'clamp': '80',
         'amnesia': '85',
         'softboiled': '87',
         'hi jump kick': '88',
         'hi': '88',
         'glare': '89',
         'lovely kiss': '8E',
         'spore': '93',
         'crabhammer': '98',
         'crab': '98',
         'explosion': '99',
         'rock slide': '9D',
         'substitute': 'A4',
         'triple kick': 'A7',
         'theif': 'A8',
         'spider web': 'A9',
         'mind reader': 'AA',
         'curse': 'AE',
         'flail': 'AF',
         'areoblast': 'B1',
         'reversal': 'B3',
         'protect': 'B6',
         'mach punch': 'B7',
         'faint attack': 'B9',
         'sweet kiss': 'BA',
         'belly drum': 'BB',
         'sludge bomb': 'BC',
         'octazooka': 'BE',
         'spikes': 'BF',
         'destiny bond': 'C2',
         'perish song': 'C3',
         'detect': 'C5',
         'lock on': 'C7',
         'outrage': 'C8',
         'sandstorm': 'C9',
         'giga drain': 'CA',
         'endure': 'CB',
         'swagger': 'CF',
         'milk drink': 'D0',
         'milk': 'D0',
         'steel wing': 'D3',
         'mean look': 'D4',
         'attract': 'D5',
         'heal bell': 'D7',
         'return': 'D8',
         'safeguard': 'DB',
         'pain split': 'DC',
         'scared fire': 'DD',
         'dynamicpunch': 'DF',
         'megahorn': 'E0',
         'dragonbreath': 'E1',
         'baton pass': 'E2',
         'encore': 'E3',
         'pursuit': 'E4',
         'rapid spin': 'E5',
         'morning sun': 'EA',
         'synthesis': 'EB',
         'moonlight': 'EC',
         'hidden power': 'ED',
         'cross chop': 'EE',
         'rain dance': 'F0',
         'sunny day': 'F1',
         'crunch': 'F2',
         'mirror coat': 'F3',
         'pysch up': 'F4',
         'extremespeed': 'F5',
         'extreme speed': 'F5',
         'ancientpower': 'F6',
         'ancient power': 'F6',
         'shadow ball': 'F7',
         'future sight': 'F8',
         'whirlpool': 'FA',
         'zap cannon': 'C0'}

def Check_Move(Ms, M, As, P):
    if M in Ms:
        As = As + 1
        P.append(M)
        return As, P
    else:
        print('')
        print("Either the move doesn't exist or you typed it incorrectly.")
        print('')
        return As, P

###################################################################################
run = 'true'
print('Code generator G/S by Kyrushi')
print('You can contact me on Twitter @Kyrushi_')
print('Please use lowercase when typing inputs!')
print('')
Pokemon = int(input('How many pokemon are you editing? '))

while run == 'true':
    print('')
    Action = input('What are you editing? [moves/evs/ivs/happiness/level] ')
    print('')

    if Action == 'moves':
        Finished = int(0)
        Printed = int(0)
        print('Please type the attack names in order. "_" is a blank slot')
        print('')

        while Finished < Pokemon:
            Attacks = int(1)
            if Finished == 0:
                print('Pokemon 1')
                while Attacks < 5:
                    print('Attack', str(Attacks),end=': ')
                    Move = input()
                    (Attacks, Pokemon1) = Check_Move(Moves, Move, Attacks, Pokemon1)
                    if Attacks == 5:
                        Finished += 1
                    
            elif Finished == 1:
                print('')
                print('Pokemon 2')
                while Attacks < 5:
                    print('Attack', str(Attacks),end=': ')
                    Move = input()
                    (Attacks, Pokemon2) = Check_Move(Moves, Move, Attacks, Pokemon2)
                    if Attacks == 5:
                        Finished += 1
                        
            elif Finished == 2:
                print('')
                print('Pokemon 3')
                while Attacks < 5:
                    print('Attack', str(Attacks),end=': ')
                    Move = input()
                    (Attacks, Pokemon3) = Check_Move(Moves, Move, Attacks, Pokemon3)
                    if Attacks == 5:
                        Finished += 1
                        
            elif Finished == 3:
                print('')
                print('Pokemon 4')
                while Attacks < 5:
                    print('Attack', str(Attacks),end=': ')
                    Move = input()
                    (Attacks, Pokemon4) = Check_Move(Moves, Move, Attacks, Pokemon4)
                    if Attacks == 5:
                        Finished += 1
                        
            elif Finished == 4:
                print('')
                print('Pokemon5')
                while Attacks < 5:
                    print('Attack', str(Attacks),end=': ')
                    Move = input()
                    (Attacks, Pokemon5) = Check_Move(Moves, Move, Attacks, Pokemon5)
                    if Attacks == 5:
                        Finished += 1
                        
            elif Finished == 5:
                print('')
                print('Pokemon 6')
                while Attacks < 5:
                    print('Attack', str(Attacks),end=': ')
                    Move = input()
                    (Attacks, Pokemon6) = Check_Move(Moves, Move, Attacks, Pokemon6)
                    if Attacks == 5:
                        Finished += 1


        while Printed < Finished:
            if Printed == 0:
                print('')
                print('Pokemon 1')
                print(BASE + Moves[Pokemon1[0]] + ATTACK1_1 , Pokemon1[0])
                print(BASE + Moves[Pokemon1[1]] + ATTACK1_2 , Pokemon1[1])
                print(BASE + Moves[Pokemon1[2]] + ATTACK1_3 , Pokemon1[2])
                print(BASE + Moves[Pokemon1[3]] + ATTACK1_4 , Pokemon1[3])
                Printed += 1
                del Pokemon1[:]

            elif Printed == 1:
                print('')
                print('Pokemon 2')
                print(BASE + Moves[Pokemon2[0]] + ATTACK2_1 , Pokemon2[0])
                print(BASE + Moves[Pokemon2[1]] + ATTACK2_2 , Pokemon2[1])
                print(BASE + Moves[Pokemon2[2]] + ATTACK2_3 , Pokemon2[2])
                print(BASE + Moves[Pokemon2[3]] + ATTACK2_4 , Pokemon2[3])
                Printed += 1
                del Pokemon2[:]

            elif Printed == 2:
                print('')
                print('Pokemon 3')
                print(BASE + Moves[Pokemon3[0]] + ATTACK3_1 , Pokemon3[0])
                print(BASE + Moves[Pokemon3[1]] + ATTACK3_2 , Pokemon3[1])
                print(BASE + Moves[Pokemon3[2]] + ATTACK3_3 , Pokemon3[2])
                print(BASE + Moves[Pokemon3[3]] + ATTACK3_4 , Pokemon3[3])
                Printed += 1
                del Pokemon3[:]

            elif Printed == 3:
                print('')
                print('Pokemon 4')
                print(BASE + Moves[Pokemon4[0]] + ATTACK4_1 , Pokemon4[0])
                print(BASE + Moves[Pokemon4[1]] + ATTACK4_2 , Pokemon4[1])
                print(BASE + Moves[Pokemon4[2]] + ATTACK4_3 , Pokemon4[2])
                print(BASE + Moves[Pokemon4[3]] + ATTACK4_4 , Pokemon4[3])
                Printed += 1
                del Pokemon4[:]

            elif Printed == 4:
                print('')
                print('Pokemon 5')
                print(BASE + Moves[Pokemon5[0]] + ATTACK5_1 , Pokemon5[0])
                print(BASE + Moves[Pokemon5[1]] + ATTACK5_2 , Pokemon5[1])
                print(BASE + Moves[Pokemon5[2]] + ATTACK5_3 , Pokemon5[2])
                print(BASE + Moves[Pokemon5[3]] + ATTACK5_4 , Pokemon5[3])
                Printed += 1
                del Pokemon5[:]

            elif Printed == 5:
                print('')
                print('Pokemon 6')
                print(BASE + Moves[Pokemon6[0]] + ATTACK6_1 , Pokemon6[0])
                print(BASE + Moves[Pokemon6[1]] + ATTACK6_2 , Pokemon6[1])
                print(BASE + Moves[Pokemon6[2]] + ATTACK6_3 , Pokemon6[2])
                print(BASE + Moves[Pokemon6[3]] + ATTACK6_4 , Pokemon6[3])
                Printed += 1
                del Pokemon6[:]
                
    elif Action == 'evs':
        MAXSTATS()

    elif Action == 'ivs':
        Finished = int(0)
        Printed = int(0)
        print('Please type the desired Hidden Powers in order [dark is perfect stats]')

        while Finished < Pokemon:
            if Finished == 0:
                print('')
                H_Power = input('Pokemon 1: ')
                if H_Power in HP:
                    Finished += 1
                else:
                    print('not an existing type or wrong context')
                    print('')
                    
            elif Finished == 1:
                H_Power2 = input('Pokemon 2: ')
                if H_Power2 in HP:
                    Finished += 1
                else:
                    print('not an existing type or wrong context')
                    print('')
                        
            elif Finished == 2:
                H_Power3 = input('Pokemon 3: ')
                if H_Power3 in HP:
                    Finished += 1
                else:
                    print('not an existing type or wrong context')
                    print('')
                        
            elif Finished == 3:
                H_Power4 = input('Pokemon 4: ')
                if H_Power4 in HP:
                    Finished += 1
                else:
                    print('not an existing type or wrong context')
                    print('')
                        
            elif Finished == 4:
                H_Power5 = input('Pokemon 5: ')
                if H_Power5 in HP:
                    Finished += 1
                else:
                    print('not an existing type or wrong context')
                    print('')
                        
            elif Finished == 5:
                H_Power6 = input('Pokemon 6: ')
                if H_Power6 in HP:
                    Finished += 1
                else:
                    print('not an existing type or wrong context')
                    print('')

        while Printed < Finished:
            if Printed == 0:
                print('')
                print('Pokemon 1: ' + H_Power)
                print(BASE + HP[H_Power] + PIV1)
                print(BASE + SIV1)
                Printed += 1

            elif Printed == 1:
                print('')
                print('Pokemon 2: ' + H_Power2)
                print(BASE + HP[H_Power2] + PIV2)
                print(BASE + SIV2)
                Printed += 1

            elif Printed == 2:
                print('')
                print('Pokemon 3: ' + H_Power3)
                print(BASE + HP[H_Power3] + PIV3)
                print(BASE + SIV3)
                Printed += 1

            elif Printed == 3:
                print('')
                print('Pokemon 4: ' + H_Power4)
                print(BASE + HP[H_Power4] + PIV4)
                print(BASE + SIV4)
                Printed += 1

            elif Printed == 4:
                print('')
                print('Pokemon 5: ' + H_Power5)
                print(BASE + HP[H_Power5] + PIV5)
                print(BASE + SIV5)
                Printed += 1

            elif Printed == 5:
                print('')
                print('Pokemon 6: ' + H_Power6)
                print(BASE + HP[H_Power6] + PIV6)
                print(BASE + SIV6)
                Printed += 1

    elif Action == 'happiness':
        HAPPY()

    elif Action == 'level':
        MAXLEVEL()
