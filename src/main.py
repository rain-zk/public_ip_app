from ip_service import get_my_ip_data

def run_app():
    print("================================")
    print("   PUBLIC IP LOOKUP TOOL        ")
    print("================================")

    data = get_my_ip_data()

    if "error" in data:
        print(f"FAILED: {data['error']}")
    else:
        print(f"IP ADDRESS:  {data.get('ip')}")
        print(f"LOCATION:   {data.get('city')}, {data.get('country_name')}")
        print(f"SERVICE:    {data.get('org')}")
    print("================================")

if __name__ == "__main__":
    run_app()