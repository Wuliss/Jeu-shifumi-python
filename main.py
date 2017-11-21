#JEU DU PIERRE FEUILLE CISEAUX
import random

#asking number of rounds
user_nbr_round = int(input('Combien de manches ? '))
nbr_round = 0
while (nbr_round < user_nbr_round):

	#user choice
	user_choice = input('Choisis entre pierre feuille ou ciseaux : ')
	if(user_choice == 'pierre' or user_choice == 'feuille' or user_choice == 'ciseaux'):

		#computer choice
		can_use = ['pierre', 'feuille', 'ciseaux']
		cp_choice = random.choice(can_use)

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

		nbr_round = nbr_round + 1
		print('Manche numero ', nbr_round, ' sur ', user_nbr_round)
	else:
		print('Je ne comprend pas...')