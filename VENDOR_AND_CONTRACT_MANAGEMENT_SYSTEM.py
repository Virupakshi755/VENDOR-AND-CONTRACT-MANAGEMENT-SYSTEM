from datetime import datetime,timedelta
import random

class VendorContractManagementSystem:

    def _init_(self):
        self.vendors = {}
        self.contracts = {}

    def create_vendor(self, vendor_id, name,contact_number):
        if vendor_id not in self.vendors:
            self.vendors[vendor_id] = {
                'name': name,
                'vendor_id':vendor_id,
                'contact_number': contact_number
            }
            print('..............................................')
            print(f"Vendor: {name} with ID: {vendor_id} and\nContact Number: {contact_number}  created successfully.")
            print('..............................................')
        else:
            vendor_id=random.randint(1000,9999)
            self.vendors[vendor_id]={
                'name': name,
                'vendor_id':vendor_id,
                'contact_number': contact_number
            }
            print('..............................................')
            print(f"Vendor: {name} with ID: {vendor_id} and\nContact Number: {contact_number}  created successfully.")
            print('..............................................')




    def update_vendor(self, vendor_id, name,contact_number):
        if vendor_id in self.vendors:
            key=input('Enter string what need to be updated')
            if key.lower() == 'name':
                inp=input('Enter Name to be updated')
                self.vendors[vendor_id][key]=inp
                print(f'Name :{inp} of id {vendor_id} updated successfully')
            elif key.lower() == 'contact_number':
                inp=random.randint(6000000000,9999999999)
                self.vendors[vendor_id][key]=inp
            else:
                print('No such Attribute found')

        else:print('Vendor id not found')

    def read_vendor(self, vendor_id):
        if vendor_id in self.vendors:
            print(f"Vendor ID: {vendor_id}")
            print(f"Name: {self.vendors[vendor_id]['name']}")
            print(f"Contact Number: {self.vendors[vendor_id]['contact_number']}")
        else:
            print(f"Vendor with ID {vendor_id} not found.")

    def delete_vendor(self, vendor_id):
        if vendor_id in self.vendors:
            del self.vendors[vendor_id]
            print(f"Vendor of id {vendor_id} deleted successfully.")
        else:
            print(f"Vendor with ID {vendor_id} not found.")

    def create_contract(self, contract_id, vendor_id, start_date, end_date, value):
        if contract_id not in self.contracts:
            self.contracts[contract_id] = {
                'vendor_id': vendor_id,
                'start_date': start_date,
                'end_date': end_date,
                'value': value
            }
            print('..............................................')
            print(f"Vendor of ID:{vendor_id},\nContract of ID: {contract_id},\nStart_Date:{start_date},\nEnd_Dtae:{end_date} and\nValue:{value} created successfully.")
            print('..............................................')
        else:
            contract_id=random.randint(1000,9999)
            self.contracts[contract_id] = {
                'vendor_id': vendor_id,
                'start_date': start_date,
                'end_date': end_date,
                'value': value
            }
            print('..............................................')
            print(f"Contract of ID: {contract_id},\n Start_Date:{start_date},\n End_Dtae:{end_date} created successfully.")
            print('..............................................')
            
           
    def update_contract(self, contract_id,start_date, end_date, value):
        if contract_id in self.contracts:
            key=input('Enter a string')
            if key in self.contracts[contract_id]:
                d=int(input('Enter how many days to extend'))
                end_date=end_date+timedelta(d)
                self.contracts[contract_id][key] = end_date
                print(f"Contract {contract_id} of {d} days extended and updated successfully.") 
            else:
                print('NO such attribute found')

        else:
            print(f"Contract with ID {contract_id} not found.")

    def read_contract(self, contract_id):
        if contract_id in self.contracts:
            print('..............................................')
            print(f"Contract ID: {contract_id}")
            print(f"Vendor ID: {self.contracts[contract_id]['vendor_id']}")
            print(f"Start Date: {self.contracts[contract_id]['start_date']}")
            print(f"End Date: {self.contracts[contract_id]['end_date']}")
            print(f"Value: {self.contracts[contract_id]['value']}")
            print('..............................................')
        else:
            print(f"Contract with ID {contract_id} not found.")
            

    def delete_contract(self, contract_id):
        if contract_id in self.contracts:
            del self.contracts[contract_id]
            print('..............................................')
            print(f"Contract of id {contract_id} deleted successfully.")
            print('..............................................')
        else:
            print('..............................................')
            print(f"Contract with ID {contract_id} not found.")
            print('..............................................')



    def alert_contract_expiry(self,contract_id):
        if contract_id in self.contracts:
            manufacture_date=datetime.now()
            expiry_date=manufacture_date+timedelta(days=30,hours=5)
            print(manufacture_date)
            print(expiry_date)
            if expiry_date-manufacture_date<timedelta(days=10):
                print('Expiray Date is Nearing')
            else:
                print(f'still {expiry_date-manufacture_date} remaining')

        else:
            print(f"Contract with ID '{contract_id}' not found.")

        
    def evaluate_vendor_performance(self, vendor_id):
        r=0.0
        n=len(self.contracts)
        num=float(n)
        if vendor_id in self.vendors:
            for i in range(n):
                contract_id=int(input('Enter the contract id:'))
                if contract_id in self.contracts:
                    rate=float(input('Enter the Rating for vendor with id {vendor_id} and \ncontract with id {contract_id} \n{rate such as 1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0}:'))
                    if rate%0.5==0 and rate<=5:
                        r+=rate
                        av=r/num
            i=[1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0]
            if av in i:
                print(f"Evaluating performance for Vendor ID {vendor_id} with rate {av} ")
                
            else:
                raise ValueError('Rate as per shown')
                            
        else:
            print(f"Vendor with ID {vendor_id} not found.")

