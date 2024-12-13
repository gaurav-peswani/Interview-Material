"""
Problem Description:
You are building the backend for a peer-to-peer payment app called StripePay. 
It manages user accounts, allowing them to send and receive money, 
as well as transfer funds to and from their connected bank accounts. 
The backend must process commands in chronological order, ensuring all 
constraints are satisfied.

Supported Commands:
1. INIT:
   - Usage: INIT,name,balance,bank_1,bank_2,...,bank_n
   - Initializes a Stripe account for 'name' with the given balance and connected banks.
   - No response value.

2. POST:
   - Usage: POST,timestamp,sender,receiver,amount
   - Processes a transaction where 'sender' sends 'amount' to 'receiver'.
   - Rules:
     - If the sender's account becomes negative, return "FAILURE".
     - If the sender is a bank, this is treated as a deposit to the receiver:
       - If the receiver lacks the bank in their connected banks, return "FAILURE".
       - Otherwise, return "SUCCESS".
     - If the receiver is a bank, this is treated as a withdrawal from the sender:
       - If the sender lacks the bank in their connected banks, return "FAILURE".
       - Otherwise, return "SUCCESS".
     - Transactions between two banks always return "FAILURE".
     - If either the sender or receiver does not exist, return "FAILURE".

3. GET:
   - Usage: GET,timestamp,name
   - Returns the balance of the given 'name'.
   - If 'name' does not exist, return "FAILURE".

Input:
- A list of commands (strings).
- Commands will always be properly formatted and at most one per second.

Output:
- A comma-separated string of responses to the commands, in the order they are processed.

Example Input:
[
    "INIT,Alice,1000,Bank1,Bank2",
    "INIT,Bob,500,Bank3",
    "POST,1,Alice,Bob,200",
    "GET,2,Alice",
    "POST,3,Bob,Alice,100",
    "GET,4,Bob",
    "POST,5,Bank3,Alice,300",
    "POST,6,Alice,Bank2,500"
]

Example Output:
"SUCCESS,800,SUCCESS,600,SUCCESS,SUCCESS"
"""


from typing import List, Optional

FAIL = "FAILURE"
PASS = "SUCCESS"

class StripePay:

    def __init__(self, commands: List[str]) -> None:
        self.commands = commands
        self.accounts = dict()
        self.banks = set()

    def _init_account(self, user: str, balance: int, banks: List[str]) -> None:
        self.accounts[user] = {}
        deposit = balance // len(banks)
        for bank in banks:
            self.accounts[user][bank] = deposit
            self.banks.add(bank)

    def _transfer(self, sender: str, receiver: str, amount: int) -> str:
        is_sender_bank = self.__is_bank(sender)
        is_receiver_bank = self.__is_bank(receiver)

        if is_sender_bank and is_receiver_bank:
            return FAIL
        
        is_peer_to_peer = self.__is_user_exist(sender) and self.__is_user_exist(receiver)
        is_withdrawal = self.__is_user_exist(sender) and is_receiver_bank
        is_deposit = self.__is_user_exist(receiver) and is_sender_bank

        if is_peer_to_peer:
            if self._get_balance(sender) < amount:
                return FAIL # not enough balance
            pending = amount
            for bank, balance in self.accounts[sender].items():
                if not pending:
                    break

                if pending >= balance:
                    remainder = 0
                    pending -= balance
                    self.accounts[sender][bank] = remainder
                elif pending < balance:
                    remainder = balance - pending
                    pending = 0
                    self.accounts[sender][bank] = remainder

            deposit = amount // len(self.accounts[receiver])
            for bank in self.accounts[receiver]:
                self.accounts[receiver][bank] += deposit
            return PASS

        elif is_deposit:
            if sender not in self.accounts[receiver]:
                return FAIL # bank does not exist for user
            self.accounts[receiver][sender] += amount # add to balance of user's bank account     
            return PASS 
           
        elif is_withdrawal:    
            if receiver not in self.accounts[sender]:
                return FAIL # bank does not exist for user
            if self.accounts[sender][receiver] < amount:
                return FAIL # transaction will fail as not enough balance
            self.accounts[sender][receiver] -= amount
            return PASS

        return FAIL # none of the transaction case satisfied.    
        
    def __is_bank(self, name: str) -> bool:
        return name in self.banks
    
    def __is_user_exist(self, name: str) -> bool:
        return name in self.accounts

    def _get_balance(self, user: str) -> int:
        total_balance = 0

        if not self.__is_user_exist(user):
            return FAIL
        
        for bank, balance in self.accounts[user].items():
            total_balance += balance
        return total_balance

    def _execute_command(self, instructions: List[str]) -> None:
        if instructions[0] == "INIT":
            output = self._init_account(user=instructions[1], balance=int(instructions[2]), banks=instructions[3:])
        elif instructions[0] == "GET":
            output = self._get_balance(user=instructions[2])
        elif instructions[0] == "POST":
            output = self._transfer(sender=instructions[2], receiver=instructions[3], amount=int(instructions[4]))
        
        return output
        
    def process_transactions(self) -> None:
        output = []
        commands = [c.split(',') for c in self.commands]
        for command in commands:
            response = self._execute_command(instructions=command)
            print(self.accounts)
            if response:
                output.append(str(response))
        return ",".join(output)
    
if __name__ == "__main__":
    commands = [
       "INIT,Alice,1000,Bank1,Bank2",
        "INIT,Bob,500,Bank3",
        "POST,1,Alice,Bob,200",
        "GET,2,Alice",
        "POST,3,Bob,Alice,100",
        "GET,4,Bob",
        "POST,5,Bank3,Alice,300",
        "POST,6,Alice,Bank2,500" 
    ]
    sp = StripePay(commands=commands)
    print(sp.process_transactions())
        
