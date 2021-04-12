import unittest
from datetime import datetime, timedelta
from bikeRental import BikeRental, Customer

class BikeRentalTest(unittest.TestCase):
    
    def test_bike_rental_displays_corrct_stock(self):
        
        shop1 = BikeRental()
        shop2 = BikeRental(10)
        self.assertEqual(shop1.display_stock(),0)
        self.assertEqual(shop2.display_stock(),10)
        
    def test_hourly_basis_negative_input(self):
        
        shop = BikeRental(10)
        self.assertEqual(shop.Rent_bike_on_hourly_basis(-1),None)
    
    def test_hourly_basis_zero_input(self):
        
        shop = BikeRental(10)
        self.assertEqual(shop.Rent_bike_on_hourly_basis(0),None)
        
    def test_hourly_basis_valid_input(self):
        
        shop = BikeRental(10)
        hour = datetime.now().hour
        self.assertEqual(shop.Rent_bike_on_hourly_basis(2).hour,hour)
        
    def test_hourly_basis_invalid_input(self):
        
        shop = BikeRental(10)
        self.assertEqual(shop.Rent_bike_on_hourly_basis(11),None)
        
    def test_daily_basis_negative_input(self):
        
        shop = BikeRental(10)
        self.assertEqual(shop.Rent_bike_on_daily_basis(-1),None)
    
    def test_daily_basis_zero_input(self):
        
        shop = BikeRental(10)
        self.assertEqual(shop.Rent_bike_on_daily_basis(0),None)
        
    def test_daily_basis_valid_input(self):
        
        shop = BikeRental(10)
        hour = datetime.now().hour
        self.assertEqual(shop.Rent_bike_on_daily_basis(2).hour,hour)
        
    def test_daily_basis_invalid_input(self):
        
        shop = BikeRental(10)
        self.assertEqual(shop.Rent_bike_on_daily_basis(11),None)
        
    def test_weekly_basis_negative_input(self):
        
        shop = BikeRental(10)
        self.assertEqual(shop.Rent_bike_on_weekly_basis(-1),None)
    
    def test_weekly_basis_zero_input(self):
        
        shop = BikeRental(10)
        self.assertEqual(shop.Rent_bike_on_weekly_basis(0),None)
        
    def test_weekly_basis_valid_input(self):
        
        shop = BikeRental(10)
        hour = datetime.now().hour
        self.assertEqual(shop.Rent_bike_on_weekly_basis(2).hour,hour)
        
    def test_weekly_basis_invalid_input(self):
        
        shop = BikeRental(10)
        self.assertEqual(shop.Rent_bike_on_weekly_basis(11),None)
        
    def test_returnbike_for_invalid_rentaltime(self):
        shop = BikeRental(10)
        customer = Customer()
        
        request = customer.return_bike()
        self.assertIsNone(shop.return_bike(request))
        
        self.assertIsNone(shop.return_bike((0,0,0)))
        
    def test_returnbike_for_invalid_rentalbasis(self):
        shop = BikeRental(10)
        customer = Customer()
        
        # create valid rentalTime and bikes
        customer.rentalTime = datetime.now()
        customer.bikes = 3

        # create invalid rentalbasis
        customer.rentalBasis = 7

        request = customer.return_bike()
        self.assertEqual(shop.return_bike(request), 0)
        
    def test_returnbike_for_invalid_numofbikes(self):
        shop = BikeRental(10)
        customer = Customer()
        customer.rentalTime = datetime.now()
        #invalid
        customer.numOfBikes = 0
        
        customer.rentalBasis = 1
        request = customer.return_bike()
        self.assertIsNone(shop.return_bike(request)) 
        
    def test_returnbike_valid(self):
        
        #shop and valid cust
        shop = BikeRental(30)
        customer1 = Customer()
        customer2 = Customer()
        customer3 = Customer()
        customer4 = Customer()
        
        #valid rental basis
        customer1.rentalBasis = 1
        customer2.rentalBasis = 1
        customer3.rentalBasis = 2
        customer4.rentalBasis = 2
        
        #valid bikes
        customer1.bikes = 1
        customer2.bikes = 5 #disc
        customer3.bikes = 2
        customer4.bikes = 8
        
        #create past valid time
        customer1.rentalTime = datetime.now() + timedelta(hours=-4)
        customer2.rentalTime = datetime.now() + timedelta(hours=-23)
        customer3.rentalTime = datetime.now() + timedelta(days=-4)
        customer4.rentalTime = datetime.now() + timedelta(days=-13)
        
        #return
        request1 = customer1.return_bike()
        request2 = customer2.return_bike()
        request3 = customer3.return_bike()
        request4 = customer4.return_bike()
        
        #correct bill
        self.assertEqual(shop.return_bike(request1),20)
        self.assertEqual(shop.return_bike(request2),402.5)
        self.assertEqual(shop.return_bike(request3),160)
        self.assertEqual(shop.return_bike(request4),2080)
        
class CustomerTest(unittest.TestCase):
    def test_return_with_valid(self):
        customer = Customer()
        customer.rentalBasis = 1
        now = datetime.now()
        customer.rentalTime = now
        customer.bikes = 4
        self.assertEqual(customer.return_bike(),(1,now,4))
        
    def test_return_with_invalid(self):
        customer = Customer()
        customer.rentalBasis = 1
        
        #invalid
        customer.rentalTime = 0
        customer.bikes = 0
        
        self.assertEqual(customer.return_bike(),(0,0,0))

if __name__ == "__main__":
    unittest.main()