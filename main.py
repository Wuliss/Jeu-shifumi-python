#JEU DU PIERRE FEUILLE CISEAUX
import random

#computer choice
nbr_cp = random.randrange(1, 3);

if(nbr_cp == 1):
	cp_choice = 'pierre'
elif(nbr_cp == 2):
	cp_choice = 'feuille'
else:
	cp_choice = 'ciseaux'

#user choice
user_choice = input('Choisis entre pierre feuille ou ciseaux : ')

#show computer choice
print('L\'ordinateur a choisis : ', cp_choice)

#algo jeu
if(user_choice == cp_choice):
	print('Egalitée')
elif(user_choice == 'pierre' and cp_choice == 'feuille'):
	print('L\'ordi gagne !')
elif(user_choice == 'pierre' and cp_choice == 'ciseaux'):
	print('Le joueur gagne')
elif(user_choice == 'feuille' and cp_choice == 'pierre'):
	print('Le joueur gagne')
elif(user_choice == 'feuille' and cp_choice == 'ciseaux'):
	print('L\'ordi gagne !')
elif(user_choice == 'ciseaux' and cp_choice == 'pierre'):
	print('L\'ordi gagne !')
elif(user_choice == 'ciseaux' and cp_choice == 'feuille'):
	print('Le Joueur gagne !')
