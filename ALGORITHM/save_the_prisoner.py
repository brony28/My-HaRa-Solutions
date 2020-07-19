#SAVE THE PRISONER!



t = int(input())

for _ in range(t):
    numOfPris,numOfSweets,startChair = list(map(int,input().split()))
    print( ((numOfSweets-1)+(startChair-1))%numOfPris + 1 )


    '''
My way of understanding and solving

    numOfSweets index starts from 0 and ends at numOfSweets-1.
    Since % is used its better to keep the index value from.
    startChair is subtracted by 1, so that the counting starts from next value of startChair. Again helpful for index starting from 0.
    Now taking mod value by numOfPris to find the index of the last chocolate.(Note the index now represent the Prisoners seated i.e starting from 0[intead of 1] upto numOfPris-1)
    Now finally the result is added by 1, to set the result in the range of 1 to numOfPris
    '''
    #Help taken from : 
    #https://www.hackerrank.com/challenges/save-the-prisoner/forum/comments/185775