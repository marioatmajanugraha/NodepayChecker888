import requests
import re

# ASCII Art
print(r"""
 █████╗ ██╗██████╗ ██████╗ ██████╗  ██████╗ ██████╗ 
██╔══██╗██║██╔══██╗██╔══██╗██╔══██╗██╔═══██╗██╔══██╗
███████║██║██████╔╝██║  ██║██████╔╝██║   ██║██████╔╝
██╔══██║██║██╔══██╗██║  ██║██╔══██╗██║   ██║██╔═══╝ 
██║  ██║██║██║  ██║██████╔╝██║  ██║╚██████╔╝██║     
╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝     

             █████╗  █████╗  █████╗                 
            ██╔══██╗██╔══██╗██╔══██╗                
            ╚█████╔╝╚█████╔╝╚█████╔╝                
            ██╔══██╗██╔══██╗██╔══██╗                
            ╚█████╔╝╚█████╔╝╚█████╔╝                
             ╚════╝  ╚════╝  ╚════╝                 
""")
print("Welcome to NodePay Airdrop Checker!")
print("By Airdrop 888 | @balveerxyz\n")
print("=" * 50 + "\n")

def clean_text(text):
    """
    Function to clean escape sequences from text
    """
    return re.sub(r'\x1b\[[0-9;]*m', '', text)

def checkElig(token):
    try:
        # Define the API endpoint
        url = "https://api.nodepay.ai/api/season/airdrop-status?"
        
        # Define headers with the Bearer token
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        
        # Send the Get request
        response = requests.get(url, headers=headers)
        data = response.json().get('data', {})
        
        # Extract data
        is_eligible = data.get('is_eligible')
        wallet = data.get('wallet_address')
        season01 = data.get('season1_tokens')
        season02 = data.get('season2_tokens')
        
        # Display results
        print("🕵️‍♂️ Checking Token...")
        print(f"┌{'─' * 46}┐")
        print(f"│ Wallet Address: {wallet}")
        print(f"│ Eligibility Status: {'✔️ Eligible' if is_eligible else '❌ Not Eligible'}")
        
        if is_eligible:
            print(f"│ Season 0 & 1 Tokens: {season01} Tokens")
            if season02 is None:
                print(f"│ Season 2 Status: To Be Determined!")
            else:
                print(f"│ Season 2 Tokens: {season02} Tokens")
        else:
            print("│ Sorry, You are not eligible.")
        
        print(f"└{'─' * 46}┘")
        print("\n")
    
    except Exception as e:
        print("Error:", e)
        print(f"└{'─' * 46}┘")
        print("\n")

try:
    with open('token_list.txt', 'r') as file:
        local_data = file.read().splitlines()
        for token_list in local_data:
            checkElig(token_list)
except FileNotFoundError:
    print("Error: token_list.txt file not found.")
