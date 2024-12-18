# Closure is a function having access to the scope of its parent function after parent funtion has returned
def parent_function(person,coins):
    # coins = 3

    def play_game():
        nonlocal coins
        coins -=1

        if coins>1:
            print("\n"+person+" has "+str(coins)+" coins left.")
        elif coins == 1:
            print("\n"+person+" has "+str(coins)+" coins left.")
        else:
            print("\n"+person+" is out of coins. ")
        
    return play_game
tommy = parent_function("Tommy",3)
jeni = parent_function("jeni",4)

tommy()
tommy()
jeni()
tommy()


def make_multiplier_of(n):
    def multiplier(x):
        return x*n
    return multiplier

times3=make_multiplier_of(3)
times5=make_multiplier_of(5)

print(times3(9))
print(times5(3))

print(times5(times3(2)))