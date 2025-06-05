import csv
import os
from eth_account import Account
import secrets

def generate_ethereum_wallet():
    # Generate a random private key
    private_key = secrets.token_hex(32)
    # Create an account from the private key
    account = Account.from_key(f"0x{private_key}")
    # Return the address and private key
    return {
        'address': account.address,
        'private_key': private_key
    }

def generate_multiple_wallets(count):
    wallets = []
    for _ in range(count):
        wallet = generate_ethereum_wallet()
        wallets.append(wallet)
    return wallets

def save_to_csv(wallets, filename):
    # Ensure the directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    # Write to CSV file
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['address', 'private_key']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for wallet in wallets:
            writer.writerow(wallet)
    
    print(f"Saved {len(wallets)} wallets to {filename}")

def main():
    # Number of wallets to generate
    wallet_count = int(input("Enter the number of Ethereum wallets to generate: "))
    
    # Generate wallets
    print(f"Generating {wallet_count} Ethereum wallets...")
    wallets = generate_multiple_wallets(wallet_count)
    
    # Save to CSV
    csv_filename = "ethereum_wallets.csv"
    save_to_csv(wallets, csv_filename)
    
    print("Done!")

if __name__ == "__main__":
    main()
