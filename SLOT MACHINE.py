import random

def spin_row():
    symbols = ["🍒", "🍋", "🍊", "🍉", "⭐", "💎"]
    result = [random.choice(symbols) for _ in range(3)]
    return result

def print_row(row):
    print(" | ".join(row))

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 2
        elif row[0] == "🍋":
            return bet * 5
        elif row[0] == "🍊":
            return bet * 10
        elif row[0] == "🍉":
            return bet * 20
        elif row[0] == "⭐":
            return bet * 50
        elif row[0] == "💎":
            return bet * 100 
    return 0

def main():
    balance = 100
    print("Welcome to the Slot Machine!")
    print("Symbols: 🍒 🍋 🍊 🍉 ⭐ 💎")
    print("*****")
    
    while balance > 0:
        print(f"Current balance: ${balance}")
        
        # Keep input as a string first so we can check it properly
        bet_input = input("Enter your bet: ")
        
        if not bet_input.isdigit():
            print(" Invalid input. Please enter just the number (e.g., 20, not $20).")
            continue
            
        bet = int(bet_input)
        
        if bet > balance:
            print("Insufficient balance.")
            continue
        elif bet <= 0:
            print(" Bet must be greater than 0.")
            continue
            
        balance -= bet
        row = spin_row()
        print_row(row)
        
        payout = get_payout(row, bet)
        if payout > 0:
            print(f" Congrats..... You won ${payout}!")
        else:
            print("lol, you lost.")
            
        balance += payout

    print("KYU RE GAREEB!!!!!!!!!")

if __name__ == "__main__":
    main()