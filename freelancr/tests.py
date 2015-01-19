from freelancr.models import Activity, Project, Customer
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

class CustomerTest(APITestCase):
  def test_customer(self):
    """
    Adding a customer
    """

    """
    No customers initially
    """
    response = self.client.get('/customer/', format='json')
    self.assertEqual(response.data, [])

    """
    Add a customer and checking response
    """
    customer = {'name': 'Company', 'street': 'Main Street', 'phone': '12345678'}
    response = self.client.post('/customer/', customer, format='json')
    responseCustomer = response.data
    self.assertEqual(responseCustomer['name'], customer['name'])
    self.assertEqual(responseCustomer['street'], customer['street'])
    self.assertEqual(responseCustomer['phone'], customer['phone'])
    self.assertEqual(responseCustomer['id'], 1)

    """
    Getting all customers - created customer should be there
    """
    response = self.client.get('/customer/', format='json')
    self.assertEqual(len(response.data), 1)
    self.assertEqual(response.data[0]['name'], customer['name'])
    self.assertEqual(response.data[0]['street'], customer['street'])
    self.assertEqual(response.data[0]['phone'], customer['phone'])
    self.assertEqual(response.data[0]['id'], responseCustomer['id'])

    """
    Get specific costumer
    """
    response = self.client.get('/customer/' + str(responseCustomer['id']) + '/', format='json')
    self.assertEqual(response.data['name'], customer['name'])
    self.assertEqual(response.data['street'], customer['street'])
    self.assertEqual(response.data['phone'], customer['phone'])
    self.assertEqual(response.data['id'], responseCustomer['id'])

    """
    Add another customer and checking response
    """
    secondCustomer = {'name': 'Company Number Two', 'street': 'Broadway', 'phone': '555-202-222'}
    response = self.client.post('/customer/', secondCustomer, format='json')
    self.assertEqual(response.data['name'], secondCustomer['name'])
    self.assertEqual(response.data['street'], secondCustomer['street'])
    self.assertEqual(response.data['phone'], secondCustomer['phone'])
    self.assertEqual(response.data['id'], 2)

    """
    Get specific second costumer
    """
    secondCustomerId = str(response.data['id'])
    response = self.client.get('/customer/' + secondCustomerId + '/', format='json')
    self.assertEqual(response.data['name'], secondCustomer['name'])
    self.assertEqual(response.data['street'], secondCustomer['street'])
    self.assertEqual(response.data['phone'], secondCustomer['phone'])
    self.assertEqual(response.data['id'], response.data['id'])

    """
    Getting all customers - both customers should be there
    """
    response = self.client.get('/customer/', format='json')
    self.assertEqual(len(response.data), 2)
    self.assertEqual(response.data[0]['name'], customer['name'])
    self.assertEqual(response.data[0]['street'], customer['street'])
    self.assertEqual(response.data[0]['phone'], customer['phone'])
    self.assertEqual(response.data[1]['name'], secondCustomer['name'])
    self.assertEqual(response.data[1]['street'], secondCustomer['street'])
    self.assertEqual(response.data[1]['phone'], secondCustomer['phone'])

    """
    Editing a customer
    """
    editCustomer = dict(responseCustomer)
    editCustomer['name'] = 'Apple Inc.'
    response = self.client.put('/customer/' + str(responseCustomer['id']) + '/', editCustomer, format='json')
    self.assertEqual(response.data['name'], editCustomer['name'])
    self.assertEqual(response.data['street'], customer['street'])
    self.assertEqual(response.data['phone'], customer['phone'])
    self.assertEqual(response.data['id'], 1)

    """
    Removing the first customer
    """
    response = self.client.delete('/customer/' + str(responseCustomer['id']) + '/', format='json')
    response = self.client.get('/customer/' + str(responseCustomer['id']) + '/', format='json')
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    """
    Get specific second costumer
    """
    response = self.client.get('/customer/' + secondCustomerId + '/', format='json')
    self.assertEqual(response.data['name'], secondCustomer['name'])
    self.assertEqual(response.data['street'], secondCustomer['street'])
    self.assertEqual(response.data['phone'], secondCustomer['phone'])
    self.assertEqual(response.data['id'], response.data['id'])

    """
    Getting all customers - only the second customer should be there
    """
    response = self.client.get('/customer/', format='json')
    self.assertEqual(len(response.data), 1)
    self.assertEqual(response.data[0]['name'], secondCustomer['name'])
    self.assertEqual(response.data[0]['street'], secondCustomer['street'])
    self.assertEqual(response.data[0]['phone'], secondCustomer['phone'])
    
    # class ProjectTest(APITestCase):