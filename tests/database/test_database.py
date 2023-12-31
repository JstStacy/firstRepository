import pytest
from modules.common.database import Database
import sqlite3

# Check db connection
@pytest.mark.database
def test_database_connection(database):
    database.test_connection()


@pytest.mark.database
def test_check_all_users(database):
    users = database.get_all_users()

    # Print collected data
    print(users)


@pytest.mark.database
def test_check_user_sergii(database):
    user = database.get_user_address_by_name('Sergii')
    
    # Check that we got expected data
    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'


@pytest.mark.database
def test_product_qnt_by_id(database):
    database.update_product_qnt_by_id(1, 25)
    water_qnt = database.select_product_qnt_by_id(1)

    # Check changes in DB
    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_product_insert(database):
    database.insert_product(4,'печиво', 'солодке', 30)
    cookies_qnt = database.select_product_qnt_by_id(4)

    # Check the number of goods is equal to expected
    assert cookies_qnt [0][0] == 30


@pytest.mark.database
def test_product_delete(database):
    database.insert_product(99, 'тестові', 'дані', 999)
    database.delete_product_by_id(99)
    qnt = database.select_product_qnt_by_id(99)

    assert len(qnt) == 0


@pytest.mark.database
def test_detailed_orders(database):
    orders = database.get_detailed_orders()
    
    #Check quantity of orders equal to 1
    assert len(orders) == 1

    #Check structure of data
    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'
    assert orders[0][3] == 'з цукром'


# Individual part
@pytest.mark.database
def test_customer_insert(database):
    database.insert_customer(3, 'Anastasiia', 'Nauky Ave.', 'Kharkiv', '63200', 'Ukraine')
    users = database.get_all_users()

    # Check data
    assert users[2][1] == 'Nauky Ave.'

# Check postal code with correct length
@pytest.mark.database
def test_customer_postalCode_length(database):
    try:
        postalCode = database.get_customer_postalCode('Anastasiia')
        for data in postalCode:
            assert len(data[0]) == 5
    except Exception:
        print('Wrong Postal Code')

# Check postal code with wrong length
@pytest.mark.database
def test_customer_postalCode_length(database):
    try:
        postalCode = database.get_customer_postalCode('Sergii')
        for data in postalCode:
            assert len(data[0]) == 5
    except Exception:
        print('Wrong Postal Code')

# Check error occur because of wrong data type 
@pytest.mark.database
def test_input_wrong_data_type(database):
    with pytest.raises(sqlite3.OperationalError) as error:
        database.update_product_qnt_by_id(1, 'some')

    assert str(error.value) == 'no such column: some'




