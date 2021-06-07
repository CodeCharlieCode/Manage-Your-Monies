import pdb
from models.merchant import Merchant

import repositories.merchant_repository as merchant_repository 

merchant_repository.delete_all()

merchant1 = Merchant('Tesco')
merchant_repository.save(merchant1)

merchant2 = Merchant('Sainsburys')
merchant_repository.save(merchant2)

merchant3 = Merchant('Amazon')
merchant_repository.save(merchant3)

pdb.set_trace()