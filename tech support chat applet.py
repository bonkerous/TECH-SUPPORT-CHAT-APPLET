import time

problem = (input('Hello my name is salah from microsoft tech support how may I help u today? '))

input('Okay i need u to download anydesk for me to acces yor computer and help ')

def anydesk_loop():
	def anydesk_cred_loop():
		global anydesk_id
		anydesk_id = (str(input('Please give me ur anydesk id its a bunch of number ')))
		global anydesk_pass
		anydesk_pass = (str(input('Now please tell me the password to anydesk its the other numbers ')))
		print(f"Okay ur id is {anydesk_id} and your password is {anydesk_pass}... Is dis correct? Yes or No....")
	anydesk_cred_loop()
	
	def anydesk_correct_loop():
	
		if anydesk_correct == 'Yes':
			print('Ok i am connecting now please wait')
			time.sleep(3)
			print('Hai i connected successfully im going to steal all ur moneyz :3c')
			time.sleep(1)
			print('U got: Bad ending')
			print("You're broke now lmfaoooo")
			print("More endings coming soon -bonk")
			exit(input('Press enter to exit application'))
		elif anydesk_correct == 'No':
			anydesk_cred_loop()
		else:
			print('Please reply correctly u dumb dog retard')
		anydesk_ask()

	def anydesk_ask():
		global anydesk_correct
		anydesk_correct = (input())
		anydesk_correct_loop()
	
	anydesk_ask()

anydesk_loop()