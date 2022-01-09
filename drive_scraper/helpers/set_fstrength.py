def set_filter_strength():
    filter_strength = input("Set Filter Strength (Recommended Between 0.1 - 1): ")

    try:
        filter_strength = float(filter_strength)
    except:
        while isinstance(filter_strength, float) is not True:
            print("Not A Number")
            print("")
            try:
                filter_strength = float(
                    input("Set Filter Strength (Recommended Between 0.01 - 0.1): ")
                )
                break
            except:
                print("Not A Number")
                print("")

    print("Filter Strength Set: " + str(filter_strength))
    print("")

    fs = "Percent>=" + str(filter_strength)

    return fs
