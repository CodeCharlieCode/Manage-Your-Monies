from models.transactions import Transaction
from models.category import Category
import pdb
from models.merchant import Merchant
from models.category import Category
from models.profile import Profile
import repositories.merchant_repository as merchant_repository 
import repositories.category_repository as category_repository
import repositories.transaction_repositiory as transaction_repository
import repositories.profile_repository as profile_repository 

merchant_repository.delete_all()
category_repository.delete_all()
transaction_repository.delete_all()

import datetime
x = datetime.datetime.now()

profile1= Profile(100, 90)
profile_repository.save(profile1)

profile2= Profile(120,80)
profile_repository.save(profile2)

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

transaction1 = Transaction(merchant1, category1, "Weekly food shop", 50, x)
transaction_repository.save(transaction1)

transaction2 = Transaction(merchant3, category2, "Purchased a film", 1.99, x)
transaction_repository.save(transaction2)

transaction3 = Transaction(merchant1, category1, "Top up shop", 5, x)
transaction_repository.save(transaction3)

transaction4 = Transaction(merchant2, category2, "video game", 45.99, x)
transaction_repository.save(transaction4)

pdb.set_trace()