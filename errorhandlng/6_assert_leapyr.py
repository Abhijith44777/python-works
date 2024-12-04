def is_leap_year(year):
    if year<0:
        return False
        
    if year%4==0 and year%100!=0 or year%400==0 and year%100==0:
        return True

    else:
        return False

def test_is_leap_year():
    assert is_leap_year(2024)==True,"non century year check failed"
    assert is_leap_year(2025)==False,"invalid noncentury year check failed"
    assert is_leap_year(2000)==True,"century leap year check failed"
    assert is_leap_year(1900)==False,"invalid century year check failed"
    assert is_leap_year(-2029)==False,"invalid year check failed"
    
try:
    test_is_leap_year()
    print("text case pass")

except Exception  as e:
    print("text failes",e)