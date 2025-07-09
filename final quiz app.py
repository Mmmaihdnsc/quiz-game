def quiz(): 
    print('\t This is a quiz game')
    score=0 # starting score for all players
    qns= {
    "Who is known as the father of computers?": "Charles Babbage",
    "What is the largest ocean on Earth?": "Pacific",
    "Which gas do plants absorb from the atmosphere?": "Carbon dioxide",       #quiz questions
    "What is the square root of 144?": "12",
    "Which country is famous for the Great Wall?": "China"
     }
    x=input('entre your name ')                                                 # player name
    for i,j in qns.items():                                                     # to take the questions one by one
        tries=3                                                                 # each question have 3 tries
        for d in range(3):                                                      #to run 3 time
         
            print(f'you have {tries} tries to guess this question \n')          #display question
            ans=input(i)                                                        #get answer
            if j.lower()==ans.lower().strip():                                  #check answer
                print('correct answer \n')                                      #display if it is correct
                score+=1                                                        #add score
                break
            else:
                if tries >1:                                                    #display message for wrong answer
                    print('wrong answer guess again \n')
                    tries-=1                                                    #decrease in tries
                else: 
                    print('you got all tries wrong no points for this question \n')#display if all tries are wrong
    print(f'your total score{score}out of 5')                                      # add score into the txt file
    file=open('final quiz score.txt','a')
    file.write(f'{x} scored {score}')
    file.close()
    print('your scores have been saved')
quiz()


         