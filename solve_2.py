from dataclasses import dataclass

@dataclass
class User:
    # write all necessary fields
    id: int
    name: str
    email: str
    phone: str
    birth_date: str
    address: str
    
# write a class BankAccount with all necessary fields

@dataclass
class BankAccount:
    id: str
    user: User
    currency: str
    amount: float

# Wallet: a users wallet for a specific currency on our platform
@dataclass
class Wallet:
    id: str
    user: User
    currency: str
    amount: float

# ExternalTransfer: a transfer from a BankAccount to a Wallet
@dataclass
class ExternalTransfer:
    id: str
    from_account: BankAccount
    to_wallet: Wallet
    amount: float
    currency: str

# InternalTransfer: a transfer between Wallets
@dataclass
class InternalTransfer:
    id: str
    from_wallet: Wallet
    to_wallet: Wallet
    amount: float
    currency: str

# ExchangeType: the type of exchange
#   - "buy" means that the user is buying a currency
#   - "sell" means that the user is selling a currency
@dataclass
class ExchangeType:
    id: str
    name: str

# ExchangeSource: the source of the exchange
#   - "internal" means that the exchange is between two wallets on our platform
#   - "external" means that the exchange is between a wallet on our platform and a bank account
@dataclass
class ExchangeSource:
    id: str
    name: str

# Exchange: an exchange between two currencies
@dataclass
class Exchange:
    id: str
    amount: float
    from_currency: str
    to_currency: str
    exchange_type: ExchangeType
    exchange_source: ExchangeSource
    user : User
    
# Transaction: tracks any change to the balance of a Wallet
@dataclass
class Transaction:
    id: str
    wallet: Wallet
    amount: float
    type: str
    source: str
    date: str
    status: str
    message: str
