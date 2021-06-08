from models.transactions import Transaction
from models.category import Category
import pdb
from models.merchant import Merchant
from models.category import Category

import repositories.merchant_repository as merchant_repository 
import repositories.category_repository as category_repository
import repositories.transaction_repositiory as transaction_repository

merchant_repository.delete_all()
category_repository.delete_all()

merchant1 = Merchant("Tesco")
merchant_repository.save(merchant1)

merchant2 = Merchant("Sainsburys")
merchant_repository.save(merchant2)

merchant3 = Merchant("Amazon")
merchant_repository.save(merchant3)

category1 = Category("Food")
category_repository.save(category1)

category2 = Category("Entertainment")
category_repository.save(category2)

transaction1 = Transaction(merchant1, category1, "Weekly food shop", 50)
transaction_repository.save(transaction1)

transaction2 = Transaction(merchant3, category2, "Purchased a film", 1.99)
transaction_repository.save(transaction2)

transaction3 = Transaction(merchant1, category1, "Top up shop", 5)
transaction_repository.save(transaction3)

pdb.set_trace()