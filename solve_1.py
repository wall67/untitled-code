from dataclasses import dataclass

@dataclass
class User:
  id: int
  email: str


@dataclass
class BankAccount:
  id: str
  user: User
  currency: str
  amount: float


@dataclass
class Transfer:
    id: int
    from_user: User
    to_user: User
    amount: float
    currency: str  


@dataclass
class TransferResponse:
  # status will be "error" or "pending" or "complete"
  status: str
  message: str
  external_id: str


@dataclass
class TransferServiceResponse:
    
    def __init__(self, TransferResponse, transfer):
        self.response = TransferResponse
        self.transfer = transfer
        
    def __str__(self) -> str:
        return f"TransferServiceResponse({self.response}, {self.transfer})"

    def  notify_user(self, user: User):
        if user.id == self.transfer.from_user.id:
            if self.response.status == "error":
                print(f"Notify user {user.id} that the transfer from {self.transfer.from_user.id} to {self.transfer.to_user.id} is {self.response.status} with message {self.response.message}")
            elif self.response.status == "pending":
                print(f"Notify user {user.id} that the transfer from {self.transfer.from_user.id} to {self.transfer.to_user.id} is {self.response.status} with message {self.response.message}")
            elif self.response.status == "complete":
                print(f"Notify user {user.id} that the transfer from {self.transfer.from_user.id} to {self.transfer.to_user.id} is {self.response.status} with message {self.response.message}")
            else:
                print(f"Notify user {user.id} that the transfer from {self.transfer.from_user.id} to {self.transfer.to_user.id} is Unknown status {self.response.status} with message {self.response.message}")
        elif user.id == self.transfer.to_user.id:
            if self.response.status == "error":
                print(f"Notify user {user.id} that the transfer from {self.transfer.from_user.id} to {self.transfer.to_user.id} is {self.response.status} with message {self.response.message}")
            elif self.response.status == "pending":
                print(f"Notify user {user.id} that the transfer from {self.transfer.from_user.id} to {self.transfer.to_user.id} is {self.response.status} with message {self.response.message}")
            elif self.response.status == "complete":
                print(f"Notify user {user.id} that the transfer from {self.transfer.from_user.id} to {self.transfer.to_user.id} is {self.response.status} with message {self.response.message}")
            else:
                print(f"Notify user {user.id} that the transfer from {self.transfer.from_user.id} to {self.transfer.to_user.id} is Unknown status {self.response.status} with message {self.response.message}")
        else:
            print(f"Log that the transfer from {self.transfer.from_user.id} to {self.transfer.to_user.id} is Unknown user {user.id}")     

class BankAccountService:

  def get_balance(bank_account: BankAccount) -> float:
    # stub of a method that calls an external API 
    # that returns the current balance of a bank account
    return 100.0

  def transfer_money(transfer: Transfer) -> TransferResponse:
    # stub of a method that calls an external API
    # that transfers money and returns a response object
    return TransferResponse("pending", "Transfer pending", "abc-123")

  def get_transfer_status(external_id: str) -> TransferResponse:
    # stub of a method that calls an external API
    # that gets the status of a transfer from the external id
    return TransferResponse("complete", "Transfer complete", "abc-123")

  

class TransferService:

  def transfer(transfer: Transfer) -> TransferServiceResponse:
    #validate transfer amount
    if transfer.amount <= 0:
        return TransferServiceResponse(TransferResponse("error", "Transfer amount must be greater than 0", "0758x52"), transfer)  
    #validate transfer currency
    if transfer.currency != "EUR":
        return TransferServiceResponse(TransferResponse("error", "Transfer currency must be EUR", "0758x53"), transfer)
    #validate transfer from_user
    if transfer.from_user is None:
        return TransferServiceResponse(TransferResponse("error", "Transfer from_user must be set", "0758x54"), transfer)
    #validate transfer to_user
    if transfer.to_user is None:
        return TransferServiceResponse(TransferResponse("error", "Transfer to_user must be set", "0758x55"), transfer)
    #validate transfer from_user bank_account
    if transfer.from_user.bank_account is None:
        return TransferServiceResponse(TransferResponse("error", "Transfer from_user bank_account must be set", "0758x56"), transfer)
    #validate transfer to_user bank_account
    if transfer.to_user.bank_account is None:
        return TransferServiceResponse(TransferResponse("error", "Transfer to_user bank_account must be set", "0758x57"), transfer)
    #validate transfer from_user bank_account currency
    if transfer.from_user.bank_account.currency != "EUR":
        return TransferServiceResponse(TransferResponse("error", "Transfer from_user bank_account currency must be EUR", "0758x58"), transfer)
    #validate transfer to_user bank_account currency
    if transfer.to_user.bank_account.currency != "EUR":
        return TransferServiceResponse(TransferResponse("error", "Transfer to_user bank_account currency must be EUR", "0758x59"), transfer)
    #validate transfer from_user bank_account amount
    if BankAccountService.get_balance(transfer.from_user.bank_account) < transfer.amount:
        return TransferServiceResponse(TransferResponse("error", "Transfer from_user bank_account amount must be greater than transfer amount", "0758x60"), transfer)
    
    #call external API to transfer money
    response = BankAccountService.transfer_money(transfer)
    #if transfer fails, return error
    if BankAccountService.get_transfer_status(response.external_id).status == "error":
        return TransferServiceResponse(response, transfer)
    elif BankAccountService.get_transfer_status(response.external_id).status == "pending":
        return TransferServiceResponse(response, transfer)
    elif BankAccountService.get_transfer_status(response.external_id).status == "complete":
        return TransferServiceResponse(response, transfer)
    else:
        return TransferServiceResponse(TransferResponse("error", "Unknown status", "0758x61"), transfer)
    
   