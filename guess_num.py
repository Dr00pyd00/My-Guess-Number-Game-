import random

def main():

    #set range of the list of numbers i gonna create catch error if user enter != int:
    start_range = 0
    while True:
        try:
            end_range = int(input('Range: '))
            break
        except ValueError:
            print('You muster enter a INTEGER.')
            continue


    #set a random number for guess it:
    num_list = [n for n in range(start_range, end_range +1)]
    the_num = random.choice(num_list)

    #ask a num and catch ValueError if not int ## and reduce the limites start/end each time :
    while True:

        try:

            user_num = input(f'Try guess between {start_range} and {end_range}:\n')

            if int(user_num) == the_num:
                print('CONGRATS !!')
                break

            elif int(user_num) > the_num:
                print('too big!')
                end_range = user_num

            elif int(user_num) < the_num:
                print('too low')
                start_range = user_num

        except ValueError:
            print('Wrong ! you MUST prompt a INTEGER !\n Try again !!')




if __name__ == '__main__':
    main()