management_system = VendorContractManagementSystem()
while True:
    print('..........................................................')
    print('1. Create Vendor\n 2. Read Vendor\n 3. Update Vendor\n 4. Delete Vendor\n 5. Create Contract\n 6. Read Contract\n 7. Update Contract\n 8. Delete Contract\n 9. Expiray_Alert\n 10.Performance of vendor\n 11. Exit\n')
    print('..........................................................')
    ch=int(input('Enter your choice'))
    if ch==1:
        print('..........Fill Up VENDOR Details............')
        print()
        vendor_id=random.randint(1000,9999)
        vendor_name=input('Enter the vendor name:')
        vendor_contactno=random.randint(6000000000,9999999999)
        management_system.create_vendor(vendor_id,vendor_name,vendor_contactno)
    elif ch==2:
        vendor_id=int(input('Enter vendor id:'))
        management_system.read_vendor(vendor_id)
    elif ch==3:
        vendor_id=int(input('Enter vendor id:'))
        management_system.update_vendor(vendor_id,vendor_name,vendor_contactno)
    elif ch==4:
        vendor_id=int(input('Enter vendor id:'))
        management_system.delete_vendor(vendor_id)
    elif ch==5:
        start_date=datetime.now()
        end_date=start_date+timedelta(days=30)
        contract_id=random.randint(1000,9999)
        value=random.randint(100000,99999999)
        management_system.create_contract(contract_id,vendor_id,start_date,end_date,value)
    elif ch==6:
        contract_id=int(input('Enter contract id:'))
        management_system.read_contract(contract_id)
    elif ch==7:
        contract_id=int(input('Enter contract id:'))
        management_system.update_contract(contract_id,start_date, end_date, value)
    elif ch==8:
        contract_id=int(input('Enter contract id:'))
        management_system.delete_contract(contract_id)
    elif ch==9:
        contract_id=int(input('Enter contract id:'))
        management_system.alert_contract_expiry(contract_id)
    elif ch==10:
         vendor_id=int(input('Enter the vendor id'))
         management_system.evaluate_vendor_performance(vendor_id)
    elif ch==11:
        print('...........THANK YOU............')
        break
    else:
        print('Please Choose the correct choice_')
