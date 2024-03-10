def hackerlandRadioTransmitters(arr, distance):
    arr.sort()

    transmitters = 0
    idx = len(arr) - 1

    while idx >= 0:
        # Iterate twice for distance, once each for cities after / before transmitter
        for _ in range(2):
            remaining = distance

            while remaining >= 0 and idx >= 1:
                cur, nxt = arr[idx], arr[idx - 1]
                diff = cur - nxt
                remaining -= diff

                if remaining >= 0: idx -= 1

        transmitters += 1
        idx -= 1

    return transmitters