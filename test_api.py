import requests
import json

BASE_URL = "http://localhost:5555"

def print_test(name, passed):
    status = "✓ PASS" if passed else "✗ FAIL"
    print(f"{status} - {name}")

def test_get_heroes():
    """Test GET /heroes"""
    response = requests.get(f"{BASE_URL}/heroes")
    passed = response.status_code == 200 and isinstance(response.json(), list)
    print_test("GET /heroes", passed)
    if not passed:
        print(f"  Response: {response.status_code}, {response.text}")
    return passed

def test_get_hero_by_id():
    """Test GET /heroes/1"""
    response = requests.get(f"{BASE_URL}/heroes/1")
    data = response.json()
    passed = (
        response.status_code == 200 and 
        'hero_powers' in data and
        isinstance(data['hero_powers'], list)
    )
    print_test("GET /heroes/1", passed)
    if not passed:
        print(f"  Response: {response.status_code}, {response.text}")
    return passed

def test_get_hero_not_found():
    """Test GET /heroes/999 (not found)"""
    response = requests.get(f"{BASE_URL}/heroes/999")
    data = response.json()
    passed = response.status_code == 404 and 'error' in data
    print_test("GET /heroes/999 (404)", passed)
    if not passed:
        print(f"  Response: {response.status_code}, {response.text}")
    return passed

def test_get_powers():
    """Test GET /powers"""
    response = requests.get(f"{BASE_URL}/powers")
    passed = response.status_code == 200 and isinstance(response.json(), list)
    print_test("GET /powers", passed)
    if not passed:
        print(f"  Response: {response.status_code}, {response.text}")
    return passed

def test_get_power_by_id():
    """Test GET /powers/1"""
    response = requests.get(f"{BASE_URL}/powers/1")
    data = response.json()
    passed = (
        response.status_code == 200 and 
        'description' in data and
        'name' in data
    )
    print_test("GET /powers/1", passed)
    if not passed:
        print(f"  Response: {response.status_code}, {response.text}")
    return passed

def test_get_power_not_found():
    """Test GET /powers/999 (not found)"""
    response = requests.get(f"{BASE_URL}/powers/999")
    data = response.json()
    passed = response.status_code == 404 and 'error' in data
    print_test("GET /powers/999 (404)", passed)
    if not passed:
        print(f"  Response: {response.status_code}, {response.text}")
    return passed

def test_patch_power_valid():
    """Test PATCH /powers/1 with valid data"""
    response = requests.patch(
        f"{BASE_URL}/powers/1",
        json={"description": "This is a valid description with more than 20 characters"}
    )
    data = response.json()
    passed = response.status_code == 200 and 'description' in data
    print_test("PATCH /powers/1 (valid)", passed)
    if not passed:
        print(f"  Response: {response.status_code}, {response.text}")
    return passed

def test_patch_power_invalid():
    """Test PATCH /powers/1 with invalid data (too short)"""
    response = requests.patch(
        f"{BASE_URL}/powers/1",
        json={"description": "Too short"}
    )
    data = response.json()
    passed = response.status_code == 400 and 'errors' in data
    print_test("PATCH /powers/1 (invalid)", passed)
    if not passed:
        print(f"  Response: {response.status_code}, {response.text}")
    return passed

def test_post_hero_power_valid():
    """Test POST /hero_powers with valid data"""
    response = requests.post(
        f"{BASE_URL}/hero_powers",
        json={"strength": "Average", "power_id": 1, "hero_id": 2}
    )
    data = response.json()
    passed = (
        response.status_code == 201 and 
        'hero' in data and 
        'power' in data and
        data['strength'] == 'Average'
    )
    print_test("POST /hero_powers (valid)", passed)
    if not passed:
        print(f"  Response: {response.status_code}, {response.text}")
    return passed

def test_post_hero_power_invalid():
    """Test POST /hero_powers with invalid strength"""
    response = requests.post(
        f"{BASE_URL}/hero_powers",
        json={"strength": "Super", "power_id": 1, "hero_id": 2}
    )
    data = response.json()
    passed = response.status_code == 400 and 'errors' in data
    print_test("POST /hero_powers (invalid)", passed)
    if not passed:
        print(f"  Response: {response.status_code}, {response.text}")
    return passed

def main():
    print("=" * 50)
    print("FLASK HERO POWERS API - TEST SUITE")
    print("=" * 50)
    print("\nMake sure the Flask server is running on port 5555!\n")
    
    tests = [
        test_get_heroes,
        test_get_hero_by_id,
        test_get_hero_not_found,
        test_get_powers,
        test_get_power_by_id,
        test_get_power_not_found,
        test_patch_power_valid,
        test_patch_power_invalid,
        test_post_hero_power_valid,
        test_post_hero_power_invalid,
    ]
    
    results = []
    for test in tests:
        try:
            results.append(test())
        except Exception as e:
            print(f"✗ FAIL - {test.__name__}: {str(e)}")
            results.append(False)
        print()
    
    print("=" * 50)
    passed = sum(results)
    total = len(results)
    percentage = (passed / total) * 100
    
    print(f"RESULTS: {passed}/{total} tests passed ({percentage:.0f}%)")
    
    if passed == total:
        print("🎉 All tests passed! Ready to submit!")
    else:
        print("⚠️  Some tests failed. Please review the errors above.")
    print("=" * 50)

if __name__ == "__main__":
    main()