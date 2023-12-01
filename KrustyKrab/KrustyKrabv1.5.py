import random

Price = float(0)
Cart = []
# всем привет с вами мр бист в этом ролике я построил красти крабс
quote = random.randint(1, 3)
# интро небольшое
if quote == 1:
    quote = str('"Squidward, where are you? Shield me with your forehead!" ~ Mr. Krabs')
elif quote == 2:
    quote = str('"What doesnt kill you, usually succeeds in the second attempt." ~ Mr. Krabs')
elif quote == 3:
    quote = str('"A 5 letter word for happiness: MONEY." ~ Mr. Krabs')
print('Welcome to Krusty Krubs!')
print("You are customer №", random.randint(1, 100000))
print(quote)
IsWorking = int(input('Do you want to continue? (1-yes)'))
while IsWorking == 1:
    # выбор тут
    print("Krabby patty - [1.25$] - 1")
    print('Coral bits - 2')
    print('Kelp rings - [1.49$] - 3')
    print('Kelp shake - [1.99$] - 4')
    print('Krabby meal - [3.49$] - 5')
    Choise = int(input("Choose your meal! (1-5)"))

    # результат выбора
    if Choise == 1:
        Cart.append("Krabby patty")
        Price = Price + 1.25
    elif Choise == 2:
        SMB = int(input('Choise the size! small - [0.99$], medium - [1.25$], big - [1.49$] (1-3) '))
        if SMB == 1:
            Cart.append("Small coral bits")
            Price = Price + 0.99
        if SMB == 2:
            Cart.append("Medium coral bits")
            Price = Price + 1.25
        if SMB == 3:
            Cart.append("Big coral bits")
            Price = Price + 1.49
    elif Choise == 3:
        Sauce = int(input('Add sauce + [0.49$] (1 - yes)'))
        if Sauce == 1:
            Cart.append("Kelp Rings with sauce")
            Price = Price + 1.98
        else:
            Cart.append('Kelp Rings')
            Price = Price + 1.49
    elif Choise == 4:
        Cart.append('Kelp shake')
        Price = Price + 1.99
    elif Choise == 5:
        Cart.append("Krabby meal")
        Price = Price + 3.49
    IsWorking = int(input("Continue, or check out? 1 - Continue, anything else - check out"))
# конец
print(Price, "$")
DoPay = int(input('Are you sure? 1 - Yes, continue check out; anything else - cancel your order'))
if DoPay == 1:
    Payment = int(input("Cash or Card? 1 - Pay with cash; 2 - Use your card."))
    if Payment == 1:
        Moneyz = int(input("Insert cash"))
        print(Moneyz - Price, "Is your change. Thank you!")
    if Payment == 2:
        print("Processing your payment...")
        print('Thank you!')


def my_decorator(funk):
    def wrapper():
        print("______________________________")
        funk()
        print("______________________________")
    return wrapper

@my_decorator
def checkout():
    print('Krusty Krab')
    print('Your order number:', random.randint(100, 999))
    print("You've paid ", Price,"$")
    print("Goodbye! We hope to see you again.")
    print('~Mr. Krabs')